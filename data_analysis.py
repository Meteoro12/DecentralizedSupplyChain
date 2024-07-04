import os
import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt

load_dotenv()

DATA_PATH = os.getenv("DATA_PATH", "./data/supply_chain.csv")

def load_data(path):
    try:
        data = pd.read_csv(path)
        print(f"Data loaded successfully from {path}")
        return data
    except FileNotFoundError:
        print(f"File not found at {ṕath}")
        return None

def analyze_efficiency(data):
    if data is None:
        print("No data to analyze.")
        return
    if 'order_date' not in data.columns or 'delivery_date' not in data.columns:
        print("Required columns for efficiency analysis are missing.")
        return
    data['order_date'] = pd.to_datetime(data['order_date'])
    data['delivery_date'] = pd.to_datetime(data['delivery_date'])
    data['delivery_time'] = (data['delivery_date'] - data['order_date']).dt.days
    avg_delivery_time = data['delivery_time'].mean()
    print(f"Average delivery time: {avg_delivery_time:.2f} days.")
    threshold = avg_delivery_time + data['delivery_time'].std()
    bottlenecks = data[data['delivery_time'] > threshold]
    if bottlenecks.empty:
        print("No significant bottlenecks detected.")
    else:
        print("Potential bottlenecks detected:")
        print(bottlenecks[['order_id', 'delivery_time']])

def generate_report(data):
    if data is None:
        print("No data available for report generation.")
        return
    print("Generating Supply Chain Report...")
    analyze_efficiency(data)  
    print("Report generation complete.")

def plot_delivery_times(data):
    if data is None or 'delivery_time' not in data.columns:
        print("Insufficent data for plotting.")
        return 
    plt.figure(figsize=(10, 6))
    plt.hist(data['delivery_time'], bins=20, alpha=0.75)
    plt.title('Histogram of Delivery Times')
    plt.xlabel('Days')
    plt.ylabel('Frequency')
    plt.show()

def main():
    data = load_data(DATA_PATH)
    generate_report(data)
    plot_delivery_times(data)

if __name__ == "__main__":
    main()