import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime

# Load data from CSV
def load_data():
    csv_path = os.path.join(os.path.dirname(__file__), 'internet_log.csv')
    df = pd.read_csv(csv_path)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df

def create_graphs():
    # Load and prepare data
    df = load_data()

    # Create figure with subplots
    fig, axs = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
    fig.suptitle('Internet Connection Monitoring Results', fontsize=16)

    # Speed plot (download and upload)
    axs[0].plot(df['Timestamp'], df['Download (Mbps)'], 'b-', label='Download')
    axs[0].plot(df['Timestamp'], df['Upload (Mbps)'], 'g-', label='Upload')
    axs[0].set_ylabel('Speed (Mbps)')
    axs[0].legend()
    axs[0].grid(True)

    # Ping plot
    axs[1].plot(df['Timestamp'], df['Ping (ms)'], 'r-')
    axs[1].set_ylabel('Ping (ms)')
    axs[1].grid(True)

    # Packet loss plot
    axs[2].plot(df['Timestamp'], df['Packet Loss (%)'], 'k-')
    axs[2].set_ylabel('Packet Loss (%)')
    axs[2].set_xlabel('Time')
    axs[2].grid(True)

    # Format x-axis to show dates nicely
    plt.xticks(rotation=45)
    fig.tight_layout()

    # Save the figure
    plt.savefig(os.path.join(os.path.dirname(__file__), 'internet_stats.png'))
    print("Graph saved as 'internet_stats.png'")

    # Show the plot
    plt.show()

if __name__ == "__main__":
    create_graphs()