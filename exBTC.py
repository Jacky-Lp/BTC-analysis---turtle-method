import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('BTC-EUR.csv', index_col='Date', parse_dates=True)
data['Buy'] = np.zeros(len(data))
data['Sell'] = np.zeros(len(data))

data['Rolling MAX'] = data['Close'].shift(1).rolling(window=28).max()
data['Rolling MIN'] = data['Close'].shift(1).rolling(window=28).min()
data['Buy'][data['Rolling MAX'] < data['Close']] = 1
data['Sell'][data['Rolling MIN'] > data['Close']] = -1

start = '2023-01-01'
end = '2023-11-01'
fig, ax = plt.subplots(2, figsize=(16, 9), sharex=True)
ax[0].plot(data['Close'][start:end], label='Close')
ax[0].plot(data['Rolling MIN'][start:end], label='Rolling MIN')
ax[0].plot(data['Rolling MAX'][start:end], label='Rolling MAX')
ax[0].legend()

ax[1].plot(data['Buy'][start:end], c='green', label='Buy')
ax[1].plot(data['Sell'][start:end], c='red', label='Sell')
ax[1].legend()

plt.show()
