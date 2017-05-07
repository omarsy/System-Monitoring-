# ! /bin/bash
#Configuration de l'envoie des sondes
echo "Entrez l'intervalle de temps de 1-5 :"
read int #L'intervalle pour l'envoie des sondes 
echo "Entrez l'Ip du serveur :"
read ip  # l'ip du serveur
echo "Entrez le port du serveur :"
read port #le port dedie pour la communication du serveur

apt-get install lm-sensors
# Installation des programmes
for fichier in `ls Collecte` #Pour chaque fichier qui se trouve dans collecte
do
cp -p Collecte/$fichier /usr/sbin/$fichier # Copie des elements pour leur installation
echo "rm /usr/sbin/$fichier" >>/usr/sbin/removeGestionSystemeClient.sh #Construction du fichier uninstall
echo "*/1 * * * * root /usr/sbin/$fichier|nc $ip $port">>/etc/crontab #Mettre les taches
done
cp -p Mail/sendmail.py /usr/sbin/sendmail.py  # ajouter le lib sendmail dans les lib de python
for fichier in `ls Crise_Detection` #Pour chaque fichier qui se trouve dans collecte
do
cp -p Crise_Detection/$fichier /usr/sbin/$fichier # Copie des elements pour leur installation dans la machine
echo "rm /usr/sbin/$fichier" >>/usr/sbin/removeGestionSystemeClient.sh #Construction du fichier uninstall
done
#installation du l'affichage
cp -p Affichage/menuClient.py /usr/sbin/GestionSystemeClient # Copie des elements pour leur installation dans la machine
echo "rm /usr/sbin/GestionSystemeClient" >>/usr/sbin/removeGestionSystemeClient.sh #Construction du fichier uninstall
echo "rm /usr/sbin/sendmail.py ">>/usr/sbin/removeGestionSystemeServeur.sh
echo "rm /usr/sbin/sendmail.pyc ">>/usr/sbin/removeGestionSystemeServeur.sh
#Installation des taches 

echo "*/1 * * * * root /usr/sbin/crise.py ">>/etc/crontab #Mettre les taches
echo "cron=\`grep 'nc $ip $port' -v /etc/crontab\`">>/usr/sbin/removeGestionSystemeClient.sh #On supprime les taches creees
echo "echo $cron >/etc/crontab ">>/usr/sbin/removeGestionSystemeClient.sh #Puis on met les nouvelles donnees dans le crontab
echo "cron=\`grep '*/1 * * * * root /usr/sbin/crise.py ' -v /etc/crontab\`">>/usr/sbin/removeGestionSystemeClient.sh #On supprime les taches creees
echo "echo $cron >/etc/crontab ">>/usr/sbin/removeGestionSystemeClient.sh #Puis on met les nouvelles donnees dans le crontab

#Auto destruction du programme charge d'installer le systeme
echo "rm /usr/sbin/removeGestionSystemeClient.sh" >>/usr/sbin/removeGestionSystemeClient.sh

#Donnee le droit a l'application de s'installer lui meme
chmod u+x /usr/sbin/removeGestionSystemeClient.sh
