import struct
NULL = -0x80000000
TYPES = {0:'bool',1:'char8',2:'int8',3:'uint8',4:'int16',5:'uint16',6:'int32',7:'uint32',8:'int64',9:'uint64',10:'float',11:'string',12:'hstring',13:'object',14:'vector',15:'f2',16:'f3',17:'f4',18:'tableref',19:'reskey',20:'lockey',21:'variant'}
def rel(b, pos):
    v = struct.unpack_from('<i', b, pos)[0]
    return None if v == NULL else pos + v
def cstr(b, pos):
    e = b.index(b'\0', pos); return b[pos:e].decode()
def parse(b):
    assert b[:4] == b'DATA'
    ver, = struct.unpack_from('<I', b, 4)
    th = rel(b, 8); nt, = struct.unpack_from('<i', b, 12)
    sh = rel(b, 16); ns, = struct.unpack_from('<i', b, 20)
    schemas = {}
    for i in range(ns):
        p = sh + i*24
        no = rel(b, p); nh, shh, ssz = struct.unpack_from('<III', b, p+4); co = rel(b, p+16); nc, = struct.unpack_from('<I', b, p+20)
        cols = []
        for j in range(nc):
            q = co + j*20
            cn = rel(b, q); ch, ct, cf, cof = struct.unpack_from('<IHHI', b, q+4); cs = rel(b, q+16)
            cols.append(dict(name=cstr(b, cn) if cn else None, hash=ch, type=ct, flags=cf, offset=cof, schema=cs))
        schemas[p] = dict(name=cstr(b, no) if no else None, hash=nh, schash=shh, size=ssz, cols=cols)
    tables = []
    for i in range(nt):
        p = th + i*28
        no = rel(b, p); nh, = struct.unpack_from('<I', b, p+4); so = rel(b, p+8)
        dt, rs = struct.unpack_from('<II', b, p+12); ro = rel(b, p+20); rc, = struct.unpack_from('<I', b, p+24)
        tables.append(dict(pos=p, name=cstr(b, no) if no else None, hash=nh, schema=so, type=dt, rowsize=rs, rowoff=ro, rows=rc))
    return dict(ver=ver, tables=tables, schemas=schemas)
def dump(b, info=None):
    info = info or parse(b)
    for t in info['tables']:
        print('TABLE', t['name'], 'type', TYPES.get(t['type']), 'rows', t['rows'], 'rowsize', t['rowsize'], 'at', t['rowoff'])
        if t['schema']:
            s = info['schemas'][t['schema']]
            print('  schema', s['name'], hex(s['schash']), 'size', s['size'])
            for r in range(t['rows']):
                base = t['rowoff'] + r*t['rowsize']
                for c in sorted(s['cols'], key=lambda c: c['offset']):
                    p = base + c['offset']; ty = c['type']
                    if ty == 19: v = '%08X:%08X:%016X' % (struct.unpack_from('<I', b, p+8)[0], struct.unpack_from('<I', b, p+12)[0], struct.unpack_from('<Q', b, p)[0])
                    elif ty in (20, 7): v = hex(struct.unpack_from('<I', b, p)[0])
                    elif ty == 6: v = struct.unpack_from('<i', b, p)[0]
                    elif ty == 10: v = struct.unpack_from('<f', b, p)[0]
                    elif ty in (9, 18): v = struct.unpack_from('<Q', b, p)[0]
                    elif ty == 8: v = struct.unpack_from('<q', b, p)[0]
                    elif ty == 0: v = b[p]
                    elif ty == 14: o = rel(b, p); v = 'vec@%s n=%d' % (o, struct.unpack_from('<I', b, p+4)[0])
                    elif ty == 13: v = 'obj@%s' % rel(b, p)
                    elif ty == 11: o = rel(b, p); v = repr(cstr(b, o)) if o else None
                    else: v = b[p:p+8].hex()
                    print('   [%d] +%d %-40s %-8s %s' % (r, c['offset'], c['name'], TYPES.get(ty), v))
        else:
            vals = [struct.unpack_from('<Q', b, t['rowoff'] + k*t['rowsize'])[0] if t['rowsize']==8 else b[t['rowoff']+k*t['rowsize']:t['rowoff']+(k+1)*t['rowsize']].hex() for k in range(t['rows'])]
            print('  values', vals)
if __name__ == '__main__':
    import sys
    dump(open(sys.argv[1], 'rb').read())

# ---------- model / writer ----------
def fnv32(x):
    h = 0x811C9DC5
    for c in x.lower().encode() if isinstance(x, str) else x: h = ((h * 0x01000193) & 0xFFFFFFFF) ^ c
    return h
