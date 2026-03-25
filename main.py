import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load dataset
data = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Clean column names
data.columns = data.columns.str.strip()

# Convert Order Date to datetime
data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')

# Drop invalid dates
data = data.dropna(subset=['Order Date'])

# Sort values
data = data.sort_values('Order Date')

# Set Order Date as index
data.set_index('Order Date', inplace=True)

# Resample monthly sales
sales = data['Sales'].resample('ME').sum().reset_index()

# Create numeric time column
sales['Months'] = range(len(sales))

# Features and target
X = sales[['Months']]
y = sales['Sales']

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next 12 months
future_days = np.arange(sales['Months'].max(), sales['Months'].max() + 12).reshape(-1,1)
future_sales = model.predict(future_days)

# Create future dates
future_dates = pd.date_range(start=sales['Order Date'].max(), periods=12, freq='ME')

# Plot
plt.figure()

plt.plot(sales['Order Date'], y, marker='o', label='Actual Sales')
plt.plot(future_dates, future_sales, marker='o', linestyle='dashed', label='Predicted Sales')

plt.title("Sales Forecast (Monthly)")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid()

plt.show()

# Save output
future_df = pd.DataFrame({
    'Date': future_dates,
    'Predicted Sales': future_sales
})

future_df.to_csv("forecast_output.csv", index=False)

print("Forecast saved as forecast_output.csv")
# Category-wise sales
category_sales = data.reset_index().groupby('Category')['Sales'].sum()

print("\nCategory-wise Sales:\n", category_sales)

# Plot
plt.figure()
category_sales.plot(kind='bar')

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()
# Region-wise sales
# Region-wise sales (FIXED)
# Region-wise sales (FIXED)

data_reset = data.reset_index()   # 🔥 ADD THIS LINE

data_reset.columns = data_reset.columns.str.strip()

print("\nColumns available:", data_reset.columns)

region_sales = data_reset.groupby('Region')['Sales'].sum()

print("\nRegion-wise Sales:\n", region_sales)

plt.figure()
region_sales.plot(kind='bar')

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.show()

# Top 10 products
top_products = data.reset_index().groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products:\n", top_products)

plt.figure()
top_products.plot(kind='bar')

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=75)

plt.show()
