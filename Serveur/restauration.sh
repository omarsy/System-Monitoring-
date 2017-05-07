#!/bin/sh
echo "Entrez le chemin pour le restauration : "
read support
cd /
tar -xvzf $support var/GestionSysteme/service.db

