# Situations au travail ("cartes chance") – carrière Informatique
# Chaque option a une liste de résultats possibles, tirés au hasard selon leur poids.
# mods = [(compétence, niveau minimum, multiplicateur)] : si le Sim a la compétence, ce résultat devient plus probable.
# loot : P+S/P+M/P+L = performance +petite/moyenne/grande ; P-S/P-M/P-L = perte ; Prog/Logic/... = gain de compétence ; $500 = argent
# Chaque résultat se termine par une notion du BTS SIO ("Le savais-tu ?").

def O(txt, loot=(), w=1, mods=()):
    return dict(txt=txt, loot=list(loot), w=w, mods=list(mods))

CARDS = [
# ======================= TRONC COMMUN (niveaux 1 à 4) =======================
dict(track='base', title="« Internet ne marche plus ! »",
 text="Un utilisateur appelle, paniqué : plus rien ne s'affiche sur son navigateur. Que fait {0.SimFirstName} ?",
 options=[
  ("Lui faire redémarrer la box", [
    O("C'était bien ça : tout remarche en 2 minutes.\n\nLe savais-tu ? Redémarrer règle beaucoup de pannes, mais c'est seulement la première étape du dépannage.", ['P+S'], 2, [('Logic', 2, 2)]),
    O("Toujours rien… {0.SimFirstName} a perdu 20 minutes au téléphone.\n\nLe savais-tu ? Le modèle OSI aide à chercher méthodiquement : on vérifie d'abord le câble (couche 1), puis l'adresse IP (couche 3).", ['P-S'])]),
  ("Aller vérifier sur place", [
    O("Le câble réseau était débranché sous le bureau ! L'utilisateur est ravi.\n\nLe savais-tu ? La couche 1 du modèle OSI, c'est la couche physique : câbles, prises, cartes réseau.", ['P+M', 'Handi'], 2, [('Handi', 2, 2)]),
    O("Le temps de traverser le bâtiment, trois nouveaux tickets sont arrivés.\n\nLe savais-tu ? Dans un helpdesk, on priorise les tickets selon l'urgence et l'impact (souvent avec l'outil GLPI).", ['P-S'])]),
 ]),
dict(track='base', title="L'imprimante maudite",
 text="L'imprimante du 2e étage affiche « Bourrage papier »… alors qu'il n'y a pas de papier dedans.",
 options=[
  ("La démonter entièrement", [
    O("Un trombone était coincé au fond ! L'imprimante repart.\n\nLe savais-tu ? On note chaque intervention dans le ticket : la prochaine fois, un collègue saura quoi faire.", ['P+M', 'Handi'], 1, [('Handi', 3, 3)]),
    O("Il reste une pièce dans la main de {0.SimFirstName}… et l'imprimante ne s'allume plus.\n\nLe savais-tu ? Quand un matériel est sous garantie, il vaut mieux contacter le fournisseur que démonter.", ['P-M'])]),
  ("Coller un post-it « En panne »", [
    O("Personne n'a rien remarqué. Ouf.\n\nLe savais-tu ? Un incident non traité finit souvent par revenir plus grave.", [], 1),
    O("Le directeur voulait justement imprimer son rapport. Il n'est pas content.\n\nLe savais-tu ? La qualité de service (SLA) fixe en combien de temps une panne doit être réglée.", ['P-S'], 1)]),
 ]),
dict(track='base', title="Le directeur pressé",
 text="Quelqu'un qui dit être le directeur appelle : il a oublié son mot de passe et exige qu'on le lui change « tout de suite, c'est moi le patron ! ».",
 options=[
  ("Vérifier son identité avant", [
    O("C'était bien lui. Il râle un peu, mais le responsable sécurité félicite {0.SimFirstName}.\n\nLe savais-tu ? On vérifie toujours l'identité avant une réinitialisation : c'est la règle contre l'ingénierie sociale.", ['P+M', 'Logic'], 3),
    O("Le directeur est vexé d'avoir attendu 5 minutes.\n\nLe savais-tu ? Même un patron doit suivre la procédure : la sécurité passe avant le confort.", ['P-S'], 1, [('Charisma', 3, 0.3)])]),
  ("Le réinitialiser directement", [
    O("Il est content et raccroche.\n\nLe savais-tu ? Tu as eu de la chance : c'est exactement comme ça que les pirates piègent les helpdesks.", ['P+S'], 1),
    O("C'était un pirate qui se faisait passer pour le directeur ! {0.SimFirstName} doit suivre une formation anti-arnaque.\n\nLe savais-tu ? Cette attaque s'appelle l'ingénierie sociale : on pirate l'humain au lieu de l'ordinateur.", ['P-L'], 1)]),
 ]),
dict(track='base', title="Café sur le portable",
 text="Un collègue a renversé son café sur son ordinateur portable. Il fume légèrement…",
 options=[
  ("Débrancher, démonter et sécher", [
    O("{0.SimFirstName} sauve l'ordinateur ! Il redémarre après séchage.\n\nLe savais-tu ? Première règle : couper l'alimentation et retirer la batterie pour éviter le court-circuit.", ['P+M', 'Handi'], 1, [('Handi', 3, 3)]),
    O("Trop tard, la carte mère est grillée.\n\nLe savais-tu ? Le matériel se remplace, les données non : c'est pour ça qu'on fait des sauvegardes.", ['P-S'])]),
  ("Restaurer ses fichiers depuis la sauvegarde", [
    O("Grâce à la sauvegarde d'hier soir, il ne perd rien. Il te remercie !\n\nLe savais-tu ? Règle 3-2-1 : 3 copies, sur 2 supports différents, dont 1 hors du bâtiment.", ['P+M', 'Logic'], 1, [('Logic', 3, 3)]),
    O("Il n'y avait aucune sauvegarde… il perd son rapport de 80 pages.\n\nLe savais-tu ? Une sauvegarde qu'on n'a jamais testée n'est pas une vraie sauvegarde.", ['P-M'])]),
 ]),
dict(track='base', title="50 postes à configurer",
 text="{0.SimFirstName} doit faire la même manipulation sur 50 ordinateurs. Et si on écrivait un petit script ?",
 options=[
  ("Écrire un script PowerShell", [
    O("Le script fait les 50 postes en 10 minutes. Le chef est bluffé !\n\nLe savais-tu ? Automatiser les tâches répétitives fait gagner du temps et évite les erreurs humaines.", ['P+L', 'Prog'], 1, [('Prog', 3, 3)]),
    O("Le script a renommé tous les postes en « test »… {0.SimFirstName} apprend à la dure.\n\nLe savais-tu ? On teste toujours un script sur 1 seul poste avant de le lancer partout.", ['P-S', 'Prog'])]),
  ("Tout faire à la main", [
    O("C'est long, mais sans surprise.\n\nLe savais-tu ? Les outils de déploiement comme les GPO sous Windows Server servent justement à éviter ça.", ['P+S'])]),
 ]),
dict(track='base', title="La certification",
 text="L'entreprise propose de payer à {0.SimFirstName} une certification (CCNA, Security+…). Il faudra réviser le soir.",
 options=[
  ("Réviser et passer l'examen", [
    O("Certifié ! Le CV de {0.SimFirstName} prend de la valeur.\n\nLe savais-tu ? Le CCNA de Cisco est très demandé pour les métiers du réseau, et il se prépare avec Packet Tracer.", ['P+L', 'Logic', 'Prog'], 1, [('Logic', 4, 3)]),
    O("Raté de peu. {0.SimFirstName} le repassera.\n\nLe savais-tu ? Les labos pratiques (Packet Tracer, VM) valent mieux que lire la théorie par cœur.", ['Logic'])]),
  ("Refuser, pas le temps", [
    O("Le chef note que {0.SimFirstName} n'est pas très motivé.\n\nLe savais-tu ? En informatique, on se forme toute sa vie : les technologies changent vite.", ['P-S'])]),
 ]),
dict(track='base', title="La clé USB mystère",
 text="{0.SimFirstName} trouve une clé USB étiquetée « Salaires 2026 » sur le parking.",
 options=[
  ("La brancher pour voir", [
    O("C'était un piège : la clé contenait un virus et le réseau est bloqué pendant une heure !\n\nLe savais-tu ? Les clés USB abandonnées sont un piège classique des pirates (l'attaque « USB drop »).", ['P-L', 'Mischief'], 2),
    O("Elle contenait… des photos de vacances. Ouf.\n\nLe savais-tu ? Tu as eu de la chance : on ne branche jamais une clé inconnue.", ['Mischief'], 1)]),
  ("La donner à l'équipe sécurité", [
    O("Bon réflexe ! C'était un test organisé par la direction. {0.SimFirstName} est cité en exemple.\n\nLe savais-tu ? La sensibilisation des utilisateurs est une des meilleures protections contre les attaques.", ['P+M'])]),
 ]),

# ======================= ADMINISTRATEUR RÉSEAU =======================
dict(track='Admin', title="Le serveur ne répond plus",
 text="Le serveur de fichiers ne répond plus : toute l'entreprise est bloquée et le téléphone de {0.SimFirstName} n'arrête pas de sonner.",
 options=[
  ("Redémarrer le serveur tout de suite", [
    O("Il redémarre et tout remarche… pour aujourd'hui.\n\nLe savais-tu ? Si on ne cherche pas la cause, la panne revient. C'est la différence entre un incident et un problème (ITIL).", ['P+S'], 2),
    O("Le disque était en train de mourir : après le redémarrage, le serveur ne revient plus !\n\nLe savais-tu ? Avant de redémarrer, on regarde les journaux (logs) pour comprendre ce qui se passe.", ['P-M'], 1)]),
  ("Lire les logs avant d'agir", [
    O("{0.SimFirstName} trouve un disque défaillant dans le RAID et le remplace sans couper le serveur !\n\nLe savais-tu ? Le RAID 1 copie les données sur 2 disques : si l'un casse, l'autre prend le relais.", ['P+L', 'Logic'], 1, [('Logic', 4, 3)]),
    O("L'analyse prend trop de temps, les utilisateurs s'impatientent.\n\nLe savais-tu ? Un outil de supervision (comme Zabbix ou Nagios) prévient avant que la panne arrive.", ['P-S', 'Logic'])]),
 ]),
dict(track='Admin', title="Mise à jour du vendredi",
 text="Il est 16h, un vendredi. Une mise à jour importante doit être installée sur le serveur de messagerie.",
 options=[
  ("L'installer maintenant", [
    O("La mise à jour fait planter la messagerie. {0.SimFirstName} reste tard pour réparer.\n\nLe savais-tu ? On évite les changements le vendredi soir : s'il y a un problème, personne n'est là pour le régler.", ['P-L'], 1),
    O("Tout s'est bien passé, cette fois.\n\nLe savais-tu ? Une bonne pratique est de tester les mises à jour sur un serveur de test d'abord.", ['P+S'], 1)]),
  ("La planifier lundi avec un plan B", [
    O("Lundi matin, tout se passe bien, et le plan de retour arrière était prêt.\n\nLe savais-tu ? Avant un changement, on prévoit toujours comment revenir en arrière (snapshot de VM, sauvegarde).", ['P+M', 'Logic'], 3),
    O("Le chef trouve que {0.SimFirstName} a été trop prudent.\n\nLe savais-tu ? Quand une faille est critique, il faut parfois corriger en urgence.", [], 1)]),
 ]),
dict(track='Admin', title="Le plat de spaghettis",
 text="La baie de brassage ressemble à un plat de spaghettis : des câbles partout, sans étiquette.",
 options=[
  ("Tout recâbler et étiqueter", [
    O("Résultat impeccable ! Chaque câble est repéré.\n\nLe savais-tu ? Une baie bien rangée avec des étiquettes fait gagner un temps fou lors des pannes.", ['P+L', 'Handi'], 1, [('Handi', 4, 3)]),
    O("{0.SimFirstName} a débranché le mauvais câble : le service compta est coupé du réseau !\n\nLe savais-tu ? On prévient les utilisateurs et on intervient en dehors des heures de travail.", ['P-M', 'Handi'])]),
  ("Laisser comme ça, ça marche", [
    O("Le jour où il faut trouver un câble, personne ne s'y retrouve.\n\nLe savais-tu ? La documentation réseau (schéma, plan d'adressage) fait partie du travail d'un admin.", ['P-S'])]),
 ]),
dict(track='Admin', title="Test surprise des sauvegardes",
 text="La direction veut vérifier que les sauvegardes fonctionnent vraiment.",
 options=[
  ("Faire une vraie restauration de test", [
    O("La restauration fonctionne parfaitement. La direction est rassurée.\n\nLe savais-tu ? Tester régulièrement la restauration est le seul moyen d'être sûr que les sauvegardes marchent.", ['P+L', 'Logic'], 1, [('Logic', 5, 3)]),
    O("La restauration échoue : la sauvegarde était vide depuis 3 mois ! Heureusement, on l'a vu à temps.\n\nLe savais-tu ? C'est pour ça qu'on teste : mieux vaut le découvrir maintenant que le jour d'une vraie panne.", ['P-S', 'Logic'])]),
  ("Montrer le tableau de bord tout vert", [
    O("La direction est satisfaite.\n\nLe savais-tu ? Un voyant vert ne prouve pas que les données sont restaurables.", ['P+S'], 1),
    O("Un auditeur demande une restauration… et elle échoue. Gros malaise.\n\nLe savais-tu ? Une sauvegarde qu'on n'a jamais testée n'est pas une vraie sauvegarde.", ['P-M'], 1)]),
 ]),
dict(track='Admin', title="Le Wi-Fi des visiteurs",
 text="Le service marketing veut que les visiteurs sur le Wi-Fi invité puissent accéder au serveur de fichiers « pour les présentations ».",
 options=[
  ("Refuser et créer un VLAN invité isolé", [
    O("Le réseau est séparé proprement : les invités ont Internet, mais pas les données de l'entreprise.\n\nLe savais-tu ? Un VLAN, c'est un réseau virtuel : sur le même switch, on crée des réseaux qui ne se voient pas.", ['P+M', 'Prog'], 1, [('Prog', 4, 3)]),
    O("Le marketing se plaint à la direction, qui demande des explications.\n\nLe savais-tu ? Savoir expliquer simplement un choix technique aux non-informaticiens, c'est une compétence clé.", ['P-S'])]),
  ("Ouvrir l'accès, c'est plus simple", [
    O("Les présentations marchent.\n\nLe savais-tu ? Tu as pris un gros risque : n'importe quel visiteur pouvait voir les fichiers.", ['P+S'], 1),
    O("Un visiteur a pu ouvrir les dossiers des ressources humaines…\n\nLe savais-tu ? On sépare toujours le réseau invité du réseau interne (VLAN + règles de pare-feu).", ['P-L'], 1)]),
 ]),
dict(track='Admin', title="Le budget des switchs",
 text="{0.SimFirstName} doit convaincre la direction d'acheter de nouveaux switchs : les anciens ont 12 ans.",
 options=[
  ("Présenter un dossier chiffré", [
    O("Budget accepté ! La direction félicite {0.SimFirstName} et lui verse une prime.\n\nLe savais-tu ? Un matériel en fin de vie n'a plus de mises à jour de sécurité : c'est un argument fort.", ['P+L', 'Charisma', '$1000'], 1, [('Charisma', 4, 3)]),
    O("Refusé, mais la direction a apprécié la présentation.\n\nLe savais-tu ? Un bon dossier compare le coût d'achat au coût d'une panne.", ['Charisma'])]),
  ("Envoyer un simple mail", [
    O("Budget refusé. Les vieux switchs vont devoir tenir encore un an.\n\nLe savais-tu ? Pour convaincre, il faut des chiffres : coût, risque, bénéfice.", ['P-S'])]),
 ]),
dict(track='Admin', title="Astreinte : le VPN est tombé",
 text="Le téléphone d'astreinte sonne pendant la pause déjeuner : le VPN ne marche plus et les commerciaux en déplacement sont bloqués.",
 options=[
  ("Laisser le repas et intervenir", [
    O("Le VPN est rétabli en 15 minutes. Les commerciaux adorent {0.SimFirstName}.\n\nLe savais-tu ? Un VPN crée un tunnel chiffré pour accéder au réseau de l'entreprise depuis l'extérieur.", ['P+M', 'Logic'], 1)]),
  ("Finir le sandwich d'abord", [
    O("Le VPN est revenu tout seul. Chanceux !\n\nLe savais-tu ? L'astreinte, c'est être joignable en dehors des heures, et c'est payé en plus.", [], 1),
    O("Une grosse vente a été perdue pendant la coupure.\n\nLe savais-tu ? Le temps de réponse en astreinte est souvent écrit dans le contrat (SLA).", ['P-M'], 1)]),
 ]),

# ======================= CYBERSÉCURITÉ =======================
dict(track='Cyber', title="Alerte phishing !",
 text="Un collègue a cliqué sur un lien dans un mail « Votre colis est bloqué, payez 1,99 € ».",
 options=[
  ("Isoler son PC du réseau immédiatement", [
    O("Bien joué : le virus n'a pas eu le temps de se propager !\n\nLe savais-tu ? Le premier réflexe en cas d'infection est d'isoler la machine pour protéger le reste du réseau.", ['P+L', 'Logic'])]),
  ("Lui dire de redémarrer et oublier", [
    O("C'était un ransomware. Trois serveurs sont chiffrés…\n\nLe savais-tu ? Un ransomware chiffre les fichiers et demande une rançon. On ne paie pas : on restaure les sauvegardes.", ['P-L'], 2),
    O("Fausse alerte : c'était un vrai lien de livraison.\n\nLe savais-tu ? Dans le doute, on signale toujours. Un faux positif ne coûte rien.", ['P+S'], 1)]),
 ]),
dict(track='Cyber', title="500 alertes au SOC",
 text="Le tableau de bord du SOC affiche 500 alertes. La plupart sont sûrement des fausses alertes.",
 options=[
  ("Les analyser une par une", [
    O("{0.SimFirstName} trouve la vraie : un compte admin se connecte depuis l'autre bout du monde !\n\nLe savais-tu ? Un SOC (centre de sécurité) surveille le réseau 24h/24 avec un outil appelé SIEM.", ['P+M', 'Logic'], 1, [('Logic', 5, 3)]),
    O("Trop d'alertes, {0.SimFirstName} n'a pas le temps de tout voir.\n\nLe savais-tu ? Trop d'alertes inutiles, ça s'appelle la « fatigue d'alerte » : les analystes finissent par rater les vraies.", ['P-S'])]),
  ("Créer une règle pour filtrer le bruit", [
    O("La règle élimine 490 fausses alertes. Il ne reste que les vraies !\n\nLe savais-tu ? Ajuster les règles de détection pour réduire les faux positifs fait partie du travail d'analyste.", ['P+L', 'Prog'], 1, [('Prog', 5, 3)]),
    O("La règle a aussi caché la vraie attaque…\n\nLe savais-tu ? Un filtre trop large crée des faux négatifs : des attaques réelles qu'on ne voit plus.", ['P-M', 'Prog'])]),
 ]),
dict(track='Cyber', title="Mission : entrer sans badge",
 text="Test d'intrusion physique : {0.SimFirstName} doit entrer dans le bâtiment d'un client sans badge (avec son autorisation écrite, bien sûr).",
 options=[
  ("Se déguiser en livreur de pizza", [
    O("Personne ne l'a arrêté ! Le rapport fait trembler le client.\n\nLe savais-tu ? Un pentest se fait toujours avec une autorisation écrite. Sans elle, c'est illégal.", ['P+L', 'Mischief'], 1, [('Mischief', 4, 3)]),
    O("L'accueil a démasqué {0.SimFirstName}. C'est aussi un bon résultat pour le client !\n\nLe savais-tu ? Un test qui échoue montre que la sécurité du client fonctionne.", ['P+S', 'Mischief'])]),
  ("Tester le Wi-Fi depuis le parking", [
    O("Le Wi-Fi utilisait un vieux chiffrement : {0.SimFirstName} entre dans le réseau en 10 minutes.\n\nLe savais-tu ? Le chiffrement WEP est cassé depuis longtemps. Aujourd'hui, on utilise WPA2 ou WPA3.", ['P+M', 'Prog'], 1, [('Prog', 5, 3)]),
    O("Le Wi-Fi est bien protégé. Rien à signaler.\n\nLe savais-tu ? Un mot de passe Wi-Fi long et complexe rend les attaques presque impossibles.", ['P+S'])]),
 ]),
dict(track='Cyber', title="Une faille chez le voisin",
 text="Pendant ses recherches, {0.SimFirstName} découvre une grosse faille sur le site d'une autre entreprise.",
 options=[
  ("La signaler discrètement à l'entreprise", [
    O("L'entreprise corrige la faille et remercie publiquement {0.SimFirstName}.\n\nLe savais-tu ? Prévenir l'entreprise sans exploiter la faille, ça s'appelle la divulgation responsable.", ['P+M', 'Charisma'])]),
  ("En parler à sa direction pour l'exploiter", [
    O("La direction est horrifiée : exploiter une faille sans autorisation est illégal ! Avertissement officiel.\n\nLe savais-tu ? En France, entrer dans un système sans autorisation est puni par la loi (article 323-1 du Code pénal).", ['P-L', 'Mischief'], 2),
    O("La direction fait semblant de ne pas avoir entendu…\n\nLe savais-tu ? L'éthique est essentielle en cybersécurité : on protège, on n'attaque pas.", ['P-S', 'Mischief'], 1)]),
 ]),
dict(track='Cyber', title="Serveur piraté cette nuit",
 text="Un serveur a été piraté pendant la nuit. Il faut comprendre comment le pirate est entré.",
 options=[
  ("Copier le disque et analyser la copie", [
    O("L'analyse montre que le pirate est passé par un logiciel pas à jour. Rapport parfait !\n\nLe savais-tu ? En investigation (forensic), on travaille sur une copie pour ne pas abîmer les preuves.", ['P+L', 'Logic'], 1, [('Logic', 5, 3)]),
    O("L'analyse est longue et ne donne rien de clair.\n\nLe savais-tu ? Les journaux (logs) centralisés aident beaucoup à retrouver ce qu'a fait un pirate.", ['P-S', 'Logic'])]),
  ("Analyser directement sur le serveur", [
    O("{0.SimFirstName} a effacé des traces importantes : les preuves ne sont plus utilisables.\n\nLe savais-tu ? Toucher à la machine d'origine modifie les preuves. On commence toujours par une copie.", ['P-M'], 1),
    O("Trouvé vite, mais c'était risqué.\n\nLe savais-tu ? En forensic, la méthode compte autant que le résultat.", ['P+S'], 1)]),
 ]),
dict(track='Cyber', title="Le mot de passe « admin123 »",
 text="{0.SimFirstName} découvre que le mot de passe du serveur principal est… « admin123 ».",
 options=[
  ("Imposer des mots de passe forts et la double authentification", [
    O("Malgré les râleurs, tout le monde a activé la double authentification.\n\nLe savais-tu ? Avec la MFA (double authentification), un mot de passe volé ne suffit plus à se connecter.", ['P+L', 'Charisma'], 1, [('Charisma', 3, 3)]),
    O("Les utilisateurs se plaignent et la direction demande d'y aller doucement.\n\nLe savais-tu ? Changer les habitudes demande de la pédagogie : on explique pourquoi avant d'imposer.", ['P-S', 'Charisma'])]),
  ("Changer juste celui-là en silence", [
    O("Le serveur est protégé, mais rien n'a changé pour les autres comptes.\n\nLe savais-tu ? Un bon mot de passe est long : une phrase de passe de 4 mots vaut mieux que « P@ssw0rd ».", ['P+S'])]),
 ]),
dict(track='Cyber', title="Audit payé le week-end",
 text="Une petite entreprise propose 2500 § à {0.SimFirstName} pour un audit de sécurité ce week-end.",
 options=[
  ("Accepter la mission", [
    O("Audit réussi, le client est ravi et paie rubis sur l'ongle !\n\nLe savais-tu ? Un audit se termine par un rapport : les failles trouvées et comment les corriger.", ['$2500', 'Logic'], 1, [('Logic', 5, 3)]),
    O("La mission était plus dure que prévu. {0.SimFirstName} n'est payé qu'en partie.\n\nLe savais-tu ? Avant une mission, on définit bien le périmètre (ce qu'on a le droit de tester).", ['$500'])]),
  ("Refuser : priorité à l'employeur", [
    O("Le chef apprécie la loyauté de {0.SimFirstName}.\n\nLe savais-tu ? Certains contrats interdisent de travailler pour d'autres clients : il faut toujours vérifier.", ['P+S'])]),
 ]),

# ======================= DÉVELOPPEMENT LOGICIEL =======================
dict(track='Dev', title="Bug en production !",
 text="Vendredi 17h : l'application plante pour tous les clients.",
 options=[
  ("Corriger directement en production", [
    O("Correctif en ligne en 10 minutes. {0.SimFirstName} est le héros du jour !\n\nLe savais-tu ? Corriger en production sans tester, c'est risqué : ça a marché cette fois.", ['P+M', 'Prog'], 1, [('Prog', 5, 3)]),
    O("Le correctif casse autre chose. La situation empire…\n\nLe savais-tu ? On teste toujours un correctif dans un environnement de test avant la production.", ['P-L', 'Prog'])]),
  ("Revenir à la version précédente", [
    O("Retour à la version d'avant en 2 minutes. {0.SimFirstName} corrigera lundi, au calme.\n\nLe savais-tu ? Revenir à la version précédente s'appelle un rollback. C'est facile grâce à Git et aux versions.", ['P+M', 'Logic'])]),
 ]),
dict(track='Dev', title="Relecture de code",
 text="Un collègue demande à {0.SimFirstName} de valider son code de 3000 lignes « vite fait, c'est urgent ».",
 options=[
  ("Le relire sérieusement", [
    O("{0.SimFirstName} trouve une faille de sécurité cachée. Bien vu !\n\nLe savais-tu ? La revue de code (code review) permet de trouver les bugs avant qu'ils arrivent chez les clients.", ['P+M', 'Logic'], 1, [('Logic', 4, 3)]),
    O("Trop long : {0.SimFirstName} ne finit pas à temps.\n\nLe savais-tu ? On demande des petites modifications : 3000 lignes d'un coup, c'est impossible à bien relire.", ['P-S'])]),
  ("Valider sans lire", [
    O("Rien de grave, cette fois.\n\nLe savais-tu ? Valider sans lire, c'est comme signer un contrat sans le lire.", [], 1),
    O("Le code supprime la base de données de test… Toute l'équipe est bloquée.\n\nLe savais-tu ? Les tests automatiques bloquent le code dangereux avant qu'il soit fusionné.", ['P-M'], 1)]),
 ]),
dict(track='Dev', title="Hackathon de 24h",
 text="L'entreprise organise un hackathon ce week-end : 24 heures pour créer une application.",
 options=[
  ("Participer", [
    O("L'équipe de {0.SimFirstName} gagne ! Prime de 1000 § à la clé.\n\nLe savais-tu ? Dans un hackathon, on apprend vite à travailler en équipe et à aller à l'essentiel.", ['P+L', 'Prog', '$1000'], 1, [('Prog', 4, 3)]),
    O("Pas de victoire, mais {0.SimFirstName} a beaucoup appris.\n\nLe savais-tu ? Les hackathons sont un excellent moyen de remplir son portfolio (ton GitHub, par exemple).", ['Prog'])]),
  ("Rester se reposer", [
    O("Un repos bien mérité.\n\nLe savais-tu ? L'équilibre vie pro / vie perso évite l'épuisement, très courant chez les développeurs.", [])]),
 ]),
dict(track='Dev', title="L'API sans documentation",
 text="Personne n'a jamais documenté l'API de l'entreprise. Le nouveau stagiaire est complètement perdu.",
 options=[
  ("Écrire une vraie documentation", [
    O("La doc est claire, le stagiaire est autonome. Toute l'équipe en profite.\n\nLe savais-tu ? Une API, c'est une « porte d'entrée » qui permet à deux programmes de communiquer.", ['P+M', 'Writing'], 1, [('Writing', 3, 3)]),
    O("La doc est un peu confuse, mais c'est mieux que rien.\n\nLe savais-tu ? Des outils comme Swagger génèrent une partie de la doc à partir du code.", ['P+S', 'Writing'])]),
  ("Lui dire de lire le code", [
    O("Le stagiaire met une semaine à comprendre.\n\nLe savais-tu ? Un code non documenté coûte cher : chaque nouveau doit tout redécouvrir.", ['P-S'])]),
 ]),
dict(track='Dev', title="Le client change tout",
 text="La veille de la livraison, le client change TOUT le cahier des charges.",
 options=[
  ("Négocier un nouveau délai", [
    O("Le client accepte une semaine de plus. Tout le monde respire.\n\nLe savais-tu ? Les méthodes agiles (Scrum) livrent par petits morceaux pour s'adapter aux changements.", ['P+M', 'Charisma'], 1, [('Charisma', 3, 3)]),
    O("Le client refuse et se plaint au chef.\n\nLe savais-tu ? Un cahier des charges signé protège les deux parties en cas de changement.", ['P-M', 'Charisma'])]),
  ("Tout coder pendant la nuit", [
    O("Livré à temps ! Mais {0.SimFirstName} est épuisé.\n\nLe savais-tu ? Le « crunch » (travailler la nuit) marche parfois, mais finit par créer des bugs.", ['P+L', 'Prog'], 1, [('Prog', 6, 2)]),
    O("Le code bâclé est plein de bugs. Le client est furieux.\n\nLe savais-tu ? Fatigué, on fait plus d'erreurs : la dette technique s'accumule.", ['P-M', 'Prog'])]),
 ]),
dict(track='Dev', title="L'IA qui code",
 text="Le chef veut que toute l'équipe utilise une IA pour coder plus vite.",
 options=[
  ("L'utiliser, mais vérifier chaque ligne", [
    O("{0.SimFirstName} code plus vite sans perdre en qualité.\n\nLe savais-tu ? Une IA peut se tromper : le développeur reste responsable du code qu'il livre.", ['P+M', 'Prog'], 1, [('Prog', 4, 2)])]),
  ("Copier-coller sans relire", [
    O("Ça marche… pour l'instant.\n\nLe savais-tu ? Copier du code qu'on ne comprend pas, c'est préparer des bugs pour plus tard.", ['P+S'], 1),
    O("Le code généré contenait une faille de sécurité. Oups.\n\nLe savais-tu ? Les failles classiques (comme l'injection SQL) se cachent souvent dans du code copié-collé.", ['P-L'], 1)]),
 ]),
dict(track='Dev', title="Mission freelance",
 text="Une start-up propose 2500 § à {0.SimFirstName} pour développer son site ce week-end.",
 options=[
  ("Accepter", [
    O("Site livré, client ravi… et compte en banque aussi !\n\nLe savais-tu ? En freelance, on fait un devis précis avant de commencer.", ['$2500', 'Prog'], 1, [('Prog', 5, 3)]),
    O("Le projet était plus gros que prévu : {0.SimFirstName} n'est payé qu'en partie.\n\nLe savais-tu ? Sans cahier des charges clair, un petit projet peut vite devenir énorme.", ['$500', 'Prog'])]),
  ("Refuser : priorité à l'employeur", [
    O("Le chef apprécie la loyauté de {0.SimFirstName}.\n\nLe savais-tu ? Beaucoup de développeurs commencent le freelance à côté avant de se lancer à 100 %.", ['P+S'])]),
 ]),
]

