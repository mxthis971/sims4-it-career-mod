# -*- coding: utf-8 -*-
# Exécuté par build.py (exec) : partage ses variables (iid, S, add, LOOT, PREFIX, TRACK_*, COM_MISSIONS…)
from home import MISSIONS, FREELANCE

T_COMMODITY = 0x339BC5BD
SD_GROUP_COMMODITY = 0x009BC58E
CAT_CAREER = 37035          # PieMenuCategory computer_Career (menu « Carrière » de l'ordi)
PERF_SMALL = 27842          # loot +performance (petit)
HOME_SIS = []

def make_commodity(name, cid, max_value):
    x = ('<?xml version="1.0" encoding="utf-8"?>\n'
         '<I c="Commodity" i="statistic" m="statistics.commodity" n="%s_%s" s="%d">\n'
         '  <T n="_default_convergence_value">0</T>\n'
         '  <U n="arrow_data">\n    <T n="negative_double_arrow">-20</T>\n    <T n="negative_single_arrow">-1</T>\n'
         '    <T n="negative_triple_arrow">-30</T>\n    <T n="positive_double_arrow">20</T>\n    <T n="positive_single_arrow">1</T>\n'
         '    <T n="positive_triple_arrow">30</T>\n  </U>\n'
         '  <T n="auto_satisfy_curve_random_time_offset">120</T>\n  <T n="decay_rate">0</T>\n'
         '  <U n="initial_tuning">\n    <T n="_use_auto_satisfy_curve_as_initial_value">False</T>\n    <T n="_value">0</T>\n  </U>\n'
         '  <T n="max_value_tuning">%d</T>\n  <T n="maximum_auto_satisfy_time">1440</T>\n  <T n="min_value_tuning">0</T>\n'
         '  <T n="remove_on_convergence">False</T>\n'
         '  <L n="states">\n    <U />\n    <U>\n      <T n="value">%d</T>\n    </U>\n  </L>\n'
         '  <T n="ui_sort_order">0</T>\n  <U n="ui_visible_distress_threshold">\n    <T n="threshold_value">0</T>\n  </U>\n'
         '  <T n="weight">1</T>\n</I>') % (PREFIX, name, cid, max_value, max_value - 1)
    add(T_COMMODITY, 0, cid, x.encode('utf-8'))
    m = simdata_from('S4_545AC67A_009BC58E_000000000001A0F3.bin')
    m.tables[0]['name'] = '%s_%s' % (PREFIX, name)
    off, ty = sd.col(m, 0, 'max_value_tuning'); struct.pack_into('<f', m.tables[0]['data'], off, float(max_value))
    st = next(i for i, t in enumerate(m.tables) if t['schema'] is not None and t['rows'] == 2 and i != 0)
    off, ty = sd.col(m, st, 'value', 1); struct.pack_into('<i', m.tables[st]['data'], off, max_value - 1)
    add(T_SIMDATA, SD_GROUP_COMMODITY, cid, sd.save(m))

def money_loot(amount):
    key = '$%d' % amount
    if key not in LOOT:
        lid_ = iid('loot_money_%d' % amount)
        add(T_LOOT, 0, lid_, ('<?xml version="1.0" encoding="utf-8"?>\n<I c="LootActions" i="action" m="interactions.utils.loot" n="%s_loot_money_%d" s="%d">\n'
            '  <L n="loot_actions">\n    <V t="money_loot">\n      <U n="money_loot">\n        <V n="amount" t="literal">\n          <U n="literal">\n'
            '            <T n="value">%d</T>\n          </U>\n        </V>\n        <T n="display_to_user">True</T>\n      </U>\n    </V>\n  </L>\n</I>' % (PREFIX, amount, lid_, amount)).encode('utf-8'))
        LOOT[key] = lid_
    return LOOT[key]

def notif_loot(key, text, extra=''):
    lid_ = iid('loot_notif_' + key)
    add(T_LOOT, 0, lid_, (('<?xml version="1.0" encoding="utf-8"?>\n<I c="LootActions" i="action" m="interactions.utils.loot" n="%s_loot_notif_%s" s="%d">\n'
        '  <L n="loot_actions">\n    <V t="notification_and_dialog">\n      <U n="notification_and_dialog">\n        <V n="dialog" t="notification">\n          <U n="notification">\n'
        '            <V n="icon" t="enabled">\n              <V n="enabled" t="participant">\n                <U n="participant">\n                  <L n="participant_type">\n                    <E>Object</E>\n                  </L>\n                </U>\n              </V>\n            </V>\n'
        '            <V n="secondary_icon" t="enabled">\n              <V n="enabled" t="participant">\n                <U n="participant">\n                  <L n="participant_type">\n                    <E>Actor</E>\n                  </L>\n                </U>\n              </V>\n            </V>\n'
        '            <V n="text" t="single">\n              <T n="single">%s</T>\n            </V>\n          </U>\n        </V>\n      </U>\n    </V>\n%s  </L>\n</I>')
        % (PREFIX, key, lid_, S('notif_' + key, text), extra)).encode('utf-8'))
    return lid_

