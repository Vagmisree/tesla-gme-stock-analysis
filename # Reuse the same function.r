# Reuse the same function
def make_graph(data, title):
    plt.figure(figsize=(10,6))
    plt.plot(data['Date'], data['Close'], label='Close Price', color='orange')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Plot GameStop stock data
make_graph(gme_data, 'GameStop Stock Price Over Time')

