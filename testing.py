# Try default UTF-8 first
destination = 'downloaded_file.csv'
import pandas as pd
try:
    df = pd.read_csv(destination)
except UnicodeDecodeError:
    # If encoding fails, try a more lenient encoding
    df = pd.read_csv(destination, encoding="latin1")

print(df.head())