def reset_loot(key, stat):
    return ('    <V t="statistics">\n      <V n="statistics" t="statistic_set">\n        <U n="statistic_set">\n'
            '          <T n="stat">%d</T>\n          <T n="value">0</T>\n        </U>\n      </V>\n    </V>\n') % stat

def skill_test(skill, lvl, tooltip=None):
    tt = ('<V n="tooltip" t="enabled"><T n="enabled">%s</T></V>' % tooltip) if tooltip else ''
    return ('<V t="skill_test"><U n="skill_test"><T n="skill">%d</T><V n="skill_range" t="interval"><U n="interval">'
            '<U n="skill_interval"><T n="lower_bound">%d</T></U></U></V>%s</U></V>') % (SKILL_ID[skill], lvl, tt)

def outcome_xml(outs):
    # outs : [(loots, base_weight, [(skill, lvl, mult)])]
    r = ''
    for loots, w, mods in outs:
        r += '<U><U n="outcome"><L n="loot_list">' + ''.join('<T>%d</T>' % l for l in loots) + '</L></U><U n="weight"><T n="base_value">%s</T>' % w
        if mods:
            r += '<L n="multipliers">' + ''.join('<U><T n="multiplier">%s</T><L n="tests"><L>%s</L></L></U>' % (mult, skill_test(sk, lvl)) for sk, lvl, mult in mods) + '</L>'
        r += '</U></U>'
    return '<V n="outcome" t="test_based"><U n="test_based"><L n="fallback_outcomes">%s</L></U></V>' % r

def make_si(key, display, stat, exit_value, skill, tests, outs, tooltip_key, tooltip_text):
    sid = iid('si_' + key)
    x = ('<?xml version="1.0" encoding="utf-8"?>\n'
         '<I c="SuperInteraction" i="interaction" m="interactions.base.super_interaction" n="%(prefix)s_si_%(key)s" s="%(sid)d">'
         '<V n="_icon" t="participant"><U n="participant"><L n="participant_type"><E>Object</E></L></U></V>'
         '<L n="_static_commodities"><U><T n="static_commodity">27767</T></U></L>'
         '<L n="appropriateness_tags"><E>Appropriateness_Computer</E></L>'
         '<T n="attention_cost">0.75</T>'
         '<V n="basic_content" t="flexible_length"><U n="flexible_length"><L n="conditional_actions">'
         '<V t="list_reference"><T n="list_reference">40705</T></V>'
         '<V t="literal"><U n="literal"><L n="conditions"><V t="stat_based"><U n="stat_based"><T n="stat">%(stat)d</T>'
         '<U n="threshold"><T n="value">%(exit)d</T></U></U></V></L><E n="interaction_action">EXIT_NATURALLY</E>'
         '<E n="progress_bar_action">NO_ACTION</E></U></V>'
         '<V t="list_reference"><T n="list_reference">39200</T></V></L>'
         '<V n="content" t="staging_content"><U n="staging_content"><U n="content_set"><L n="affordance_links">'
         '<T>31661</T><T>31652</T><T>31650</T></L></U></U></V>'
         '<V n="periodic_stat_change" t="enabled"><U n="enabled"><L n="operations">'
         '<V t="dynamic_skill"><U n="dynamic_skill"><U n="skill_loot_data_override"><E n="effectiveness">StandardPeriodic</E>'
         '<T n="stat">%(skill)d</T></U></U></V>'
         '<V t="statistic_change"><U n="statistic_change"><T n="amount">1</T><T n="stat">%(stat)d</T></U></V>'
         '</L></U></V></U></V>'
         '<L n="basic_extras">'
         '<V t="state_change"><U n="state_change"><V n="new_value" t="single_value"><U n="single_value"><T n="new_value">96859</T></U></V>'
         '<V n="timing" t="immediately" /></U></V>'
         '<V t="state_change"><U n="state_change"><V n="new_value" t="single_value"><U n="single_value"><T n="new_value">15106</T></U></V>'
         '<V n="timing" t="at_end"><U n="at_end"><E n="criticality">OnCancelOrException</E></U></V></U></V>'
         '</L>'
         '<V n="canonical_animation" t="enabled"><U n="enabled"><T n="factory">31395</T></U></V>'
         '<T n="category">%(cat)d</T><T n="collapsible">True</T><V n="content_score" t="disabled" />'
         '<T n="disallow_as_mixer_target">True</T>'
         '<T n="display_name">%(name)s</T>'
         '<L n="interaction_category_tags"><E>Interaction_Computer</E><E>Interaction_Super</E><E>Interaction_All</E></L>'
         '%(outcome)s'
         '<V n="pie_menu_icon" t="enabled"><V n="enabled" t="resource_key"><U n="resource_key"><T n="key">2f7d0004:00000000:ecea5e28ef363c46</T></U></V></V>'
         '<T n="pie_menu_priority">9</T>'
         '<E n="scoring_priority">NORMAL</E>'
         '<U n="skill_loot_data"><E n="effectiveness">StandardPeriodic</E><V n="level_range" t="enabled"><U n="enabled">'
         '<T n="lower_bound">1</T><T n="upper_bound">10</T></U></V><T n="stat">%(skill)d</T></U>'
         '<T n="subaction_selection_weight">3</T>'
         '<V n="super_affordance_compatibility" t="reference"><T n="reference">77330</T></V>'
         '<E n="target_type">OBJECT</E>'
         '<L n="test_autonomous"><L><V t="appropriateness" /></L></L>'
         '<V n="test_disallow_while_running" t="enabled"><U n="enabled"><T n="test_self">True</T></U></V>'
         '<L n="test_globals">'
         '<V t="sim_info"><U n="sim_info"><V n="ages" t="specified"><L n="specified"><E>TEEN</E><E>YOUNGADULT</E><E>ADULT</E><E>ELDER</E></L></V>'
         '<E n="who">Actor</E></U></V>'
         '<V t="state"><U n="state"><E n="operator">NOTEQUAL</E><T n="value">15080</T></U></V>'
         '%(tests)s'
         '<V t="statistic"><U n="statistic"><T n="stat">%(stat)d</T><V n="threshold" t="value_threshold"><U n="value_threshold">'
         '<E n="comparison">LESS</E><T n="value">%(exit)d</T></U></V>'
         '<V n="tooltip" t="enabled"><T n="enabled">%(tt)s</T></V></U></V>'
         '</L>'
         '<T n="time_overhead">30</T>'
         '<V n="utility_info" t="enabled"><L n="enabled"><U><E n="key">POWER</E></U></L></V>'
         '</I>') % dict(prefix=PREFIX, key=key, sid=sid, stat=stat, exit=exit_value, skill=SKILL_ID[skill], cat=CAT_CAREER,
                        name=S('si_name_' + key, display), outcome=outcome_xml(outs), tests=''.join(tests),
                        tt=S(tooltip_key, tooltip_text))
    add(T_SI, 0, sid, x.encode('utf-8'))
    HOME_SIS.append(sid)
    return sid

