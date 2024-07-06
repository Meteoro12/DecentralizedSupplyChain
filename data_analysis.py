import os
import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt

try:
    load_dotenv()
except Exception as e:
    print(f"Error loading environment variables: {e}")

def get_data_path():
    try:
        DATA_PATH = os.getenv("DATA_PATH", "./data/supply_chain.csv")
        if not os.path.exists(DATA_PATH):
            raise FileNotFoundError(f"Configured data path does not exist: {DATA_PATH}")
        return DATA_PATH
    except Exception as e:
        print(f"Error getting data path: {e}")
        return None

def load_data(path):
    if path is None:
        print("No valid path provided for data loading.")
        return None
    try:
        data = pd.read_csv(path)
        print(f"Data loaded successfully from {path}")
        return data
    except FileNotFoundError:
        print(f"File not found at {path}")
    except pd.errors.EmptyDataError:
        print(f"No data: File at {path} is empty.")
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
    return None

def analyze_efficiency(data):
    if data is None:
        print("No data to analyze.")
        return
    if 'order_date' not in data.columns or 'delivery_date' not in data.columns:
        print("Required columns for efficiency analysis are missing.")
        return
    try:
        data['order_date'] = pd.to_datetime(data['order_date'])
        data['delivery_date'] = pd.to_datetime(data['delivery_date'])
    except Exception as e:
        print(f"Error processing date columns: {e}")
        return
    try:
        data['delivery_time'] = (data['delivery_date'] - data['order_date']).dt.days
        avg_delivery_time = data['delivery_time'].mean()
        print(f"Average delivery time: {avg_delivery_time:.2f} days.")
        threshold = avg_delivery_time + data['delivery_time'].std()
        bottlenecks = data[data['delivery_time'] > threshold]
        if bottlenecks.empty:
            print("No significant bottlenecks detected.")
        else:
            print("Potential bottlenecks detected:")
            print(bottlenecks[['order_id', 'delivery_time']])
    except Exception as e:
        print(f"An error occurred during efficiency analysis: {e}")

def generate_report(data):
    if data is None:
        print("No data available for report generation.")
        return
    print("Generating Supply Chain Report...")
    analyze_efficiency(data)  
    print("Report generation complete.")

def plot_delivery_times(data):
    if data is None or 'delivery_time' not in data.columns:
        print("Insufficent data for plotting.")
        return 
    try:
        plt.figure(figsize=(10, 6))
        plt.hist(data['delivery_time'], bins=20, alpha=0.75)
        plt.title('Histogram of Delivery Times')
        plt.xlabel('Days')
        plt.ylabel('Frequency')
        plt.show()
    except Exception as e:
        print(f"An error occurred while plotting data: {e}")

def main():
    DATA_PATH = get_data_path()
    data = load.0(`data(DATA_PATH)
    generate_report(data)
    plot_delivery_times(data)

if __name__ == "__main__":
    main()