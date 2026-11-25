# Génère le mod "Carrière Informatique" pour Les Sims 4 (1.121)
# Sortie : mathis_CarriereInformatique.package + mathis_CarriereInformatique.ts4script
import re, struct, zlib, os, zipfile, copy
import simdata as sd

OUT = os.path.join(os.path.dirname(__file__), 'out')
os.makedirs(OUT, exist_ok=True)
PREFIX = 'mathis_InfoIT'

T_CAREER, T_TRACK, T_LEVEL, T_ASP, T_SI, T_SIMDATA, T_STBL = 0x73996BEB, 0x48C75CE3, 0x2C70ADF8, 0x28B64675, 0xE882D22F, 0x545AC67A, 0x220557DA
SD_GROUP = {T_CAREER: 0x00996B98, T_TRACK: 0x00C75CAB, T_LEVEL: 0x0070ADD4, T_ASP: 0x00B6465D}

def fnv32(s):
    h = 0x811C9DC5
    for c in s.lower().encode(): h = ((h * 0x01000193) & 0xFFFFFFFF) ^ c
    return h
def fnv64(s):
    h = 0xCBF29CE484222325
    for c in s.lower().encode(): h = ((h * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF) ^ c
    return h
def iid(name):  # instance ID 32 bits (comme Mod Constructor : plus sûr)
    return fnv32(PREFIX + '_' + name)

# ---------------- textes ----------------
STR = {}
KEYTEXT = {}  # clé lisible -> texte FR (sert aux traductions)
def S(key, text):
    k = fnv32(PREFIX + '_str_' + key); STR[k] = text; KEYTEXT[key] = text; return '0x%08X' % k

# ---------------- objectifs (compétences) existants ----------------
OBJ = {
 'Prog': {2:27751,3:27752,4:27753,5:27754,6:27755,7:27756,8:27757,9:27758,10:27759},
 'Logic': {2:26603,3:26604,4:26606,5:26607,6:26608,7:204991,8:26611,9:204992,10:26613},
 'Charisma': {2:26463,3:26464,4:26465,5:26466,6:26467,7:26468,8:26470,9:202047,10:26472},
 'Handi': {2:109075,3:218428,4:109078,5:218429,6:109079,7:218430,8:218421,9:218431,10:218423},
 'Mischief': {2:27427,3:27428,4:27429,5:27430,6:27431,7:27432,8:27433,9:27434,10:27435},
 'Writing': {2:26592,3:26593,4:26594,5:26595,6:202027,7:26597,8:26598,9:26599,10:26600},
}

# ---------------- conception ----------------
# (titre, description, salaire/h, exigences pour la promotion suivante)
BASE = [
 ('Stagiaire Helpdesk', "Tu réponds au téléphone, tu redémarres des box et tu entends « ça marche pas » 40 fois par jour.", 30, []),
 ('Technicien support N1', "Tu crées des comptes, tu changes des mots de passe et tu installes des imprimantes récalcitrantes.", 38, [('Logic', 2)]),
 ('Technicien support N2', "Les tickets compliqués arrivent chez toi : postes qui plantent, VPN capricieux, mails perdus.", 47, [('Prog', 2), ('Logic', 3)]),
 ('Technicien systèmes et réseaux', "Tu brasses des câbles, tu configures des switchs et tu commences à comprendre le réseau de l'entreprise. Bientôt, il faudra choisir ta spécialité.", 60, [('Prog', 3), ('Logic', 4)]),
]
BRANCHES = [
 ('Admin', 'Administrateur réseau', "Serveurs, VLAN, pare-feu et sauvegardes : tu fais tourner l'infrastructure, jusqu'à devenir DSI.", [
   ('Administrateur systèmes junior', "Tu gères les serveurs Windows et Linux et tu surveilles que tout est vert.", 72, [('Prog', 4), ('Handi', 3)]),
   ('Administrateur réseau', "VLAN, routage, DHCP, DNS : le réseau, c'est toi.", 90, [('Prog', 5), ('Logic', 5), ('Handi', 4)]),
   ('Ingénieur réseau', "Tu conçois des réseaux multisites et tu mets en place la haute disponibilité.", 115, [('Prog', 6), ('Charisma', 3), ('Handi', 5)]),
   ('Architecte réseau', "Tu dessines l'infrastructure de demain : datacenter, cloud et redondance.", 150, [('Prog', 7), ('Logic', 7), ('Charisma', 4)]),
   ('Responsable infrastructure', "Tu diriges une équipe d'admins et tu gères le budget du matériel.", 200, [('Prog', 8), ('Charisma', 6), ('Logic', 8)]),
   ('DSI', "Directeur des systèmes d'information : toute l'informatique de l'entreprise est sous ta responsabilité.", 290, []),
 ]),
 ('Cyber', 'Cybersécurité', "Analyse des alertes, tests d'intrusion et gestion de crise : tu protèges l'entreprise des pirates, jusqu'à devenir RSSI.", [
   ('Analyste SOC N1', "Tu surveilles les alertes de sécurité et tu tries les vrais incidents des fausses alertes.", 75, [('Prog', 4), ('Mischief', 3)]),
   ('Analyste SOC N2', "Tu enquêtes sur les incidents : logs, malwares, comptes compromis.", 95, [('Prog', 5), ('Logic', 5), ('Mischief', 4)]),
   ('Pentester', "On te paie pour pirater l'entreprise (légalement) et trouver les failles avant les méchants.", 125, [('Prog', 7), ('Mischief', 6)]),
   ('Expert forensic', "Après une attaque, tu analyses les disques et la mémoire pour retrouver ce que le pirate a fait.", 165, [('Prog', 8), ('Logic', 7), ('Mischief', 7)]),
   ('Architecte sécurité', "Tu conçois la sécurité de tout le système d'information : segmentation, MFA, zero trust.", 220, [('Prog', 9), ('Charisma', 4), ('Logic', 8)]),
   ('RSSI', "Responsable de la sécurité des systèmes d'information : en cas de cyberattaque, c'est toi qu'on appelle.", 310, []),
 ]),
 ('Dev', 'Développement logiciel', "Du premier « Hello world » à la direction technique : tu crées des applications, jusqu'à devenir CTO.", [
   ('Développeur junior', "Tu corriges des bugs et tu écris tes premières fonctionnalités, encadré par les seniors.", 70, [('Prog', 4), ('Writing', 2)]),
   ('Développeur', "Tu développes des fonctionnalités complètes, de la base de données à l'interface.", 88, [('Prog', 5), ('Logic', 5)]),
   ('Développeur full-stack', "Front, back, API, base de données : tu touches à tout.", 112, [('Prog', 7), ('Writing', 4)]),
   ('Lead dev', "Tu encadres l'équipe, tu fais les revues de code et tu choisis les technos.", 145, [('Prog', 8), ('Logic', 7), ('Charisma', 3)]),
   ('Architecte logiciel', "Tu conçois l'architecture des applications : microservices, performances, sécurité.", 195, [('Prog', 9), ('Charisma', 5), ('Logic', 8)]),
   ('CTO', "Directeur technique : tu décides de la stratégie technique de toute l'entreprise.", 285, []),
 ]),
]
TPL_BASE = ['7EB5', '7EC0', '7EC1', '7EC2']
TPL_BRANCH = ['7EC3', '7EC4', '7EC9', '7ECA', '7ECB', '7ECC']

# ---------------- helpers XML ----------------
def tpl(name): return open(os.path.join('tpl', name), encoding='utf-8-sig').read()
def set_header(x, cls_n, inst):
    return re.sub(r'(<I [^>]*?) n="[^"]*" s="\d+">', lambda m: '%s n="%s" s="%d">' % (m.group(1), cls_n, inst), x, count=1)
def set_T(x, name, value):
    new, n = re.subn(r'<T n="%s">[^<]*(<!--.*?-->)?</T>' % name, '<T n="%s">%s</T>' % (name, value), x, count=1)
    assert n == 1, name; return new
def remove_block(x, tag, name):
    # supprime <tag n="name" ...> ... </tag> (gère l'imbrication)
    m = re.search(r'\n\s*<%s n="%s"[^>]*?(/>|>)' % (tag, name), x)
    if not m: return x
    if m.group(1) == '/>': return x[:m.start()] + x[m.end():]
    depth, i = 1, m.end()
    pat = re.compile(r'<(/?)%s\b[^>]*?(/?)>' % tag)
    while depth:
        mm = pat.search(x, i)
        if mm.group(1): depth -= 1
        elif not mm.group(2): depth += 1
        i = mm.end()
    return x[:m.start()] + x[i:]
def strip_comments(x): return re.sub(r'<!--.*?-->', '', x)

res = []   # (type, group, instance, bytes)
def add(t, g, i, data): res.append((t, g, i, data))

def simdata_from(ref, ):
    return sd.load(open(os.path.join('ref', ref), 'rb').read())
def sd_set(m, ti, colname, value, row=0):
    off, ty = sd.col(m, ti, colname, row); d = m.tables[ti]['data']
    if ty in (20, 7): struct.pack_into('<I', d, off, value)
    elif ty in (18, 9): struct.pack_into('<Q', d, off, value)
    elif ty == 6: struct.pack_into('<i', d, off, value)
    elif ty == 0: d[off] = 1 if value else 0
    else: raise Exception('type %d' % ty)
def sd_set_vector(m, ti, colname, values_table, start, count):
    off, ty = sd.col(m, ti, colname); assert ty == 14
    t = m.tables[ti]
    if count == 0:
        t['ptrs'].pop(off, None); struct.pack_into('<I', t['data'], off + 4, 0)
    else:
        t['ptrs'][off] = (values_table, start * 8); struct.pack_into('<I', t['data'], off + 4, count)
def sd_tableref_table(m, values):
    # remplace/crée la table de tableref (type 18) et retourne son index
    idx = next((i for i, t in enumerate(m.tables) if t['type'] == 18 and t['schema'] is None), None)
    if idx is None:
        m.tables.append(dict(name=None, type=18, rowsize=8, rows=0, schema=None, data=bytearray(), ptrs={}, strs={}, hash=0x811C9DC5)); idx = len(m.tables) - 1
    t = m.tables[idx]; t['rows'] = len(values); t['data'] = bytearray(b''.join(struct.pack('<Q', v) for v in values) + (b'' if values else b''))
    return idx

# ---------------- IDs ----------------
CAREER_ID = iid('career')
SI_ID = iid('si_career')
TRACK_BASE = iid('track_base')
TRACK_IDS = {b[0]: iid('track_' + b[0]) for b in BRANCHES}
COM_MISSIONS = iid('com_missions')  # tâche quotidienne « Missions à distance »

# ---------------- aspirations ----------------
def make_aspiration(name, reqs):
    if not reqs: return 0
    aid = iid('asp_' + name)
    objs = [OBJ[s][lvl] for s, lvl in reqs]
    x = tpl('aspiration.xml')
    x = set_header(x, PREFIX + '_asp_' + name, aid)
    x = re.sub(r'<L n="objectives">.*?</L>', '<L n="objectives">\n' + ''.join('    <T>%d</T>\n' % o for o in objs) + '  </L>', x, flags=re.S)
    add(T_ASP, 0, aid, strip_comments(x).encode('utf-8'))
    m = simdata_from('S4_545AC67A_00B6465D_000000000000801B.bin')
    m.tables[0]['name'] = PREFIX + '_asp_' + name
    vt = sd_tableref_table(m, objs); sd_set_vector(m, 0, 'objectives', vt, 0, len(objs))
    add(T_SIMDATA, SD_GROUP[T_ASP], aid, sd.save(m))
    return aid

# ---------------- niveaux ----------------
DAYS = ['0 SUNDAY', '1 MONDAY', '2 TUESDAY', '3 WEDNESDAY', '4 THURSDAY', '5 FRIDAY', '6 SATURDAY']
# Horaires : liste de créneaux (jours dim..sam, heure de début, durée en heures)
LV, MV, MJ, MaS = [0,1,1,1,1,1,0], [0,1,1,1,1,1,0], [0,1,1,1,1,0,0], [0,0,1,1,1,1,1]
def days(*names):
    idx = {'dim':0,'lun':1,'mar':2,'mer':3,'jeu':4,'ven':5,'sam':6}
    d = [0]*7
    for n in names: d[idx[n]] = 1
    return d
LUNVEN = days('lun','mar','mer','jeu','ven')
SCHED = {
 'base1': [(days('lun','mar','mer','jeu'), 9, 7)],                       # stage : 4 jours, 9h-16h
 'base2': [(LUNVEN, 8, 8)],                                              # 8h-16h
 'base3': [(LUNVEN, 8, 8)],
 'base4': [(LUNVEN, 8, 9)],                                              # 8h-17h
 'admin5': [(LUNVEN, 8, 8)],
 'admin6': [(LUNVEN, 7, 8)],                                             # 7h-15h (maintenance avant l'arrivée des utilisateurs)
 'admin7': [(days('lun','mar','mer','jeu'), 8, 9), (days('sam'), 9, 4)], # + astreinte samedi matin
 'admin8': [(LUNVEN, 9, 9)],                                             # 9h-18h
 'admin9': [(LUNVEN, 8, 10)],                                            # 8h-18h
 'admin10': [(LUNVEN, 9, 10)],                                           # DSI 9h-19h
 'cyber5': [(days('mar','mer','jeu','ven','sam'), 14, 8)],               # SOC équipe d'après-midi 14h-22h
 'cyber6': [(days('dim','lun','mar','mer'), 22, 8)],                     # SOC de nuit 22h-6h, 4 nuits
 'cyber7': [(days('lun','mar','mer','jeu'), 9, 9)],                      # pentester : 4 jours de 9h
 'cyber8': [(LUNVEN, 10, 8)],                                            # forensic 10h-18h
 'cyber9': [(LUNVEN, 9, 8)],
 'cyber10': [(LUNVEN, 8, 10)],                                           # RSSI 8h-18h
 'dev5': [(LUNVEN, 10, 8)],                                              # 10h-18h
 'dev6': [(days('lun','mar','jeu','ven'), 9, 9)],                        # mercredi libre
 'dev7': [(LUNVEN, 11, 8)],                                              # 11h-19h
 'dev8': [(LUNVEN, 9, 9)],
 'dev9': [(days('lun','mar','mer','jeu'), 9, 9)],
 'dev10': [(LUNVEN, 8, 11), (days('sam'), 10, 4)],                       # CTO : 8h-19h + samedi
}
MOOD = {'base': 14639, 'Admin': 14639, 'Cyber': 14636, 'Dev': 14641}  # Concentré / Plein d'énergie / Inspiré
def schedule_xml(entries):
    out = '  <U n="work_schedule">\n    <L n="schedule_entries">\n'
    for d, start, hours in entries:
        out += '      <U>\n        <U n="days_available">\n' + ''.join('          <T n="%s">%s</T>\n' % (DAYS[i], 'True' if d[i] else 'False') for i in range(7))
        out += '        </U>\n        <T n="duration">%d</T>\n        <U n="start_time">\n          <T n="hour">%d</T>\n        </U>\n      </U>\n' % (hours, start)
    return out + '    </L>\n  </U>\n'
def sd_schedule(m, entries):
    def find(name): return next(i for i, t in enumerate(m.tables) if t['schema'] is not None and m.schemas[t['schema']]['name'] == name)
    wk, en, dy, tm = find('TunableWeeklySchedule'), find('TunableScheduleEntry'), find('TunableAvailableDays'), find('TunableTimeOfDay')
    E, D, T = m.tables[en], m.tables[dy], m.tables[tm]
    n = len(entries)
    row_e, row_d, row_t = bytes(E['data'][:E['rowsize']]), bytes(D['data'][:D['rowsize']]), bytes(T['data'][:T['rowsize']])
    E['data'] = bytearray(row_e * n); D['data'] = bytearray(row_d * n); T['data'] = bytearray(row_t * n)
    E['rows'] = D['rows'] = T['rows'] = n
    off_days, _ = sd.col(m, en, 'days_available'); off_time, _ = sd.col(m, en, 'start_time'); off_dur, _ = sd.col(m, en, 'duration')
    E['ptrs'] = {}
    for i, (d, start, hours) in enumerate(entries):
        E['ptrs'][i * E['rowsize'] + off_days] = (dy, i * D['rowsize'])
        E['ptrs'][i * E['rowsize'] + off_time] = (tm, i * T['rowsize'])
        struct.pack_into('<f', E['data'], i * E['rowsize'] + off_dur, float(hours))
        D['data'][i * D['rowsize']:i * D['rowsize'] + 7] = bytes(d)
        struct.pack_into('<ii', T['data'], i * T['rowsize'], start, 0)
    off_v, _ = sd.col(m, wk, 'schedule_entries')
    m.tables[wk]['ptrs'][off_v] = (en, 0); struct.pack_into('<I', m.tables[wk]['data'], off_v + 4, n)
LEVEL_SD = {k: f for k, f in ((f[-8:-4], f) for f in os.listdir('ref') if f.startswith('S4_545AC67A_0070ADD4'))}
def make_level(name, tplkey, track, title, desc, pay, reqs):
    sched = SCHED[name]
    lid = iid('lvl_' + name)
    x = tpl('level_%s.xml' % tplkey)
    x = set_header(x, PREFIX + '_lvl_' + name, lid)
    tkey = S('title_' + name, title); dkey = S('desc_' + name, desc)
    x = set_T(x, 'title', tkey); x = set_T(x, 'title_description', dkey)
    x = re.sub(r'<T n="simoleons_per_hour">\d+</T>', '<T n="simoleons_per_hour">%d</T>' % pay, x, count=1)
    x = remove_block(x, 'V', 'fame_moment')
    x = remove_block(x, 'U', 'work_schedule')
    x = x.replace('</I>', schedule_xml(sched) + '</I>')
    x = set_T(x, 'ideal_mood', str(MOOD[track]))
    # tâche quotidienne : notre commodité « Missions à distance » remplace « Programmation » (réservée à Génie de la technologie)
    assert '>76237<' in x, name
    x = re.sub(r'(<T n="statistic">)76237(<!--[^>]*-->)?(</T>\s*<V n="tooltip_text" t="enabled">\s*<U n="enabled">\s*<T n="general_description">)0x[0-9A-Fa-f]+',
               lambda mm: mm.group(1) + str(COM_MISSIONS) + mm.group(3) + S('task_missions', ' Missions à distance ({0.String})'), x)
    assert '>76237<' not in x, name
    aid = make_aspiration(name, reqs)
    if '<T n="aspiration">' in x:
        x = set_T(x, 'aspiration', str(aid)) if aid else re.sub(r'\n\s*<T n="aspiration">[^\n]*', '', x, count=1)
    elif aid:
        x = x.replace('<L n="end_of_day_loot">', '<T n="aspiration">%d</T>\n  <L n="end_of_day_loot">' % aid, 1)
    add(T_LEVEL, 0, lid, strip_comments(x).encode('utf-8'))
    m = simdata_from(LEVEL_SD[tplkey])
    m.tables[0]['name'] = PREFIX + '_lvl_' + name
    sd_set(m, 0, 'title', int(tkey, 16)); sd_set(m, 0, 'title_description', int(dkey, 16))
    sd_set(m, 0, 'aspiration', aid)
    sd_set(m, 0, 'ideal_mood', MOOD[track])
    sd_schedule(m, sched)
    pay_t = next(i for i, t in enumerate(m.tables) if t['type'] == 6)
    struct.pack_into('<i', m.tables[pay_t]['data'], 0, pay)
    add(T_SIMDATA, SD_GROUP[T_LEVEL], lid, sd.save(m))
    return lid

# ---------------- pistes ----------------
def make_track(tid, sdname, tplname, refsd, name_key, desc_key, level_ids, branch_ids):
    x = tpl(tplname)
    x = set_header(x, sdname, tid)
    x = set_T(x, 'career_name', name_key); x = set_T(x, 'career_name_gender_neutral', name_key); x = set_T(x, 'career_description', desc_key)
    x = re.sub(r'<L n="career_levels">.*?</L>', '<L n="career_levels">\n' + ''.join('    <T>%d</T>\n' % l for l in level_ids) + '  </L>', x, flags=re.S)
    if branch_ids:
        x = re.sub(r'<L n="branches">.*?</L>', '<L n="branches">\n' + ''.join('    <T>%d</T>\n' % b for b in branch_ids) + '  </L>', x, flags=re.S)
    add(T_TRACK, 0, tid, strip_comments(x).encode('utf-8'))
    m = simdata_from(refsd)
    m.tables[0]['name'] = sdname
    sd_set(m, 0, 'career_name', int(name_key, 16)); sd_set(m, 0, 'career_name_gender_neutral', int(name_key, 16)); sd_set(m, 0, 'career_description', int(desc_key, 16))
    vt = sd_tableref_table(m, list(branch_ids) + list(level_ids))
    sd_set_vector(m, 0, 'branches', vt, 0, len(branch_ids))
    sd_set_vector(m, 0, 'career_levels', vt, len(branch_ids), len(level_ids))
    add(T_SIMDATA, SD_GROUP[T_TRACK], tid, sd.save(m))

career_name = S('career_name', 'Informatique')
base_levels = [make_level('base%d' % (i + 1), TPL_BASE[i], 'base', *BASE[i]) for i in range(4)]
for key, bname, bdesc, levels in BRANCHES:
    lids = [make_level('%s%d' % (key.lower(), i + 5), TPL_BRANCH[i], key, *levels[i]) for i in range(6)]
    make_track(TRACK_IDS[key], PREFIX + '_track_' + key, 'track_branch.xml', 'S4_545AC67A_00C75CAB_0000000000007EDD.bin',
               S('track_' + key, bname), S('trackdesc_' + key, bdesc), lids, [])
make_track(TRACK_BASE, PREFIX + '_track_base', 'track_base.xml', 'S4_545AC67A_00C75CAB_0000000000007EDB.bin',
           career_name, S('career_desc', "Du helpdesk au poste de direction : dépanne, configure, sécurise et code. Après le niveau 4, choisis ta voie : Administrateur réseau, Cybersécurité ou Développement logiciel."),
           base_levels, [TRACK_IDS[b[0]] for b in BRANCHES])

# ---------------- carrière ----------------
x = tpl('career.xml')
x = set_header(x, PREFIX + '_career', CAREER_ID)
x = x.replace('>27932<', '>%d<' % CAREER_ID)
x = set_T(x, 'career_affordance', str(SI_ID))
x = set_T(x, 'start_track', str(TRACK_BASE))
companies = ['NetSecure SAS', 'Datacenter Caraïbes', 'ByteForge Studio', 'CyberDéfense Antilles']
x = re.sub(r'<L n="company_names">.*?</L>', '<L n="company_names">\n' + ''.join('          <T>%s</T>\n' % S('company%d' % i, c) for i, c in enumerate(companies)) + '        </L>', x, flags=re.S)
add(T_CAREER, 0, CAREER_ID, strip_comments(x).encode('utf-8'))
m = simdata_from('S4_545AC67A_00996B98_0000000000006D1C.bin')
m.tables[0]['name'] = PREFIX + '_career'
sd_set(m, 0, 'start_track', TRACK_BASE)
add(T_SIMDATA, SD_GROUP[T_CAREER], CAREER_ID, sd.save(m))

# ---------------- situations au travail (cartes chance) ----------------
import xml.etree.ElementTree as ET
from cards import CARDS
from cards_extra import ADMIN, CYBER
CARDS = CARDS + ADMIN + CYBER
T_LOOT = 0x0C772E27
SKILL_ID = {'Prog': 16703, 'Logic': 16706, 'Charisma': 16699, 'Handi': 16704, 'Mischief': 16707, 'Writing': 16714}
PERF = {'P+S': 27842, 'P+M': 31826, 'P+L': 31837, 'P-S': 31865, 'P-M': 31864, 'P-L': 31875}
LOOT = dict(PERF)
for sk, sid in SKILL_ID.items():
    lid_ = iid('loot_skill_' + sk)
    add(T_LOOT, 0, lid_, ('<?xml version="1.0" encoding="utf-8"?>\n<I c="LootActions" i="action" m="interactions.utils.loot" n="%s_loot_skill_%s" s="%d">\n'
        '  <L n="loot_actions">\n    <V t="dynamic_skill_loot">\n      <U n="dynamic_skill_loot">\n        <U n="skill_loot_data_override">\n'
        '          <E n="effectiveness">Standard</E>\n          <V n="level_range" t="enabled">\n            <U n="enabled">\n'
        '              <T n="lower_bound">1</T>\n              <T n="upper_bound">10</T>\n            </U>\n          </V>\n'
        '          <T n="stat">%d</T>\n        </U>\n      </U>\n    </V>\n  </L>\n</I>' % (PREFIX, sk, lid_, sid)).encode('utf-8'))
    LOOT[sk] = lid_
for amount in (500, 1000, 2500):
    lid_ = iid('loot_money_%d' % amount)
    add(T_LOOT, 0, lid_, ('<?xml version="1.0" encoding="utf-8"?>\n<I c="LootActions" i="action" m="interactions.utils.loot" n="%s_loot_money_%d" s="%d">\n'
        '  <L n="loot_actions">\n    <V t="money_loot">\n      <U n="money_loot">\n        <V n="amount" t="literal">\n          <U n="literal">\n'
        '            <T n="value">%d</T>\n          </U>\n        </V>\n        <T n="display_to_user">True</T>\n      </U>\n    </V>\n  </L>\n</I>' % (PREFIX, amount, lid_, amount)).encode('utf-8'))
    LOOT['$%d' % amount] = lid_
ICON = '2f7d0004:00000000:7035c7fa615ef73b'
def _outcome(o, key):
    out = '<U>'
    if o['loot']: out += '<L n="loot_actions">' + ''.join('<T>%d</T>' % LOOT[l] for l in o['loot']) + '</L>'
    out += ('<V n="notification" t="enabled"><V n="enabled" t="literal"><U n="literal">'
            '<V n="icon" t="enabled"><V n="enabled" t="resource_key"><U n="resource_key"><T n="key">%s</T></U></V></V>'
            '<V n="secondary_icon" t="enabled"><V n="enabled" t="participant" /></V>'
            '<V n="text" t="single"><T n="single">%s</T></V></U></V></V>') % (ICON, S(key, o['txt']))
    mods = []
    if o['w'] != 1: mods.append('<U><T n="weight_multiplier">%s</T></U>' % o['w'])
    for sk, lvl, mult in o['mods']:
        mods.append('<U><V n="test" t="skill_test"><U n="skill_test"><T n="skill">%d</T><V n="skill_range" t="interval"><U n="interval">'
                    '<U n="skill_interval"><T n="lower_bound">%d</T></U></U></V><T n="use_effective_skill_level">True</T></U></V>'
                    '<T n="weight_multiplier">%s</T></U>' % (SKILL_ID[sk], lvl, mult))
    if mods: out += '<L n="weight_modifiers">' + ''.join(mods) + '</L>'
    return out + '</U>'
def build_adventure(si_xml):
    root = ET.fromstring(si_xml)
    adv = root.find("L[@n='basic_extras']/V[@t='adventure']/U[@n='adventure']")
    moms = adv.find("L[@n='_adventure_moments']")
    # On garde uniquement nos propres moments : on vide la liste puis on reconstruit le départ
    for u in list(moms): moms.remove(u)
    moms.append(ET.fromstring('<U><E n="key">Career_Starter</E><U n="value"><V n="aventure_moment" t="literal"><U n="literal">'
        '<L n="_finish_actions"><U><L n="action_results"><U /><U><L n="next_moments"><E>Career_ChooseCard</E></L>'
        '<L n="weight_modifiers"><U><T n="weight_multiplier">2</T></U></L></U></L></U></L></U></V></U></U>'))
    # Clés de l'enum AdventureMomentKey (n'importe quelle clé existante est réutilisable)
    _all = [k.strip() for k in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'advkeys.txt')) if k.strip()]
    _skip = {'Career_Starter', 'Career_ChooseCard', 'AdventureTest_Initial_Common'}
    KEYS = [k for k in _all if k.startswith('Career_') and k not in _skip] + [k for k in _all if not k.startswith('Career_') and k not in _skip]
    assert len(set(KEYS)) == len(KEYS) and len(CARDS) <= len(KEYS), (len(CARDS), len(KEYS))
    track_of = {'base': TRACK_BASE, **TRACK_IDS}
    choose = []
    for n, c in enumerate(CARDS, 1):
        key = KEYS[n - 1]
        fin = ''
        for j, (label, outcomes) in enumerate(c['options']):
            fin += ('<U><L n="action_results">' + ''.join(_outcome(o, 'card%d_opt%d_res%d' % (n, j, r)) for r, o in enumerate(outcomes)) +
                    '</L><V n="display_text" t="single"><T n="single">%s</T></V></U>') % S('card%d_opt%d' % (n, j), label)
        xml = ('<U><E n="key">%s</E><U n="value"><V n="aventure_moment" t="literal"><U n="literal"><L n="_finish_actions">%s</L>'
               '<V n="_visibility" t="show_dialog"><U n="show_dialog"><V n="text" t="single"><T n="single">%s</T></V>'
               '<V n="title" t="enabled"><T n="enabled">%s</T></V></U></V></U></V></U></U>') % (key, fin, S('card%d_text' % n, c['text']), S('card%d_title' % n, c['title']))
        moms.append(ET.fromstring(xml))
        if c['track'] == 'any':
            choose.append('<U><L n="next_moments"><E>%s</E></L></U>' % key)
        else:
            choose.append(('<U><L n="next_moments"><E>%s</E></L><L n="weight_modifiers"><U><V n="test" t="career_test"><U n="career_test">'
                       '<T n="negate">True</T><V n="test_type" t="career_track"><U n="career_track"><T n="career_track">%d</T></U></V>'
                       '</U></V><T n="weight_multiplier">0</T></U></L></U>') % (key, track_of[c['track']]))
    moms.append(ET.fromstring('<U><E n="key">Career_ChooseCard</E><U n="value"><V n="aventure_moment" t="literal"><U n="literal">'
                              '<L n="_finish_actions"><U><L n="action_results">' + ''.join(choose) + '</L></U></L></U></V></U></U>'))
    return '<?xml version="1.0" encoding="utf-8"?>\n' + ET.tostring(root, encoding='unicode')

