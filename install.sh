#!/bin/bash

# This script is used to automatically pull files from git and update files on the server

echo "Pulling latest changes..."
sudo git pull

echo "Copying updated files..."
sudo cp apache/index.html /var/www/html/index.html
sudo cp nginx/index.html /var/www/nginx/index.html

sudo cp lemp-app/app.py ~/lemp-app/app.py
sudo cp -ra lemp-app/templates/ ~/lemp-app/
sudo cp lemp-app_config/lemp-app.service /etc/systemd/system/lemp-app.service

sudo cp streamlit-app/streamlit_app.py ~/streamlit-app/streamlit_app.py
sudo cp streamlit-app/pages/ ~/streamlit-app/
sudo cp streamlit-app/config.toml ~/streamlit-app/.streamlit/config.toml
sudo cp streamlit-app/streamlit.service /etc/systemd/system/streamlit.service

sudo cp cron_API/fetch_weather.py ~/cron_api/fetch_weather.py
sudo cp cron_API/fetch_weather.sh ~/cron_api/fetch_weather.sh

#Apache server no longer in use
#echo "Restarting apache"
#sudo systemctl restart apache2

echo "Restarting nginx"
sudo cp nginx/nginx_config /etc/nginx/sites-available/nginx_config
sudo systemctl restart nginx

echo "Restart lemp-app"
sudo systemctl daemon-reload
sudo systemctl restart lemp-app

echo "Update complete."
