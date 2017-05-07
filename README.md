I) Utilisation
1) Installation
Pour installer le système de monitoring il faut choisir entre deux fichiers :
-soit on l'installe en mode client 'sudo /configClient.sh' 
-ou en mode Serveur qui installe aussi un monitoring client chargé de collecter les données 'sudo ./configServeur.sh'

ATTENTION : vous devez être mode super utilisateur.


Lors de l'installation on va vous demander le délai de l'envoie des données:
Vous devez entrer une valeur comprise entre 1 et 5 minutes.
L’IP et le port vont vous être demandé, tapez l’IP du serveur et le port que vous voulez allouer à la machine.

-Après avoir installé une nouvelle Machine vous devez écrire dans votre console :
"sudo GestionSystemeMenuServeur" , l’IHM va se mettre en place :
*Aller a la troisième ligne  ou appuyer sur « 3 » et appuyer entrez 
*Tapez le port que vous voulez allouer a la machine cliente
*Tapez le nom de la machine cliente 
ATTENTION : Le nom de la machine doit être identique avec  la chaîne de $HOST de la machine que vous voulez installée


2)Procédure d'Utilisation
Pour utiliser le monitoring nous n’avons pas besoin de taper des lignes de commande il faut juste accéder a l’IHM disponible sur console en tapant :
- "sudo GestionSystemeClient" pour configurer les données des clients  plus précisément la situation de crise.
- "sudo GestionSystemeMenuServeur"  pour gérer l'ensemble des serveur de votre parc .

---GESTION SYSTÈME MENU SERVEUR
	-configuration Limite de  Stockage : permet de configurer la taille maximale de la base de donnée
	-Sauvegarde et restauration : Permet le backup et la restauration de la base de donnée
	-Installer la communication machine serveur : est utilisé après avoir installé le module client dans une nouvelle machine en fait de lui allouer un port
	-Supprimer la communication machine serveur : permet de supprimer une machine dans la base de donnée et empêcher la communication, DANGER.
	-Demarrer l’Ecoute : permet d’ouvrir les ports pour récupérer les données des clients
	-Dessiner une graphe : permet de dessiner une graphe selon votre choix
		-ram
		-cpu
		-nombre utilisateur
	-Configuration mail : permet d’écrire le mail par défaut

		-Mail Alerte Cert : mail par défaut lors de l’envoie des alerte CERT
		-Mail Situation Crise : mail par défaut de la situation de crise
	-Quitter : pour quitter le Menu . Attention ne pas appuyer « Ctr+C »  ,si vous l’appuyez par mégarde tapez « reset » puis entrez.
---GESTION SYSTÈME MENU CLIENT
	-Sélection des alerte : Permet de sélectionner les ressource qu’on doit auditer
	-Modifier la Situation de crise : Permet de modifier la limite des ressources pour declencher une situation de crise.
3) Désinstallation

Pour désinstaller le Monitoring Serveur coté serveur il faudra taper la commande :
-"/usr/sbin/removeGestionSystemeServeur.sh"
NB : la désinstallation du serveur entraîne la désinstallation du module client.


Pour désinstaller le Monitoring coté Client il faut taper la commande :
-"/usr/sbin/removeGestionSystemeClient.sh"

II)Modules 
1) Module affichage

Ce module contient l'ensemble des programmes nécessaires pour interagir avec le système notamment le Menu du client et le Menu du Serveur.

Caractéristique des scripts menus :  Pour ajouter une nouvelle menu dans le code source se fait   en rajoutant des données dans la variable menu_data .
-menu_data 
*titre  Correspond a l’intitule du menu-data
*type : MENU ou COMMAND  si le type est MENU vous devez ajouter les champs 
 subtitle qui correspond au sous titre du « MENU » et le champs option qui va contenir l’ensemble des sous menu organise de la même façon 
si c’est un type  « COMMAND » on doit ajouter le champ ‘command’  et la commande qu’on doit exécuter.

-Partie 3 : module Affichage + Bonus mode interactif

