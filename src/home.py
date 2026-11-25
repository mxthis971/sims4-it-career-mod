# -*- coding: utf-8 -*-
# Missions sur l'ordinateur de la maison (tâche quotidienne de la carrière) + contrats freelance.
# Données ici, génération du tuning dans build_home() (appelée par build.py).

# Missions de carrière : (piste, clé, nom, compétence, astuce "Le savais-tu ?")
MISSIONS = [
 ('base', 'tickets', "Traiter des tickets à distance", 'Logic',
  "Un bon ticket dit : qui, quoi, depuis quand, et ce qui a déjà été essayé. Ça fait gagner un temps fou."),
 ('base', 'certif', "Réviser une certification (Cisco, Microsoft…)", 'Prog',
  "Le modèle OSI a 7 couches : Physique, Liaison, Réseau, Transport, Session, Présentation, Application. Moyen mnémotechnique : « Pour Le Réseau, Tout Se Passe Automatiquement »."),
 ('Admin', 'vlan', "Configurer les VLAN d'un switch", 'Logic',
  "Un VLAN découpe un switch en plusieurs réseaux séparés. Le port relié au routeur est en mode « trunk » pour faire passer tous les VLAN."),
 ('Admin', 'backup', "Vérifier les sauvegardes de la nuit", 'Logic',
  "Une sauvegarde qu'on n'a jamais restaurée n'est pas une sauvegarde. On fait des tests de restauration régulièrement."),
 ('Admin', 'script', "Écrire un script d'automatisation (PowerShell)", 'Prog',
  "Si tu fais la même tâche plus de 3 fois, automatise-la. Exemple : créer 30 comptes utilisateurs depuis un fichier CSV."),
 ('Admin', 'schema', "Mettre à jour le schéma du réseau", 'Writing',
  "Une bonne documentation (schéma, plan d'adressage IP, mots de passe dans un coffre-fort) permet à un collègue de te remplacer pendant tes vacances."),
 ('Admin', 'supervision', "Surveiller les alertes de supervision", 'Logic',
  "Les outils de supervision (Zabbix, Nagios, Centreon) interrogent les équipements, souvent en SNMP, et préviennent avant que les utilisateurs se plaignent."),
 ('Cyber', 'logs', "Analyser des journaux de sécurité", 'Logic',
  "Un SIEM rassemble les journaux de tous les équipements et repère les comportements anormaux, comme 50 mots de passe faux en 1 minute."),
 ('Cyber', 'cve', "Faire de la veille sur les failles (CVE)", 'Prog',
  "Chaque faille connue a un numéro CVE et une note de gravité CVSS sur 10. Le CERT-FR publie des alertes en français."),
 ('Cyber', 'phishing', "Préparer un faux phishing de sensibilisation", 'Mischief',
  "Une campagne de faux phishing sert à entraîner les salariés, pas à les punir. On les forme juste après."),
 ('Cyber', 'lab', "S'entraîner sur un labo de pentest", 'Prog',
  "On ne teste que des machines qu'on a le droit d'attaquer : un labo perso ou un CTF. Attaquer sans autorisation est un délit."),
 ('Cyber', 'incident', "Rédiger une procédure de réponse à incident", 'Writing',
  "Les étapes d'une réponse à incident : détecter, contenir (isoler la machine), éradiquer, restaurer, puis tirer les leçons."),
 ('Dev', 'bugs', "Corriger des bugs", 'Prog',
  "Pour corriger un bug, on commence par le reproduire. Un bug qu'on ne sait pas reproduire est très dur à corriger."),
]

# Contrats freelance : (clé, nom, compétence requise, niveau, durée en minutes, paie, paie bonus, compétence travaillée, texte, astuce, risque)
# risque=True : le contrat peut échouer (pas de paie)
FREELANCE = [
 ('pc', "Dépanner le PC d'un particulier", None, 0, 120, 120, 180, 'Handi',
  "Le PC de Mme Michu ramait : 14 barres d'outils et un antivirus expiré.",
  "Avant de toucher à un PC, on sauvegarde les fichiers importants du client.", False),
 ('wifi', "Installer le Wi-Fi d'un commerce", 'Logic', 3, 180, 250, 375, 'Logic',
  "La boulangerie a maintenant un Wi-Fi pour la caisse et un Wi-Fi invité séparé.",
  "On sépare le Wi-Fi invité du réseau de l'entreprise, et on utilise WPA2 ou mieux WPA3.", False),
 ('site', "Créer le site web d'un artisan", 'Prog', 3, 240, 400, 600, 'Prog',
  "Le plombier du quartier a son site : HTML, CSS et un formulaire de contact.",
  "Un site moderne doit être en HTTPS (le cadenas) : les données sont chiffrées entre le visiteur et le serveur.", False),
 ('backup', "Mettre en place les sauvegardes d'un cabinet", 'Logic', 5, 180, 500, 750, 'Logic',
  "Le cabinet médical a des sauvegardes automatiques chaque nuit, dont une copie hors du bâtiment.",
  "Règle 3-2-1 : 3 copies, sur 2 supports différents, dont 1 hors du bâtiment.", False),
 ('reseau', "Configurer le réseau d'une PME", 'Logic', 6, 240, 750, 1100, 'Logic',
  "Switchs, VLAN, DHCP et pare-feu : la PME a un vrai réseau propre.",
  "Le DHCP distribue automatiquement les adresses IP. On réserve des IP fixes pour les serveurs et les imprimantes.", False),
 ('audit', "Faire l'audit de sécurité d'une PME", 'Prog', 6, 240, 900, 1350, 'Prog',
  "{0.SimFirstName} rend un rapport clair : 3 failles graves, 5 moyennes, et comment les corriger.",
  "Un audit se fait toujours avec un accord écrit du client, qui fixe ce qu'on a le droit de tester.", False),
 ('bounty', "Bug bounty : chercher une faille (légalement)", 'Prog', 8, 300, 2000, 3000, 'Mischief',
  "{0.SimFirstName} trouve une faille sur le site d'une grande entreprise et la signale proprement. Récompense versée !",
  "Le bug bounty, c'est être payé pour trouver des failles, dans les règles fixées par l'entreprise.", True),
]