# ---- 1) missions de carrière (remplissent la tâche quotidienne, 2 h par jour au total) ----
make_commodity('com_missions', COM_MISSIONS, 120)
_track_of = {'base': TRACK_BASE, **TRACK_IDS}
for track, key, name, skill, tip in MISSIONS:
    test = ('<V t="career_test"><U n="career_test"><V n="test_type" t="career_track"><U n="career_track">'
            '<T n="career_track">%d</T></U></V></U></V>') % _track_of[track]
    ok = notif_loot('m_%s_ok' % key, "{0.SimFirstName} a fini les missions du jour : « %s ».\n\nLe savais-tu ? %s" % (name, tip))
    top = notif_loot('m_%s_top' % key, "Excellent travail ! Le chef de {0.SimFirstName} est impressionné (performance en hausse).\n\nLe savais-tu ? %s" % tip)
    make_si('m_' + key, 'Mission : ' + name, COM_MISSIONS, 120, skill, [test],
            [([ok], 3, []), ([top, PERF_SMALL], 1, [(skill, 5, 2), (skill, 8, 2)])],
            'tt_missions_done', "Plus de mission pour aujourd'hui. Reviens après la prochaine journée de travail.")

# ---- 2) contrats freelance (pour tout Sim ado ou plus, payés à la fin) ----
_SKILL_FR = {'Prog': 'Programmation', 'Logic': 'Logique', 'Handi': 'Bricolage', 'Mischief': 'Malice', 'Charisma': 'Charisme', 'Writing': 'Écriture'}
for key, name, req, lvl, minutes, pay, pay_top, skill, text, tip, risky in FREELANCE:
    cid = iid('com_free_' + key)
    make_commodity('com_free_' + key, cid, minutes)
    tests = []
    if req:
        tests.append(skill_test(req, lvl, S('tt_free_req_%s' % key, "{0.SimFirstName} doit avoir %s niveau %d pour ce contrat." % (_SKILL_FR[req], lvl))))
    reset = reset_loot(key, cid)
    ok = notif_loot('f_%s_ok' % key, "Contrat terminé : %s\n\n{0.SimFirstName} est payé(e) %d §.\n\nLe savais-tu ? %s" % (text, pay, tip), reset)
    top = notif_loot('f_%s_top' % key, "Client ravi ! %s\n\nAvec le pourboire, {0.SimFirstName} touche %d §.\n\nLe savais-tu ? %s" % (text, pay_top, tip), reset)
    outs = [([ok, money_loot(pay)], 3, []), ([top, money_loot(pay_top)], 1, [(skill, 6, 2), (skill, 9, 2)])]
    if risky:
        fail = notif_loot('f_%s_fail' % key, "Aucune faille trouvée cette fois, donc pas de récompense.\n\nLe savais-tu ? %s Persévère, ta compétence a quand même progressé." % tip, reset)
        outs = [([ok, money_loot(pay)], 2, [('Mischief', 6, 1.5)]), ([top, money_loot(pay_top)], 1, [('Mischief', 8, 2)]), ([fail], 2, [])]
    make_si('f_' + key, 'Freelance : ' + name, cid, minutes, skill, tests, outs,
            'tt_free_busy', "Contrat déjà terminé.")
print('home SIs', len(HOME_SIS))
