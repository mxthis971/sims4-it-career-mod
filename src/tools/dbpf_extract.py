import struct, sys, zlib, os
def read_index(path):
    f = open(path, 'rb'); h = f.read(96)
    assert h[:4] == b'DBPF', path
    count = struct.unpack_from('<I', h, 36)[0]
    pos = struct.unpack_from('<I', h, 64)[0] or struct.unpack_from('<I', h, 40)[0]
    f.seek(pos); flags = struct.unpack('<I', f.read(4))[0]
    const = {}
    for i in range(8):
        if flags & (1 << i): const[i] = struct.unpack('<I', f.read(4))[0]
    ents = []
    for _ in range(count):
        v = []
        for i in range(8):
            v.append(const[i] if i in const else struct.unpack('<I', f.read(4))[0])
        t, g, ih, il, off, fs, ms, cc = v
        ents.append((t, g, (ih << 32) | il, off, fs & 0x7FFFFFFF, ms, cc & 0xFFFF))
    return f, ents
def get(f, e):
    t, g, inst, off, fs, ms, comp = e
    f.seek(off); d = f.read(fs)
    if comp == 0x5A42: return zlib.decompress(d)
    if comp == 0: return d
    raise Exception('compression %x' % comp)
if __name__ == '__main__':
    out = sys.argv[1]; types = [int(x, 16) for x in sys.argv[2].split(',')]
    insts = set(int(x, 0) for x in sys.argv[3].split(','))
    pkgs = sys.argv[4:]
    found = {}
    for p in pkgs:  # first package wins (pass delta first)
        f, ents = read_index(p)
        for e in ents:
            if e[0] in types and e[2] in insts and (e[0], e[2]) not in found:
                found[(e[0], e[2])] = 1
                d = get(f, e)
                open(os.path.join(out, 'S4_%08X_%08X_%016X.bin' % (e[0], e[1], e[2])), 'wb').write(d)
                print(os.path.basename(p), '%08X %016X' % (e[0], e[2]), len(d))
