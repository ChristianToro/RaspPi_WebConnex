#!/bin/bash

# Update & install dependencies
sudo apt update
sudo apt install -y python3-pip git
pip3 install speedtest-cli gspread oauth2client

# Create monitoring script directory
mkdir -p /home/pi/internet_monitor
cd /home/pi/internet_monitor

# Download Python script
wget -O internet_monitor.py https://your-download-url-or-copy-manually

# Move your credentials JSON into place
# (Assume you manually copy it into /home/pi/internet_monitor/credentials.json)

# Make CSV file if it doesn't exist
touch /home/pi/internet_log.csv

# Set up cron job (every 30 mins)
(crontab -l ; echo "*/30 * * * * /usr/bin/python3 /home/pi/internet_monitor/internet_monitor.py") | crontab -

echo "Setup complete. Script will run every 30 minutes."
