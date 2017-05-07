# ! /bin/bash


#
# Installation du Monitoring Cote Serveur
#
#Autheur Omar 
#
#

#Copier les fichier dans /usr/sbin
#Configuration des modules necessaire pour le serveur
./configClient.sh  #Installation du monitoring Client
echo "">/usr/sbin/removeGestionSystemeServeur.sh
for fichier in `ls Serveur`
do
cp -p Serveur/$fichier /usr/sbin/$fichier
echo "rm /usr/sbin/$fichier" >>/usr/sbin/removeGestionSystemeServeur.sh
done

cp -p Mail/sendmail.py /usr/sbin/sendmail.py  # ajouter le lib sendmail dans les lib de python
cp -p Affichage/menuServeur.py /usr/sbin/GestionSystemeMenuServeur #Installation du menu 
cp -p Web/Actualiser_Cert.py /usr/sbin/Actualiser_Cert.py #Installation Actialisation des messages cert
cp -p Web/mail_cert.sh /usr/sbin/mail_cert.sh



echo "*/1 * * * * root /usr/sbin/Actualiser_Cert.py">>/etc/crontab #Mettre la tache actualisation de Cert
echo "cron=\`grep 'Actualiser_Cert.py' -v /etc/crontab\`">>/usr/sbin/removeGestionSystemeServeur.sh #On supprime les taches creees
echo "echo $cron >/etc/crontab ">>/usr/sbin/removeGestionSystemeServeur.sh #Puis on met les nouvelles donnees dans le crontab
echo "rm /usr/sbin/sendmail.py ">>/usr/sbin/removeGestionSystemeServeur.sh
echo "rm /usr/sbin/sendmail.pyc ">>/usr/sbin/removeGestionSystemeServeur.sh
echo "rm /usr/sbin/mail_cert.sh">>/usr/sbin/removeGestionSystemeServeur.sh
echo "rm /usr/sbin/GestionSystemeMenuServeur">>/usr/sbin/removeGestionSystemeServeur.sh
echo "rm -R /etc/GestionSysteme">>/usr/sbin/removeGestionSystemeServeur.sh
echo "rm -R /var/GestionSysteme">>/usr/sbin/removeGestionSystemeServeur.sh
echo "rm /usr/sbin/removeGestionSystemeServeur.sh" >>/usr/sbin/removeGestionSystemeServeur.sh
echo "/usr/sbin/removeGestionSystemeClient.sh" >>/usr/sbin/removeGestionSystemeServeur.sh
mkdir /var/GestionSysteme
./Serveur/creationBD.py
sudo mkdir /etc/GestionSysteme
cp -pR InterfaceWeb /etc/GestionSysteme
sudo chmod u+rwx /usr/sbin/removeGestionSystemeServeur.sh
