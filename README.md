
# Raspberry Pi Internet Monitor

This project uses a Raspberry Pi 4B to track and log internet connectivity statistics including:
- Ping
- Download speed
- Upload speed
- Packet loss

These metrics are logged to a CSV file and synced to a Google Sheets document for visualization and tracking.

---

## Features

- 🌐 **Speed Test**: Measures ping, download, and upload speeds using `speedtest-cli`.
- 📉 **Packet Loss**: Pings Google's DNS server to calculate packet loss.
- 📄 **Logging**: Saves all results to a local CSV file.
- ☁️ **Google Sheets Sync**: Automatically updates a Google Sheet with the latest data.
- 🕒 **Automation**: Uses a cron job to run every 30 minutes.

---

## Prerequisites

- Raspberry Pi 4B (1 GB RAM minimum)
- Python 3 installed
- Google Cloud Project with Sheets and Drive APIs enabled
- A valid `credentials.json` file from Google Cloud

---

## Installation

1. **Clone the repo**
```bash
git clone https://github.com/ChristianToro/RaspPi_WebConnex.git
cd RaspPi_WebConnex
```

2. **Install dependencies**
```bash
sudo apt update
sudo apt install -y python3-pip git
pip3 install speedtest-cli gspread oauth2client
```

3. **Place your credentials**
Place your `credentials.json` file in:
```
/home/pi/internet_monitor/credentials.json
```

4. **Set up cron job**
The provided bash script adds a cron job that runs the monitor every 30 minutes.

```bash
chmod +x setup_monitoring.sh
./setup_monitoring.sh
```

---

## How It Works

Each run of the script performs the following:
1. Runs a speed test (ping, download, upload)
2. Pings `8.8.8.8` to calculate packet loss
3. Appends results to a local CSV
4. Syncs the CSV to a Google Sheet

---

## File Structure

```
internet_monitor/
├── internet_monitor.py       # Main monitoring script
├── setup_monitoring.sh       # Setup script for automation
├── credentials.json          # Google Sheets API credentials
├── internet_log.csv          # Local CSV log file
└── SETUP_GOOGLE_API_CREDENTIALS.txt  # Setup instructions for Google API
```

---

## Visualization

For visualizing data, you can:
- Connect the Google Sheet to Google Data Studio
- Import the CSV to Grafana using the CSV data source plugin
- Export CSVs for use in other platforms

---

## License

This project is licensed under the MIT License.

---

## Author

Created by [Christian Toro](https://github.com/ChristianToro). Contributions welcome!
