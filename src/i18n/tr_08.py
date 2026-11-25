T = {
'card99_text': ("Reviewing the firewall, {0.SimFirstName} finds a rule \"Source: any, Destination: any, Allow\".", "Al revisar el cortafuegos, {0.SimFirstName} encuentra una regla «Origen: cualquiera, Destino: cualquiera, Permitir»."),
'card99_title': ("The \"Allow Everything\" Rule", "La regla «permitirlo todo»"),
'card100_opt0_res0': ("If a camera gets hacked, the hacker can no longer reach the servers.\n\nDid you know? Segmentation limits how far an attack can spread. Connected devices are often poorly secured.", "Si hackean una cámara, el atacante ya no puede llegar a los servidores.\n\n¿Lo sabías? La segmentación limita la propagación de un ataque. Los objetos conectados suelen estar mal protegidos."),
'card100_opt0': ("Split into zones with a firewall between them", "Separar en zonas con un cortafuegos entre ellas"),
'card100_opt1_res0': ("A hacked camera becomes an entry point to the whole network.\n\nDid you know? A \"flat\" network lets a hacker move around everywhere.", "Una cámara hackeada sirve de puerta de entrada a toda la red.\n\n¿Lo sabías? Una red «plana» deja que un atacante se mueva por todas partes."),
'card100_opt1': ("Keep one big network", "Mantener una sola red grande"),
'card100_text': ("At the company, PCs, servers and cameras are all on the same network.", "En la empresa, los equipos, los servidores y las cámaras están todos en la misma red."),
'card100_title': ("Segmenting the Network", "Segmentar la red"),
'card101_opt0_res0': ("The vendor never called: it was a scam attempt.\n\nDid you know? Always call back using a number you found yourself, not the one the caller gave you.", "El proveedor nunca llamó: era un intento de estafa.\n\n¿Lo sabías? Siempre se devuelve la llamada a un número que uno mismo ha buscado, no al que da quien llama."),
'card101_opt0': ("Call the vendor back on the official number", "Llamar al proveedor al número oficial"),
'card101_opt1_res0': ("The \"technician\" disables the firewall and disappears…\n\nDid you know? Urgency is a classic pressure tactic used by scammers.", "El «técnico» desactiva el cortafuegos y desaparece…\n\n¿Lo sabías? La urgencia es una técnica de presión clásica de los estafadores."),
'card101_opt1': ("Give access, it's urgent", "Dar acceso, es urgente"),
'card101_text': ("Someone calls {0.SimFirstName}: \"I'm the technician from your firewall vendor, give me admin access for an urgent update.\"", "Alguien llama a {0.SimFirstName}: «Soy el técnico del proveedor del cortafuegos, deme acceso de administrador para una actualización urgente.»"),
'card101_title': ("The Fake Technician's Call", "La llamada del falso técnico"),
'card102_opt0_res0': ("Everything is logged and timestamped: the answer comes in 5 minutes.\n\nDid you know? Centralized logs (in a SIEM) keep a record even if a hacker wipes the server's own logs.", "Todo está registrado y con fecha y hora: la respuesta llega en 5 minutos.\n\n¿Lo sabías? Los registros centralizados (en un SIEM) guardan un rastro aunque un atacante borre los del servidor."),
'card102_opt0': ("Pull the centralized logs", "Sacar los registros centralizados"),
'card102_opt1_res0': ("The audit flags a serious lack of traceability.\n\nDid you know? Without logs, it's impossible to know what happened after an attack.", "La auditoría señala una grave falta de trazabilidad.\n\n¿Lo sabías? Sin registros, es imposible saber qué pasó tras un ataque."),
'card102_opt1': ("Admit there are no logs", "Reconocer que no hay registros"),
'card102_text': ("An auditor asks who logged into the HR server last month.", "Un auditor pregunta quién se conectó al servidor de RR. HH. el mes pasado."),
'card102_title': ("The Login Logs", "Los registros de conexión"),
'card103_opt0_res0': ("Access only to their server, with two-factor authentication and logging.\n\nDid you know? Many attacks come in through a less secure supplier (a \"bounce\" attack).", "Acceso solo a su servidor, con doble autenticación y registro.\n\n¿Lo sabías? Muchos ataques entran a través de un proveedor menos protegido (ataque de rebote)."),
'card103_opt0': ("Give limited, monitored access", "Darle un acceso limitado y vigilado"),
'card103_opt1_res0': ("The supplier gets hacked… and the hacker walks into your network with their account.\n\nDid you know? Least privilege applies to suppliers too!", "Hackean al proveedor… y el atacante entra en tu red con su cuenta.\n\n¿Lo sabías? ¡El mínimo privilegio también vale para los proveedores!"),
'card103_opt1': ("Give them an admin account, it's simpler", "Darle una cuenta de administrador, es más simple"),
'card103_text': ("A supplier is about to get network access to manage some software.", "Un proveedor va a recibir acceso a la red para gestionar un programa."),
'card103_title': ("The Supplier Audit", "La auditoría del proveedor"),
'card104_opt0_res0': ("The director understands and goes through an approved IT policy.\n\nDid you know? Messages marked as \"personal\" are protected, even on company equipment.", "El director lo entiende y opta por una normativa informática aprobada.\n\n¿Lo sabías? Los mensajes identificados como «personales» están protegidos, incluso en el material de la empresa."),
'card104_opt0': ("Explain what the law says", "Explicar lo que dice la ley"),
'card104_opt1_res0': ("An employee files a complaint. The company is in the wrong.\n\nDid you know? The CISO also advises on legality, not just on technology.", "Un empleado presenta una denuncia. La empresa está en falta.\n\n¿Lo sabías? El CISO también asesora sobre la legalidad, no solo sobre la técnica."),
'card104_opt1': ("Obey without arguing", "Obedecer sin discutir"),
'card104_text': ("The director wants to read employees' personal emails \"for security\".", "El director quiere leer los correos personales de los empleados «por seguridad»."),
'card104_title': ("The Boss Wants to Watch Everything", "El jefe quiere vigilarlo todo"),
'card105_opt0_res0': ("The alert was real: the vendor had been hacked. The network is spared.\n\nDid you know? Checking a file's signature and hash makes sure it hasn't been tampered with.", "La alerta era cierta: habían hackeado al editor. La red se salva.\n\n¿Lo sabías? Comprobar la firma y la huella (hash) de un archivo garantiza que no se ha modificado."),
'card105_opt0_res1': ("False alarm, the update was clean. A day's delay, no big deal.\n\nDid you know? Always cross-check several sources before concluding.", "Falsa alarma, la actualización estaba limpia. Un día de retraso, nada grave.\n\n¿Lo sabías? Siempre se contrastan varias fuentes antes de sacar conclusiones."),
'card105_opt0': ("Block the update and investigate", "Bloquear la actualización y verificar"),
'card105_opt1_res0': ("The malicious code spreads to every PC…\n\nDid you know? Updates are rolled out to a small test group first.", "El código malicioso se extiende por todos los equipos…\n\n¿Lo sabías? Las actualizaciones se despliegan primero en un pequeño grupo de prueba."),
'card105_opt1': ("Install it everywhere as usual", "Instalarla en todas partes como siempre"),
'card105_text': ("An update to a well-known program seems to contain malicious code, according to an alert online.", "Según una alerta en Internet, una actualización de un programa conocido parece contener código malicioso."),
'card105_title': ("The Booby-Trapped Update", "La actualización trampa"),
'card106_opt0_res0': ("A clear policy: which data can and can't go into an AI. Everyone gets it.\n\nDid you know? What you send to an online service may be stored elsewhere: be careful with sensitive data.", "Una normativa clara: qué datos se pueden poner o no en una IA. Todo el mundo lo entiende.\n\n¿Lo sabías? Lo que se envía a un servicio en línea puede almacenarse en otro sitio: cuidado con los datos sensibles."),
'card106_opt0': ("Write an AI usage policy", "Redactar una norma de uso de la IA"),
'card106_opt1_res0': ("A confidential document ends up stored with an outside service…\n\nDid you know? New technologies also create new risks.", "Un documento confidencial acaba almacenado en un servicio externo…\n\n¿Lo sabías? Las nuevas tecnologías también crean nuevos riesgos."),
'card106_opt1': ("Do nothing", "No hacer nada"),
'card106_text': ("Employees are pasting confidential documents into an online AI to summarize them.", "Algunos empleados copian documentos confidenciales en una IA en línea para resumirlos."),
'card106_title': ("AI and Data", "La IA y los datos"),
'card107_opt0_res0': ("The QR code led to a fake login page that stole passwords. Nobody fell for it.\n\nDid you know? A QR code is just a hidden link: check the address before typing anything (quishing).", "El código QR llevaba a una página de inicio de sesión falsa que robaba contraseñas. Nadie ha caído.\n\n¿Lo sabías? Un código QR es solo un enlace oculto: se comprueba la dirección antes de escribir nada (quishing)."),
'card107_opt0': ("Remove them and warn everyone", "Quitarlas y avisar a todos"),
'card107_opt1_res0': ("{0.SimFirstName} types their password on the fake page… Everything has to be changed urgently.\n\nDid you know? Never test a suspicious link with your real account.", "{0.SimFirstName} escribe su contraseña en la página falsa… Hay que cambiarlo todo de urgencia.\n\n¿Lo sabías? Nunca se prueba un enlace sospechoso con tu cuenta real."),
'card107_opt1': ("Scan it to see", "Escanearlo para ver"),
'card107_text': ("Stickers with a \"Free Wi-Fi\" QR code have appeared in the company lobby.", "Han aparecido en el vestíbulo de la empresa pegatinas con un código QR de «Wi-Fi gratis»."),
'card107_title': ("The Booby-Trapped QR Code", "El código QR trampa"),
'tt_missions_done': ("No more missions today. Come back after the next workday.", "No quedan misiones por hoy. Vuelve después de la próxima jornada de trabajo."),
'tt_free_busy': ("Contract already finished.", "Contrato ya terminado."),
}

