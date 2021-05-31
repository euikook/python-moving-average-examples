import numpy as np

import pandas as pd

import matplotlib.dates as mdates

from avgutils import do_cma, do_sma, do_ema, do_wma

from matplotlib import rcParams
rcParams['font.family'] = 'monospace'
rcParams['font.sans-serif'] = ['Tahoma']
import matplotlib.pyplot as plt

N = 15

from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

all_frames = pd.read_csv('data.csv')

df = all_frames.tail(365)

# df = all_frames

date = pd.to_datetime(df.Date)
high = df.High 
low  = df.Low
price = df.Close

cma = do_cma(price)
sma = do_sma(price, N=N)
ema = do_ema(price, N=N)
wma = do_wma(price, N=N)



ax = pd.DataFrame({
    'Date': date, 
    'Price': price, 
    'CMA': cma, 
    'SMA': sma,
    'WMA': wma, 
    'EMA': ema
    }).plot(x='Date', kind='line', figsize=(16, 9))

fmt_month = mdates.MonthLocator()
ax.xaxis.set_minor_locator(fmt_month)
# Text in the x axis will be displayed in 'YYYY-mm' format.
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.legend(labels=[
    'Closing Price', 
    'Cumulative Moving Average',
    'Simple Moving Average',
    'Weighted Moving Average',
    'Exponential Moving Average',
    ], fontsize=12)


plt.xlim(date.iat[0], date.iat[-1])

plt.title(f'Moving Average(N={N})', fontsize=14)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig('all.svg', format='svg')