2) Modules Collecte
Module chargé de collecter les données des ressources notamment : le pourcentage d’utilisation du cpu ,du disque et du ram utilisé, le nombre d'utilisateur , le nombre de processus ,  la température de la machine.
IMPORTANT :l’ensemble des scripts du module client doit être lié au crontab (voire configClient.sh)

-Partie 1 : Collecte d'information

3) Module serveur 
Ce module contient l'ensemble des scripts  nécessaires pour qu'un serveur puisse fonctionné : 
-CreationBD.py : Pour la création d'une base de donnée
*arguments : ne prend pas d’arguments
-delete_in_db.py : Permettant de supprimer les données
*arguments : delete_in_db.py nomdelabase nomdelatable colonne1 critere1 colonne2 critere2..
delete_table_in_db.py :Supprime une table passée en argument 
*arguments : delete_table_in_db.py nomdb nomtable1 nomtable2 ...
-denier_etat.py : Retourne une dictionnaire (python) ayant les dernier états de toutes les machines 
*arguments : ernier_etat.py nom_table1 nom_table2 ...
-ecoute_port.py :Récupère les ports dans la base de donnée et appelle un autre script qui gère l’écoute des ports
*arguments : prend pas d’argument
-graphe_historique.py : Script permettant de récupérer les données de toutes les machines d'une table donnée
*argument : graphe_historique.py nom_de_la_table
-insert_in_db.py : Script permettant l'insertion des données
*arguments : insert_in_db.py db_name nomtable colonne1 donnee1 colonne2 donnee2 ...
-installation_port.sh : Script ermettant d'enregistrer une nouvelle machine et de lui attribuer un port
*arguments : prend pas d’argument
-limite_Stockage.sh : Script permettant de configurer la limite de stockage
*arguments : prend pas d’argument
-ouvrir_des_ports.sh : Charger d’écouter les ports passés en argument
*arguments :  ouvrir_des_ports.sh port1 port2 ...
-suppression_machine.sh : Programme permettant de supprimer des machines
*arguments : prend pas d’argument
-tache_exec.sh : Script permettant d'inserer les données dans la base
*arguments : prend pas d’arguments



Partie 4 : module web-service qui attend les requêtes + modules web service qui communique avec le module web service +Affichage graphique
Partie 2 : +Bonus utilisation de format standard ou d’un moteur de base de données sans serveur + Bonus ajout d’une nouvelle machine dans le 
réseaux ne nécessite pas de modification manuelle du code ou de la base + Bonus Taille maximum de l’historique configurable.

4) Module Crise Détection 
-Configuartion_crise.sh : Choix du niveau maximum que peut atteindre les ressources
-crise.py : Script qui cherche est ce que les ressources n'ont pas atteint la limite fixée, si c'est le cas on l'envoie par mail à l'administrateur
-crisedecision.py : Script nous permettant de choisir les ressources qui nécessitent d’être surveillé
-mail_alerte.sh : Script permettant de récupérer le mail par défaut et de remplacer les valeurs, ou envoie l’état seulement

-Partie 3: Un module de détection de situation de crise + Un module d’envoi de mail + Bonus Critère de la situation de crise configurable + Bonus  Contenu de l’e-mail paramétrable (fichier template) 

5) Web
-Actualiser_cert.py: script permettant d'envoyer de nouvelles alertes CERT
-mail_cert.sh : script permettant de récupérer le mail qui se trouve dans le template et de remplacer les données
-sendmail.py : module permettant d'envoyer le message
6) Interface web
-makehtml.py : Script  permettant de mettre en place l'interface web


Partie 4 : Interface web
III) Librairie utilisée

-feedparser : utilisé à cause de leur documentation

-pygal : utilisé à cause de leur documentation

-sqlite3 : moteur de base de donnée facile a utiliser



IMPORTANT :

NB : Si vous voulez tester par script vous pouvez l'appeler en utilisant la commande
"sudo nom_du_script"

Si le sous_menu "demarre l ecoute " s’arrête après la réception d 'une donnée , vous pouvez taper "sudo ecouter_ports.py" en effet le sous_menu ne marche pas dans certaines versions de  Linux .
