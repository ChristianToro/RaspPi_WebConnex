import csv
import os
import random
import datetime

# File path
csv_file = os.path.join(os.path.dirname(__file__), 'internet_log.csv')

# Generate sample data
def generate_sample_data(num_samples=100):
    # Create header and data rows
    header = ['Timestamp', 'Ping (ms)', 'Download (Mbps)', 'Upload (Mbps)', 'Packet Loss (%)']
    data = []

    # Start time (24 hours ago)
    start_time = datetime.datetime.now() - datetime.timedelta(days=1)

    # Generate data points
    for i in range(num_samples):
        # Create timestamp with even intervals
        timestamp = start_time + datetime.timedelta(minutes=i*15)

        # Generate realistic values with some variation
        ping = round(random.uniform(20, 100), 2)
        download = round(random.uniform(50, 150), 2)
        upload = round(random.uniform(5, 20), 2)

        # Occasionally add packet loss
        packet_loss = 0.0
        if random.random() < 0.2:  # 20% chance of packet loss
            packet_loss = round(random.uniform(0.1, 5.0), 2)

        # Add some correlated degradation (when ping is high, speeds are lower)
        if ping > 70:
            download = round(download * 0.7, 2)
            upload = round(upload * 0.7, 2)

        data.append([timestamp.isoformat(), ping, download, upload, packet_loss])

    return header, data

# Write to CSV
def write_to_csv(header, data):
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    print(f"Generated {len(data)} sample data points in {csv_file}")

if __name__ == "__main__":
    header, data = generate_sample_data(100)
    write_to_csv(header, data)