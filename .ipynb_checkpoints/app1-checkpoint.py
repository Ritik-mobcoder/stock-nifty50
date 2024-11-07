import yfinance as yf

# Download stock data for Infosys
ticker = "INFY.NS"
data = yf.download(ticker, start="2010-01-01", end="2023-01-01")

# Add a new column with the ticker symbol at the end
data['Symbol'] = ticker
print(data)