import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fetch data from public API (for this example, let's use a JSON API)
url = "https://api.coindesk.com/v1/bpi/currentprice.json"  # Example: Bitcoin Price Index API
response = requests.get(url)
data = response.json()

# Extract relevant data
bitcoin_data = {
    "currency": [key for key in data['bpi'].keys()],
    "rate": [data['bpi'][key]['rate_float'] for key in data['bpi'].keys()],
}

# Create a DataFrame
df = pd.DataFrame(bitcoin_data)

# Data Visualization using seaborn and matplotlib
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

# Create a barplot
sns.barplot(x='currency', y='rate', data=df, palette='viridis')

# Title and labels
plt.title('Bitcoin Prices by Currency', fontsize=16)
plt.xlabel('Currency', fontsize=12)
plt.ylabel('Price in USD', fontsize=12)

# Show plot
plt.tight_layout()
plt.show()
