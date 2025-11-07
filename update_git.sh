#!/bin/bash

# This script is used to automatically pull files from git and update files on the server

echo "Pulling latest changes..."
sudo git pull

echo "Copying updated files..."
sudo cp apache/index.html /var/www/html/index.html
sudo cp nginx/index.html /var/www/nginx/index.html
sudo cp app.py ~/lemp-app/app.py

echo "Restarting apache"
sudo systemctl restart apache2

echo "Restarting nginx"
sudo systemctl restart nginx

echo "Update complete."
