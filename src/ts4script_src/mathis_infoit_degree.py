# Script de la carrière Informatique (mathis_CarriereInformatique)
# 1) Compatibilité "À la fac"  2) missions et freelance sur les ordinateurs
# Ajoute les pistes de la carrière au diplôme Informatique (university_Major_ComputerScience).
# Effet : un Sim diplômé en Informatique entre plus haut dans la carrière, avec prime et bonus de salaire.
# Sans le pack "À la fac", le script ne fait rien.
import inspect
import services
from sims4.resources import Types
from sims4.tuning.instance_manager import InstanceManager

TRACKS = __TRACKS__
MAJOR_IDS = (219555,)  # university_Major_ComputerScience
_done = False

def _inject():
    global _done
    if _done:
        return
    major_mgr = services.get_instance_manager(Types.UNIVERSITY_MAJOR)
    track_mgr = services.get_instance_manager(Types.CAREER_TRACK)
    if major_mgr is None or track_mgr is None:
        return
    tracks = [track_mgr.get(t) for t in TRACKS]
    if any(t is None for t in tracks):
        return
    for major_id in MAJOR_IDS:
        major = major_mgr.get(major_id)
        if major is None:
            continue
        existing = tuple(major.career_tracks)
        major.career_tracks = existing + tuple(t for t in tracks if t not in existing)
    _done = True

# Missions sur l'ordi + freelance : on ajoute nos interactions à tous les ordinateurs.
# Un objet est un ordinateur s'il propose déjà « Remplir des rapports » (108475), comme tous les PC du jeu et des packs.
HOME_SIS = __HOME_SIS__
COMPUTER_MARKER = 108475
_home_done = False

def _inject_home():
    global _home_done
    if _home_done:
        return
    aff_mgr = services.get_instance_manager(Types.INTERACTION)
    obj_mgr = services.get_instance_manager(Types.OBJECT)
    if aff_mgr is None or obj_mgr is None:
        return
    sis = tuple(a for a in (aff_mgr.get(i) for i in HOME_SIS) if a is not None)
    if not sis:
        return
    found = 0
    for obj in tuple(obj_mgr.types.values()):
        sa = getattr(obj, '_super_affordances', None)
        if not sa:
            continue
        if any(getattr(a, 'guid64', None) == COMPUTER_MARKER for a in sa):
            obj._super_affordances = tuple(sa) + tuple(a for a in sis if a not in sa)
            found += 1
    if found:
        _home_done = True

def _safe_inject():
    try:
        _inject()
    except Exception:
        pass
    try:
        _inject_home()
    except Exception:
        pass

_original = InstanceManager.load_data_into_class_instances

def _patched(self, *args, **kwargs):
    result = _original(self, *args, **kwargs)
    if inspect.isgenerator(result):
        def _gen():
            value = yield from result
            _safe_inject()
            return value
        return _gen()
    _safe_inject()
    return result

InstanceManager.load_data_into_class_instances = _patched

# Filet de sécurité : on réessaie au chargement d'un foyer
try:
    from zone import Zone
    _original_zone = Zone.on_loading_screen_animation_finished
    def _zone_patched(self, *args, **kwargs):
        _safe_inject()
        return _original_zone(self, *args, **kwargs)
    Zone.on_loading_screen_animation_finished = _zone_patched
except Exception:
    pass
