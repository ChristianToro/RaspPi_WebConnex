import speedtest
import subprocess
import datetime
import csv
import os
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# CONFIG
CSV_FILE = 'internet_log.csv'
# CREDS_FILE = '/home/pi/credentials.json'  # Your Google API JSON credentials
SPREADSHEET_NAME = 'Internet Stats'
HOST_TO_PING = '8.8.8.8'
PACKET_COUNT = 10

# Run speed test
def run_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()
    ping = st.results.ping
    download = st.download() / 1_000_000  # Convert to Mbps
    upload = st.upload() / 1_000_000
    return round(ping, 2), round(download, 2), round(upload, 2)

# Check packet loss
def get_packet_loss(host=HOST_TO_PING, count=PACKET_COUNT):
    try:
        result = subprocess.run(["ping", "-c", str(count), host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in result.stdout.splitlines():
            if "packet loss" in line:
                loss_percent = float(line.split(',')[2].strip().split('%')[0])
                return round(loss_percent, 2)
    except Exception as e:
        print("Error checking packet loss:", e)
    return 100.0

# Log to CSV
def log_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Timestamp', 'Ping (ms)', 'Download (Mbps)', 'Upload (Mbps)', 'Packet Loss (%)'])
        writer.writerow(data)

# Sync CSV to Google Sheets
# def sync_to_google_sheets():
#     scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#     creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, scope)
#     client = gspread.authorize(creds)
    
#     try:
#         sheet = client.open(SPREADSHEET_NAME).sheet1
#     except gspread.exceptions.SpreadsheetNotFound:
#         sheet = client.create(SPREADSHEET_NAME).sheet1
    
#     sheet.clear()
#     with open(CSV_FILE, 'r') as f:
#         content = list(csv.reader(f))
#         sheet.update('A1', content)

def main():
    timestamp = datetime.datetime.now().isoformat()
    ping, download, upload = run_speedtest()
    packet_loss = get_packet_loss()
    
    data = [timestamp, ping, download, upload, packet_loss]
    print("Logging:", data)
    
    log_to_csv(data)
    # sync_to_google_sheets()

if __name__ == '__main__':
    main()
