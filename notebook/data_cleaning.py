import pandas as pd

# Load raw data
df = pd.read_csv("../data/sales_data.csv")

# Basic cleaning
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df.dropna(subset=['date', 'product', 'quantity', 'unit_price'], inplace=True)
df = df[df['quantity'] > 0]
df['revenue'] = df['quantity'] * df['unit_price']

# Save clean dataset
df.to_csv("../data/clean_sales_data.csv", index=False)

print("✅ Data cleaned and saved as clean_sales_data.csv")
print(df.head())