# Missions et freelance : traduits ici puis assemblés avec les mêmes modèles que home.py
M = {  # clé : (nom EN, astuce EN, nom ES, astuce ES)
 'tickets': ("Handle tickets remotely", "A good ticket says: who, what, since when, and what has already been tried. It saves a huge amount of time.",
             "Atender tickets a distancia", "Un buen ticket dice: quién, qué, desde cuándo y qué se ha probado ya. Ahorra muchísimo tiempo."),
 'certif': ("Study for a certification (Cisco, Microsoft…)", "The OSI model has 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, Application. Mnemonic: \"Please Do Not Throw Sausage Pizza Away\".",
            "Estudiar para una certificación (Cisco, Microsoft…)", "El modelo OSI tiene 7 capas: Física, Enlace de datos, Red, Transporte, Sesión, Presentación, Aplicación."),
 'vlan': ("Configure a switch's VLANs", "A VLAN splits a switch into several separate networks. The port linked to the router is in \"trunk\" mode to carry every VLAN.",
          "Configurar las VLAN de un switch", "Una VLAN divide un switch en varias redes separadas. El puerto conectado al router está en modo «trunk» para que pasen todas las VLAN."),
 'backup': ("Check last night's backups", "A backup you've never restored isn't a backup. Run restore tests regularly.",
            "Revisar las copias de seguridad de anoche", "Una copia que nunca se ha restaurado no es una copia. Se hacen pruebas de restauración con regularidad."),
 'script': ("Write an automation script (PowerShell)", "If you do the same task more than 3 times, automate it. Example: create 30 user accounts from a CSV file.",
            "Escribir un script de automatización (PowerShell)", "Si haces la misma tarea más de 3 veces, automatízala. Ejemplo: crear 30 cuentas de usuario desde un archivo CSV."),
 'schema': ("Update the network diagram", "Good documentation (diagram, IP addressing plan, passwords in a vault) lets a colleague cover for you during your vacation.",
            "Actualizar el esquema de la red", "Una buena documentación (esquema, plan de direccionamiento IP, contraseñas en una caja fuerte digital) permite que un compañero te sustituya en vacaciones."),
 'supervision': ("Watch the monitoring alerts", "Monitoring tools (Zabbix, Nagios, Centreon) poll devices, often over SNMP, and warn you before users complain.",
                 "Vigilar las alertas de supervisión", "Las herramientas de supervisión (Zabbix, Nagios, Centreon) consultan los equipos, a menudo por SNMP, y avisan antes de que los usuarios se quejen."),
 'logs': ("Analyze security logs", "A SIEM gathers logs from every device and spots abnormal behavior, like 50 wrong passwords in 1 minute.",
          "Analizar registros de seguridad", "Un SIEM reúne los registros de todos los equipos y detecta comportamientos anómalos, como 50 contraseñas erróneas en 1 minuto."),
 'cve': ("Keep watch on vulnerabilities (CVEs)", "Every known flaw has a CVE number and a CVSS severity score out of 10. Government CERTs publish alerts.",
         "Vigilar las vulnerabilidades (CVE)", "Cada fallo conocido tiene un número CVE y una nota de gravedad CVSS sobre 10. El INCIBE-CERT publica alertas en español."),
 'phishing': ("Prepare an awareness phishing test", "A fake phishing campaign is meant to train employees, not punish them. You train them right afterward.",
              "Preparar un falso phishing de concienciación", "Una campaña de falso phishing sirve para entrenar a los empleados, no para castigarlos. Se les forma justo después."),
 'lab': ("Practice in a pentest lab", "Only test machines you're allowed to attack: a personal lab or a CTF. Attacking without permission is a crime.",
         "Entrenar en un laboratorio de pentest", "Solo se prueban máquinas que se tiene derecho a atacar: un laboratorio propio o un CTF. Atacar sin autorización es un delito."),
 'incident': ("Write an incident response procedure", "The steps of incident response: detect, contain (isolate the machine), eradicate, recover, then learn the lessons.",
              "Redactar un procedimiento de respuesta a incidentes", "Las etapas de una respuesta a incidentes: detectar, contener (aislar la máquina), erradicar, restaurar y sacar conclusiones."),
 'bugs': ("Fix bugs", "To fix a bug, start by reproducing it. A bug you can't reproduce is very hard to fix.",
          "Corregir bugs", "Para corregir un bug, se empieza por reproducirlo. Un bug que no se sabe reproducir es muy difícil de corregir."),
}
F = {  # clé : (nom, texte, astuce) EN puis ES
 'pc': (("Fix a home user's PC", "Mrs. Smith's PC was crawling: 14 toolbars and an expired antivirus.", "Before touching a PC, back up the client's important files."),
        ("Reparar el PC de un particular", "El PC de la señora García iba lentísimo: 14 barras de herramientas y un antivirus caducado.", "Antes de tocar un PC, se hace una copia de los archivos importantes del cliente.")),
 'wifi': (("Install Wi-Fi for a small shop", "The bakery now has a Wi-Fi for the cash register and a separate guest Wi-Fi.", "Keep guest Wi-Fi separate from the business network, and use WPA2 or, better, WPA3."),
          ("Instalar el Wi-Fi de una tienda", "La panadería tiene ahora un Wi-Fi para la caja y otro Wi-Fi de invitados separado.", "El Wi-Fi de invitados se separa de la red de la empresa y se usa WPA2 o, mejor, WPA3.")),
 'site': (("Build a website for a tradesperson", "The local plumber has a website: HTML, CSS and a contact form.", "A modern website must use HTTPS (the padlock): data is encrypted between the visitor and the server."),
          ("Crear la web de un autónomo", "El fontanero del barrio ya tiene web: HTML, CSS y un formulario de contacto.", "Una web moderna debe usar HTTPS (el candado): los datos viajan cifrados entre el visitante y el servidor.")),
 'backup': (("Set up backups for a medical office", "The medical office now has automatic nightly backups, including an off-site copy.", "The 3-2-1 rule: 3 copies, on 2 different media, 1 of them off-site."),
            ("Implantar las copias de seguridad de una consulta", "La consulta médica tiene copias automáticas cada noche, una de ellas fuera del edificio.", "Regla 3-2-1: 3 copias, en 2 soportes distintos, 1 de ellas fuera del edificio.")),
 'reseau': (("Configure a small business network", "Switches, VLANs, DHCP and a firewall: the small business has a real, clean network.", "DHCP hands out IP addresses automatically. Servers and printers get reserved static IPs."),
            ("Configurar la red de una pyme", "Switches, VLAN, DHCP y cortafuegos: la pyme tiene por fin una red en condiciones.", "El DHCP reparte automáticamente las direcciones IP. Se reservan IP fijas para los servidores y las impresoras.")),
 'audit': (("Run a security audit for a small business", "{0.SimFirstName} hands in a clear report: 3 serious flaws, 5 medium ones, and how to fix them.", "An audit always comes with the client's written agreement, which sets what you're allowed to test."),
           ("Hacer la auditoría de seguridad de una pyme", "{0.SimFirstName} entrega un informe claro: 3 fallos graves, 5 medios y cómo corregirlos.", "Una auditoría siempre se hace con un acuerdo por escrito del cliente, que fija lo que se puede probar.")),
 'bounty': (("Bug bounty: hunt for a flaw (legally)", "{0.SimFirstName} finds a flaw on a big company's website and reports it properly. Reward paid!", "Bug bounty means getting paid to find flaws, following the rules the company sets."),
            ("Bug bounty: buscar un fallo (legalmente)", "{0.SimFirstName} encuentra un fallo en la web de una gran empresa y lo comunica correctamente. ¡Recompensa cobrada!", "El bug bounty consiste en cobrar por encontrar fallos, siguiendo las reglas que fija la empresa.")),
}
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from home import MISSIONS, FREELANCE
SK = {'en': {'Prog': 'Programming', 'Logic': 'Logic', 'Handi': 'Handiness', 'Mischief': 'Mischief'},
      'es': {'Prog': 'Programación', 'Logic': 'Lógica', 'Handi': 'Manitas', 'Mischief': 'Travesuras'}}
