import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://api.coindesk.com/v1/bpi/currentprice.json" 
response = requests.get(url)
data = response.json()

bitcoin_data = {
    "currency": [key for key in data['bpi'].keys()],
    "rate": [data['bpi'][key]['rate_float'] for key in data['bpi'].keys()],
}

df = pd.DataFrame(bitcoin_data)

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

sns.barplot(x='currency', y='rate', data=df, palette='viridis')

plt.title('Bitcoin Prices by Currency', fontsize=16)
plt.xlabel('Currency', fontsize=12)
plt.ylabel('Price in USD', fontsize=12)

plt.tight_layout()
plt.show()
