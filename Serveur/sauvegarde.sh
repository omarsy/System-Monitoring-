#!/bin/sh

echo "Entrez le chemin ou gaire le backup (chemin absolu) : "
read support

tar -cvzf $support /var/GestionSysteme/service.db




