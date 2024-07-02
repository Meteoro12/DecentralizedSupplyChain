import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import matplotlib.pyplot as plt

load_dotenv()

DATA_PATH = os.getenv("DATA_PATH", "./data/supply_chain.csv")

def load_data(path):
    try:
        data = pd.read_csv(path)
        print(f"Data loaded successfully from {path}")
        return data
    except FileNotFoundError:
        print(f"File not found at {path}")
        return None

def analyze_efficiency(data):
    if data is None:
        print("No data to analyze.")
        return None
    
    if 'order_date' in data.columns and 'delivery_date' in data.columns:
        data['order_date'] = pd.to_datetime(data['order_date'])
        data['delivery_date'] = pd.to_datetime(data['delivery_date'])
        data['delivery_time'] = (data['delivery_date'] - data['order_date']).dt.days
        
        avg_delivery_time = data['delivery_time'].mean()
        print(f"Average delivery time: {avg_delivery_time} days.")
        
        threshold = avg_delivery_time + data['delivery_time'].std()
        bottlenecks = data[data['delivery_time'] > threshold]
        
        if not bottlenecks.empty:
            print("Potential bottlenecks detected:")
            print(bottlenecks[['order_id', 'delivery_time']])
        else:
            print("No significant bottlenecks detected.")
    else:
        print("Required columns for efficiency analysis are missing.")
        
def generate_report(data):
    if data is None:
        print("No data available for report generation.")
        return None

    print("Generating Supply Chain Report...")
    analyze_efficiency(data)  
    
    print("Report generation complete.")
    
def plot_delivery_times(data):
    if data is None or 'delivery_time' not in data.columns:
        print("Insufficient data for plotting.")
        return
    
    plt.figure(figsize=(10, 6))
    plt.hist(data['delivery_time'], bins=20, alpha=0.75)
    plt.title('Histogram of Delivery Times')
    plt.xlabel('Days')
    plt.ylabel('Frequency')
    plt.show()
    
def main():
    data = load_data(DATA_PATH)
    generate_report(data)
    plot_delivery_times(data)

if __name__ == "__main__":
    main()