# ---------------- interaction "aller au travail" ----------------
x = open('si_template.xml', encoding='utf-8-sig').read()
x = set_header(x, PREFIX + '_si_Career', SI_ID)
x = x.replace('>27932<', '>%d<' % CAREER_ID).replace('>32475<', '>%d<' % TRACK_BASE)
x = x.replace('>32476<', '>%d<' % TRACK_IDS['Admin']).replace('>32477<', '>%d<' % TRACK_IDS['Dev'])
x = build_adventure(strip_comments(x))
add(T_SI, 0, SI_ID, x.encode('utf-8'))

# ---------------- missions sur l'ordi + freelance ----------------
exec(open('build_home.py', encoding='utf-8').read())

# ---------------- STBL (FR + anglais en secours) ----------------
def stbl(strings):
    body = bytearray(); total = 0
    for k, v in strings.items():
        b = v.encode('utf-8'); body += struct.pack('<IBH', k, 0, len(b)) + b; total += len(b) + 1
    return b'STBL' + struct.pack('<HBQHI', 5, 0, len(strings), 0, total) + bytes(body)
stbl_inst = fnv64(PREFIX + '_stbl') & 0x00FFFFFFFFFFFFFF
import json
os.makedirs('i18n', exist_ok=True)
json.dump(KEYTEXT, open('i18n/fr.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
def _lang(code):
    p = os.path.join('i18n', code + '.json')
    tr = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
    missing = [k for k in KEYTEXT if k not in tr]
    if missing: print('i18n %s : %d textes manquants (FR utilisé)' % (code, len(missing)))
    for k, v in tr.items():
        if k in KEYTEXT:
            for tok in set(re.findall(r'\{[^}]*\}', KEYTEXT[k])):
                assert tok in v, (code, k, tok)
    return {fnv32(PREFIX + '_str_' + k): tr.get(k, KEYTEXT[k]) for k in KEYTEXT}
# 0x00 anglais (aussi la langue de secours), 0x07 français, 0x13 espagnol (codes lus dans Strings_*.package du jeu)
for lang, code in ((0x00, 'en'), (0x07, None), (0x13, 'es')):
    add(T_STBL, 0x80000000, (lang << 56) | stbl_inst, stbl(STR if code is None else _lang(code)))

# ---------------- DBPF ----------------
def dbpf(resources):
    data = bytearray(96); index = bytearray(struct.pack('<I', 0))
    for t, g, i, d in resources:
        c = zlib.compress(d, 9); off = len(data); data += c
        index += struct.pack('<IIIIIIIHH', t, g, i >> 32, i & 0xFFFFFFFF, off, len(c) | 0x80000000, len(d), 0x5A42, 1)
    ioff = len(data); data += index
    h = bytearray(96); h[0:4] = b'DBPF'
    struct.pack_into('<II', h, 4, 2, 1)
    struct.pack_into('<I', h, 36, len(resources)); struct.pack_into('<I', h, 44, len(index))
    struct.pack_into('<I', h, 60, 3); struct.pack_into('<I', h, 64, ioff)
    data[0:96] = h
    return bytes(data)
pkg = os.path.join(OUT, 'mathis_CarriereInformatique.package')
open(pkg, 'wb').write(dbpf(res))

# ---------------- script "À la fac" ----------------
script = open('ts4script_src/mathis_infoit_degree.py', encoding='utf-8').read()
script = script.replace('__TRACKS__', repr([TRACK_BASE] + [TRACK_IDS[b[0]] for b in BRANCHES]))
script = script.replace('__HOME_SIS__', repr(HOME_SIS))
zp = os.path.join(OUT, 'mathis_CarriereInformatique.ts4script')
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_STORED) as z:
    z.writestr('mathis_infoit_degree.py', script)

print('resources', len(res), 'strings', len(STR))
print('career', CAREER_ID, 'base track', TRACK_BASE, TRACK_IDS)