PTR_TYPES = (11, 13, 14, 21)
class Model: pass
def load(b):
    info = parse(b); m = Model(); m.ver = info['ver']; m.extra = b[24:32]
    sch_keys = list(info['schemas'].keys())
    m.schemas = [info['schemas'][k] for k in sch_keys]
    for sc in m.schemas:
        for c in sc['cols']: c['schema_idx'] = sch_keys.index(c['schema']) if c['schema'] else None
    ts = info['tables']
    # table extents
    def owner(addr):
        for idx, t in enumerate(ts):
            size = t['rowsize'] * t['rows']
            if t['rowoff'] <= addr < t['rowoff'] + max(size, 1): return idx, addr - t['rowoff']
        raise Exception('dangling pointer %d' % addr)
    m.tables = []
    for t in ts:
        size = t['rowsize'] * t['rows']
        d = dict(name=t['name'], type=t['type'], rowsize=t['rowsize'], rows=t['rows'],
                 schema=(sch_keys.index(t['schema']) if t['schema'] else None),
                 data=bytearray(b[t['rowoff']:t['rowoff'] + size]), ptrs={}, strs={}, hash=t['hash'])
        m.tables.append(d)
    for idx, t in enumerate(ts):
        if not t['schema']: continue
        s = info['schemas'][t['schema']]
        for r in range(t['rows']):
            for c in s['cols']:
                if c['type'] not in PTR_TYPES: continue
                local = r * t['rowsize'] + c['offset']; p = t['rowoff'] + local
                tgt = rel(b, p)
                if tgt is None: continue
                if c['type'] == 11: m.tables[idx]['strs'][local] = cstr(b, tgt)
                else: m.tables[idx]['ptrs'][local] = owner(tgt)
    return m
def col(m, ti, name, row=0):
    t = m.tables[ti]; s = m.schemas[t['schema']]
    for c in s['cols']:
        if c['name'] == name: return row * t['rowsize'] + c['offset'], c['type']
    raise KeyError(name)
def save(m):
    out = bytearray()
    nt, ns = len(m.tables), len(m.schemas)
    th = 32; data0 = th + 28 * nt
    def al(x, a=16): return (x + a - 1) // a * a
    pos = al(data0); offs = []
    for t in m.tables:
        offs.append(pos); pos = al(pos + len(t['data']))
    # schema area must start after the last table's real end
    last_end = offs[-1] + len(m.tables[-1]['data'])
    sch0 = al(last_end); col0 = sch0 + 24 * ns
    colpos = []; p = col0
    for s in m.schemas: colpos.append(p); p += 20 * len(s['cols'])
    strpos = p
    strings = bytearray(); smap = {}
    def S(x):
        if x is None: return None
        if x not in smap: smap[x] = strpos + len(strings); strings.extend(x.encode() + b'\0')
        return smap[x]
    # pre-register strings in a stable order
    for t in m.tables: S(t['name'])
    for s in m.schemas:
        S(s['name'])
        for c in s['cols']: S(c['name'])
    for t in m.tables:
        for v in t['strs'].values(): S(v)
    total = strpos + len(strings)
    out = bytearray(total)
    def wrel(at, target):
        struct.pack_into('<i', out, at, NULL if target is None else target - at)
    out[0:4] = b'DATA'; struct.pack_into('<I', out, 4, m.ver)
    wrel(8, th); struct.pack_into('<i', out, 12, nt); wrel(16, sch0); struct.pack_into('<i', out, 20, ns); out[24:32] = m.extra
    for i, t in enumerate(m.tables):
        p = th + 28 * i
        wrel(p, S(t['name'])); struct.pack_into('<I', out, p + 4, fnv32(t['name']) if t['name'] else 0x811C9DC5)
        wrel(p + 8, sch0 + 24 * t['schema'] if t['schema'] is not None else None)
        struct.pack_into('<II', out, p + 12, t['type'], t['rowsize']); wrel(p + 20, offs[i]); struct.pack_into('<I', out, p + 24, t['rows'])
        out[offs[i]:offs[i] + len(t['data'])] = t['data']
        for local, (tj, toff) in t['ptrs'].items(): wrel(offs[i] + local, offs[tj] + toff)
        for local, v in t['strs'].items(): wrel(offs[i] + local, S(v))
    for k, s in enumerate(m.schemas):
        p = sch0 + 24 * k
        wrel(p, S(s['name'])); struct.pack_into('<III', out, p + 4, s['hash'], s['schash'], s['size']); wrel(p + 16, colpos[k]); struct.pack_into('<I', out, p + 20, len(s['cols']))
        for j, c in enumerate(s['cols']):
            q = colpos[k] + 20 * j
            wrel(q, S(c['name'])); struct.pack_into('<IHHI', out, q + 4, c['hash'], c['type'], c['flags'], c['offset'])
            wrel(q + 16, None if c['schema_idx'] is None else sch0 + 24 * c['schema_idx'])
    out[strpos:] = strings
    return bytes(out)
