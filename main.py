from datetime import date
import matplotlib
import mplcursors as cursors
import yfinance as yf
from matplotlib import pyplot as plt

# download Stock data till date
ticker = input('Stock Name: ')
data = yf.download(ticker, start='2021-01-01', end=date.today())
x = ticker.upper()

# Get Stock chart using pyplot
plt.figure(figsize=(15,5))
plt.plot(data['Close'])
plt.title(f'{x} Stock Price Chart')
plt.xlabel('Date')
plt.ylabel('Price')
cursors.cursor(hover=True)
plt.show()
