import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('ecommerce_data.csv')

# Product-wise quantity sold
product_sales = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,4))
product_sales.plot(kind='bar', color='skyblue')
plt.title('Top-Selling Products')
plt.ylabel('Total Quantity Sold')
plt.tight_layout()
plt.savefig('product_sales.png')
plt.show()

# Peak Order Times
df['OrderHour'] = pd.to_datetime(df['OrderTime'], format='%H:%M').dt.hour
hourly_orders = df['OrderHour'].value_counts().sort_index()

plt.figure(figsize=(8,4))
hourly_orders.plot(kind='line', marker='o', color='orange')
plt.title('Order Frequency by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Orders')
plt.grid(True)
plt.tight_layout()
plt.savefig('peak_hours.png')
plt.show()

# Average rating per product
avg_rating = df.groupby('Product')['Rating'].mean()
print("\nAverage Rating per Product:\n", avg_rating)
