# Assemble tr_*.py -> en.json / es.json
import json, glob, importlib.util, os, re
here = os.path.dirname(os.path.abspath(__file__))
fr = json.load(open(os.path.join(here, 'fr.json'), encoding='utf-8'))
en, es = {}, {}
for p in sorted(glob.glob(os.path.join(here, 'tr_*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(p)[:-3], p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, (e, s) in m.T.items():
        assert k in fr, ('clé inconnue', p, k)
        en[k] = e; es[k] = s
missing = [k for k in fr if k not in en]
print('manquants:', len(missing), missing[:10])
for lang, d in (('en', en), ('es', es)):
    for k, v in d.items():
        for tok in set(re.findall(r'\{[^}]*\}', fr[k])):
            assert tok in v, (lang, k, tok)
        assert v.count('\n') == fr[k].count('\n'), (lang, k)
    json.dump({k: d[k] for k in fr if k in d}, open(os.path.join(here, lang + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('en', len(en), 'es', len(es))
