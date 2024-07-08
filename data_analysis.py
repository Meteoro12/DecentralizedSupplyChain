import os
import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt

try:
    load_dotenv()
except Exception as error:
    print(f"Error loading environment variables: {error}")

def get_supply_chain_data_path():
    try:
        data_path = os.getenv("DATA_PATH", "./data/supply_chain.csv")
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Configured data path does not exist: {data_path}")
        return data_path
    except Exception as error:
        print(f"Error identifying data path: {error}")
        return None

def load_supply_chain_data(path):
    if path is None:
        print("No valid path provided for data extraction.")
        return None
    try:
        supply_chain_data = pd.read_csv(path)
        print(f"Supply Chain Data successfully retrieved from {path}")
        return supply_chain_data
    except FileNotFoundError:
        print(f"Data file not found at {path}")
    except pd.errors.EmptyDataError:
        print(f"No data available: File at {path} is empty.")
    except Exception as error:
        print(f"Unexpected error during data loading: {error}")
    return None

def analyze_supply_chain_eff Federicicency(supply_chain_data):
    if supply_chain_data is None:
        print("Missing data for efficiency analysis.")
        return
    required_columns = {'order_date', 'delivery_date'}
    if not required_columns.issubset(supply_chain_data.columns):
        print("Essential columns for efficiency analysis are missing.")
        return
    try:
        supply_chain_data['order_date'] = pd.to_datetime(supply_chain_data['order_date'])
        supply_chain_data['delivery_date'] = pd.to_datetime(supply_chain_data['delivery_date'])
    except Exception as error:
        print(f"Error converting date columns: {error}")
        return
    try:
        supply_chain_data['delivery_duration'] = (supply_chain_data['delivery_date'] - supply_chain_data['order_date']).dt.days
        mean_delivery_duration = supply_chain_data['delivery_duration'].mean()
        print(f"Mean Delivery Duration: {mean_delivery_duration:.2f} days.")
        delivery_duration_threshold = mean_delivery_duration + supply_chain_data['delivery_duration'].std()
        potential_bottlenecks = supply_chain_data[supply_chain_data['delivery_duration'] > delivery_duration_threshold]
        if potential_bottlenecks.empty:
            print("No significant efficiency bottlenecks found.")
        else:
            print("Detected potential efficiency bottlenecks:")
            print(potential_bottlenecks[['order_id', 'delivery_duration']])
    except Exception as error:
        print(f"Error during efficiency analysis: {error}")

def generate_efficiency_report(supply_chain_data):
    if supply_chain_data is None:
        print("Unavailable data for report generation.")
        return
    print("Commencing Supply Chain Efficiency Report Generation...")
    analyze_supply_chain_efficiency(supply_chain_data)  
    print("Efficiency Report generated successfully.")

def visualize_delivery_durations(supply_chain_data):
    if supply_chain_data is None or 'delivery_duration' not in supply_chain_data.columns:
        print("Insufficient data for visualization.")
        return 
    try:
        plt.figure(figsize=(10, 6))
        plt.hist(supply_chain_data['delivery_duration'], bins=20, alpha=0.75)
        plt.title('Histogram of Delivery Durations')
        plt.xlabel('Days')
        plt.ylabel('Frequency')
        plt.show()
    except Exception as error:
        print(f"Error during delivery duration visualization: {error}")

def main():
    supply_chain_data_path = get_supply_chain_data_path()
    supply_chain_data = load_supply_chain_data(supply_chain_data_path)
    generate_efficiency_report(supply_chain_data)
    visualize_delivery_durations(supply_chain_data)

if __name__ == "__main__":
    main()