# ======================= VIE PROFESSIONNELLE : recrutement, carrière réelle =======================
CARDS += [
dict(track='any', title="Un chasseur de têtes appelle",
 text="Un recruteur contacte {0.SimFirstName} sur LinkedIn : une start-up propose 20 % de salaire en plus, un baby-foot et des stock-options… mais l'entreprise n'a que 6 mois de trésorerie.",
 options=[
  ("Utiliser l'offre pour négocier avec son patron", [
    O("Le patron fait une contre-offre : une prime de 1000 § pour garder {0.SimFirstName} !\n\nLe savais-tu ? Une offre concurrente est un bon argument, mais il ne faut pas en abuser.", ['$1000', 'P+S', 'Charisma'], 1, [('Charisma', 4, 3)]),
    O("Le patron le prend mal : « Si tu veux partir, la porte est là ! »\n\nLe savais-tu ? On négocie avec des faits (salaire du marché, résultats) plutôt qu'avec des menaces.", ['P-M', 'Charisma'])]),
  ("Refuser poliment", [
    O("La start-up fait faillite 4 mois plus tard. Bonne décision !\n\nLe savais-tu ? Avant d'accepter une offre, on se renseigne sur la santé de l'entreprise (levées de fonds, avis Glassdoor…).", ['P+S'])]),
 ]),
dict(track='any', title="L'offre d'une ESN",
 text="Une ESN (entreprise de services numériques) veut recruter {0.SimFirstName} : un client différent tous les 6 mois, et un test technique pour commencer.",
 options=[
  ("Passer le test technique pour voir son niveau", [
    O("Test réussi haut la main ! Même sans changer de travail, {0.SimFirstName} prend confiance.\n\nLe savais-tu ? Une ESN « loue » ses informaticiens à des clients : c'est souvent là qu'on débute en sortant du BTS.", ['Logic', 'Prog'], 1, [('Logic', 4, 3)]),
    O("Le test était dur, mais {0.SimFirstName} sait maintenant ce qu'il doit travailler.\n\nLe savais-tu ? Se faire évaluer de temps en temps aide à savoir où on en est.", ['Logic'])]),
  ("Ignorer le message", [
    O("{0.SimFirstName} reste concentré sur son travail actuel.\n\nLe savais-tu ? Interne ou ESN : en interne, on connaît bien une seule entreprise ; en ESN, on voit plein de contextes différents.", [])]),
 ]),
dict(track='any', title="Le recruteur trop curieux",
 text="Un recruteur d'une entreprise concurrente invite {0.SimFirstName} à déjeuner… et pose beaucoup de questions sur les projets secrets de son entreprise.",
 options=[
  ("Rester vague et poli", [
    O("{0.SimFirstName} a compris le piège : c'était de l'espionnage industriel. Son patron le félicite.\n\nLe savais-tu ? Les contrats de travail contiennent souvent une clause de confidentialité.", ['P+M'])]),
  ("Tout raconter pour impressionner", [
    O("Le patron l'apprend… Avertissement officiel !\n\nLe savais-tu ? Divulguer des informations confidentielles peut mener au licenciement pour faute grave.", ['P-L', 'Mischief'])]),
 ]),
dict(track='any', title="Le faux recruteur",
 text="{0.SimFirstName} reçoit une offre incroyable par mail : 10 000 §/mois ! Il suffit d'ouvrir la fiche de poste « Offre.pdf.exe ».",
 options=[
  ("Ouvrir le document", [
    O("C'était un virus ! L'ordinateur de {0.SimFirstName} part en réinstallation.\n\nLe savais-tu ? Un fichier « .pdf.exe » est un programme déguisé : la vraie extension est la dernière.", ['P-L'])]),
  ("Signaler le mail à la sécurité", [
    O("Bien vu ! Les pirates utilisent de fausses offres d'emploi pour piéger leurs victimes.\n\nLe savais-tu ? Afficher les extensions des fichiers dans Windows aide à repérer ce genre de piège.", ['P+M', 'Logic'])]),
 ]),
dict(track='any', title="L'entretien annuel",
 text="C'est l'entretien annuel de {0.SimFirstName} avec son manager.",
 options=[
  ("Arriver avec ses réussites chiffrées", [
    O("« 98 % des tickets résolus, 2 projets livrés » : le manager est impressionné. Prime de 500 § !\n\nLe savais-tu ? Des résultats chiffrés convainquent toujours plus que « j'ai beaucoup travaillé ».", ['P+L', '$500', 'Charisma'], 1, [('Charisma', 3, 3)]),
    O("Bon entretien, mais sans plus.\n\nLe savais-tu ? L'entretien annuel sert aussi à demander des formations.", ['P+S'])]),
  ("Improviser", [
    O("{0.SimFirstName} ne se souvient plus de ce qu'il a fait en mars… Le manager reste sur sa faim.\n\nLe savais-tu ? Noter ses réussites au fil de l'année, c'est un bon réflexe (comme ton portfolio de BTS !).", ['P-S'])]),
 ]),
dict(track='any', title="La demande d'augmentation",
 text="Cela fait un an que {0.SimFirstName} n'a pas été augmenté.",
 options=[
  ("Demander +10 % avec les salaires du marché", [
    O("Accordé ! Une prime de 1000 § en attendant la nouvelle fiche de paie.\n\nLe savais-tu ? Des sites et des études publient les salaires moyens des métiers de l'informatique : c'est un bon appui.", ['$1000', 'Charisma'], 1, [('Charisma', 5, 3)]),
    O("« Pas cette année, le budget est serré. »\n\nLe savais-tu ? Si on refuse l'augmentation, on peut négocier autre chose : formation, télétravail, matériel.", ['Charisma'])]),
  ("Attendre qu'on la propose", [
    O("Personne ne l'a proposée…\n\nLe savais-tu ? En entreprise, il faut souvent demander : rares sont les augmentations qui tombent du ciel.", [])]),
 ]),
dict(track='any', title="Le télétravail",
 text="Des amis de {0.SimFirstName} ont 2 jours de télétravail par semaine. Et si on demandait la même chose ?",
 options=[
  ("Proposer un essai d'un jour par semaine", [
    O("Le manager accepte un essai. {0.SimFirstName} est plus efficace et le prouve !\n\nLe savais-tu ? Pour télétravailler en sécurité, on passe par un VPN de l'entreprise.", ['P+M', 'Charisma'], 1, [('Charisma', 3, 3)]),
    O("Refusé : « On ne peut pas surveiller le travail à distance. »\n\nLe savais-tu ? Le télétravail se négocie souvent avec des objectifs clairs à atteindre.", ['P-S'])]),
  ("Ne rien demander", [
    O("Rien ne change.\n\nLe savais-tu ? Le télétravail est encadré par un accord d'entreprise ou une charte.", [])]),
 ]),
dict(track='any', title="Le stagiaire de BTS SIO",
 text="Un stagiaire de BTS SIO arrive dans l'équipe, et c'est {0.SimFirstName} qui doit l'encadrer.",
 options=[
  ("Lui confier une vraie mission", [
    O("Le stagiaire installe un serveur GLPI de A à Z. Il est ravi, et {0.SimFirstName} a appris à expliquer.\n\nLe savais-tu ? En stage de BTS, une vraie mission bien documentée est parfaite pour l'épreuve E5 !", ['P+M', 'Charisma'])]),
  ("Lui faire faire des photocopies", [
    O("Le stagiaire s'ennuie… et le dit dans son rapport de stage.\n\nLe savais-tu ? Un stage réussi peut finir en embauche ou en alternance : c'est gagnant pour l'entreprise aussi.", ['P-S'])]),
 ]),
dict(track='any', title="Fichiers clients et RGPD",
 text="Le service commercial veut mettre le fichier clients (avec les coordonnées bancaires) sur un Google Drive perso « pour aller plus vite ».",
 options=[
  ("Refuser et proposer une solution conforme", [
    O("{0.SimFirstName} propose un partage sécurisé sur le serveur de l'entreprise. Le délégué à la protection des données approuve.\n\nLe savais-tu ? Le RGPD oblige à protéger les données personnelles. La CNIL peut donner de grosses amendes.", ['P+M', 'Logic'])]),
  ("Laisser faire", [
    O("Le Drive était public… Les données ont fuité et la CNIL ouvre une enquête !\n\nLe savais-tu ? En cas de fuite de données, l'entreprise doit prévenir la CNIL dans les 72 heures.", ['P-L'], 1),
    O("Pas de problème… pour l'instant.\n\nLe savais-tu ? Le RGPD s'applique même si personne ne s'en rend compte.", ['P-S'], 1)]),
 ]),
dict(track='any', title="Le salon de la tech",
 text="L'entreprise envoie {0.SimFirstName} à un grand salon de la tech pendant une journée.",
 options=[
  ("Rencontrer un maximum de monde", [
    O("{0.SimFirstName} repart avec 30 contacts et plein d'idées !\n\nLe savais-tu ? Le réseau professionnel aide beaucoup à trouver un stage, une alternance ou un emploi.", ['P+M', 'Charisma'], 1, [('Charisma', 3, 2)]),
    O("Quelques discussions sympas, sans plus.\n\nLe savais-tu ? Avoir son CV à jour sur LinkedIn aide après un salon.", ['Charisma'])]),
  ("Suivre les conférences techniques", [
    O("{0.SimFirstName} découvre plein de nouvelles technos.\n\nLe savais-tu ? La veille technologique fait partie du métier (et c'est demandé au BTS SIO !).", ['Logic', 'Prog'])]),
 ]),
dict(track='any', title="Le collègue épuisé",
 text="Un collègue enchaîne les heures supplémentaires et semble au bord de l'épuisement.",
 options=[
  ("En parler au manager", [
    O("Le manager répartit mieux le travail. Le collègue remercie {0.SimFirstName}.\n\nLe savais-tu ? L'épuisement professionnel (burn-out) est fréquent en informatique, surtout pendant les astreintes.", ['P+S', 'Charisma'])]),
  ("Reprendre une partie de son travail", [
    O("{0.SimFirstName} l'aide beaucoup, mais rentre très fatigué.\n\nLe savais-tu ? Aider, c'est bien, mais il faut aussi savoir dire non pour se protéger.", ['P+M'])]),
 ]),
dict(track='base', title="Proposition d'alternance",
 text="L'entreprise propose à {0.SimFirstName} de reprendre ses études en alternance (licence pro, bachelor) tout en restant salarié.",
 options=[
  ("Accepter", [
    O("Une semaine à l'école, deux semaines en entreprise : c'est intense mais {0.SimFirstName} progresse très vite.\n\nLe savais-tu ? Après un BTS SIO, beaucoup continuent en alternance : l'école est payée et on a un salaire.", ['P+M', 'Logic', 'Prog'])]),
  ("Refuser", [
    O("{0.SimFirstName} préfère rester à plein temps.\n\nLe savais-tu ? On peut aussi progresser par des certifications, sans reprendre d'études.", [])]),
 ]),
dict(track='Admin', title="Coupure de courant !",
 text="Coupure d'électricité dans tout le bâtiment ! La salle serveurs tient sur les batteries.",
 options=[
  ("Éteindre proprement les serveurs", [
    O("L'onduleur a tenu et {0.SimFirstName} a tout éteint proprement : aucune donnée perdue.\n\nLe savais-tu ? Un onduleur (UPS) est une grosse batterie qui laisse le temps d'éteindre les serveurs sans les abîmer.", ['P+L', 'Logic'], 1, [('Logic', 4, 3)]),
    O("Une machine n'a pas eu le temps de s'éteindre et doit être réparée.\n\nLe savais-tu ? On peut configurer l'onduleur pour qu'il éteigne les serveurs tout seul.", ['P-S', 'Logic'])]),
  ("Attendre que le courant revienne", [
    O("Les batteries se vident au bout de 10 minutes : les serveurs s'arrêtent d'un coup. Base de données abîmée !\n\nLe savais-tu ? Une coupure brutale peut corrompre les données : c'est pour ça qu'on éteint proprement.", ['P-L'])]),
 ]),
dict(track='Admin', title="Un hébergeur cloud recrute",
 text="Un grand hébergeur cloud propose un poste à {0.SimFirstName} : « Ici, tout est automatisé, on gère des milliers de serveurs ! »",
 options=[
  ("Se former au cloud pour être prêt", [
    O("{0.SimFirstName} découvre la virtualisation à grande échelle. Son entreprise actuelle en profite aussi !\n\nLe savais-tu ? Le cloud, c'est louer des serveurs chez un hébergeur au lieu de les avoir dans ses locaux.", ['P+M', 'Logic', 'Prog'])]),
  ("Rester sur les serveurs « sur site »", [
    O("{0.SimFirstName} reste fidèle à sa salle serveurs.\n\nLe savais-tu ? Beaucoup d'entreprises mélangent les deux : c'est le « cloud hybride ».", [])]),
 ]),
dict(track='Cyber', title="L'agence nationale recrute",
 text="L'agence nationale de cybersécurité cherche des profils comme {0.SimFirstName} pour une formation avancée.",
 options=[
  ("Postuler à la formation", [
    O("Accepté ! {0.SimFirstName} revient avec de nouvelles compétences et beaucoup de prestige.\n\nLe savais-tu ? En France, l'ANSSI protège les administrations et les entreprises importantes contre les cyberattaques.", ['P+L', 'Logic', 'Prog'], 1, [('Logic', 6, 3)]),
    O("Refusé cette fois, mais la sélection était très dure.\n\nLe savais-tu ? Les CTF (compétitions de hacking éthique, comme Root-Me) sont un super entraînement.", ['Logic'])]),
  ("Rester dans le privé", [
    O("{0.SimFirstName} préfère rester dans son équipe.\n\nLe savais-tu ? Public ou privé, les experts en cybersécurité sont très recherchés.", [])]),
 ]),
dict(track='Dev', title="Un studio de jeux vidéo",
 text="Un studio de jeux vidéo a vu le GitHub de {0.SimFirstName} et lui propose un test de code.",
 options=[
  ("Passer le test", [
    O("Le studio adore son code et lui propose une mission freelance payée 2500 § !\n\nLe savais-tu ? Un GitHub avec des projets perso est souvent plus parlant qu'un CV.", ['$2500', 'Prog'], 1, [('Prog', 6, 3)]),
    O("Raté, mais {0.SimFirstName} a appris plein de choses sur les moteurs de jeu.\n\nLe savais-tu ? Le jeu vidéo est un secteur passionnant mais très exigeant.", ['Prog'])]),
  ("Décliner", [
    O("{0.SimFirstName} reste sur ses projets actuels.\n\nLe savais-tu ? Garder un projet perso à côté permet de continuer à apprendre.", [])]),
 ]),
]