for track, key, name, skill, tip in MISSIONS:
    en_n, en_t, es_n, es_t = M[key]
    T['si_name_m_' + key] = ('Mission: ' + en_n, 'Misión: ' + es_n)
    T['notif_m_%s_ok' % key] = ("{0.SimFirstName} finished today's missions: \"%s\".\n\nDid you know? %s" % (en_n, en_t),
                                "{0.SimFirstName} ha terminado las misiones del día: «%s».\n\n¿Lo sabías? %s" % (es_n, es_t))
    T['notif_m_%s_top' % key] = ("Excellent work! {0.SimFirstName}'s boss is impressed (performance up).\n\nDid you know? %s" % en_t,
                                 "¡Excelente trabajo! El jefe de {0.SimFirstName} está impresionado (el rendimiento sube).\n\n¿Lo sabías? %s" % es_t)
for key, name, req, lvl, minutes, pay, pay_top, skill, text, tip, risky in FREELANCE:
    (en_n, en_x, en_t), (es_n, es_x, es_t) = F[key]
    T['si_name_f_' + key] = ('Freelance: ' + en_n, 'Freelance: ' + es_n)
    if req:
        T['tt_free_req_' + key] = ("{0.SimFirstName} needs level %d %s for this contract." % (lvl, SK['en'][req]),
                                   "{0.SimFirstName} necesita %s nivel %d para este contrato." % (SK['es'][req], lvl))
    T['notif_f_%s_ok' % key] = ("Contract done: %s\n\n{0.SimFirstName} gets paid §%d.\n\nDid you know? %s" % (en_x, pay, en_t),
                                "Contrato terminado: %s\n\n{0.SimFirstName} cobra %d §.\n\n¿Lo sabías? %s" % (es_x, pay, es_t))
    T['notif_f_%s_top' % key] = ("Happy client! %s\n\nWith the tip, {0.SimFirstName} earns §%d.\n\nDid you know? %s" % (en_x, pay_top, en_t),
                                 "¡Cliente encantado! %s\n\nCon la propina, {0.SimFirstName} cobra %d §.\n\n¿Lo sabías? %s" % (es_x, pay_top, es_t))
    if risky:
        T['notif_f_%s_fail' % key] = ("No flaw found this time, so no reward.\n\nDid you know? %s Keep at it, your skill still improved." % en_t,
                                      "Esta vez no se ha encontrado ningún fallo, así que no hay recompensa.\n\n¿Lo sabías? %s Persevera, tu habilidad ha mejorado de todos modos." % es_t)
