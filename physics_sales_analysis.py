# 1. Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load Data
df = pd.read_csv('../data/sales_data.csv')  # Adjust the path if needed
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 3. Resampling
weekly_sales = df['Sales'].resample('W').sum()
monthly_avg = df['Sales'].resample('M').mean()

# 4. Plotting
plt.style.use('dark_background')
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# 4.1 Daily vs Weekly Sales
ax[0].plot(df.index, df['Sales'], label='Daily Sales', color='cyan', alpha=0.5)
ax[0].plot(weekly_sales.index, weekly_sales, label='Weekly Sales (Sum)', color='yellow', linewidth=2)
ax[0].set_title('Sales Resampling: Daily vs Weekly', fontsize=14, weight='bold', color='gold')
ax[0].legend()
ax[0].set_ylabel('Sales')

# 4.2 Monthly Average Sales
ax[1].bar(monthly_avg.index.strftime('%b'), monthly_avg, color='orange', edgecolor='white')
ax[1].set_title('Monthly Average Sales', fontsize=14, weight='bold', color='gold')
ax[1].set_ylabel('Avg Sales')

plt.tight_layout()
plt.show()
