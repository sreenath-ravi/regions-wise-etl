import pandas as pd

def extract_data(file_path):
    try:      
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None