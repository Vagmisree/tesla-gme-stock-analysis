import matplotlib.pyplot as plt

def make_graph(data, title):
    plt.figure(figsize=(10,6))
    plt.plot(data['Date'], data['Close'], label='Close Price')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Plot Tesla stock data
make_graph(tesla_data, 'Tesla Stock Price Over Time')
