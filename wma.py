import numpy as np

import pandas as pd

import matplotlib.dates as mdates

from avg import do_cma, do_sma, do_ema, do_wma

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

wma15 = do_wma(price, N=N)
wma30 = do_wma(price, N=30)
wma60 = do_wma(price, N=60)
wma90 = do_wma(price, N=90)
wma120 = do_wma(price, N=120)



ax = pd.DataFrame({
    'Date': date, 
    'Price': price, 
    'WMA-15': wma15, 
    'WMA-30': wma30,
    'WMA-60': wma60, 
    'WMA-90': wma90,
    'WMA-120': wma120
    }).plot(x='Date', kind='line', figsize=(16, 9))

fmt_month = mdates.MonthLocator()
ax.xaxis.set_minor_locator(fmt_month)
# Text in the x axis will be displayed in 'YYYY-mm' format.
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.legend(labels=[
    'Closing Price', 
    'Weighted Moving Average(N=15)',
    'Weighted Moving Average(N=30)',
    'Weighted Moving Average(N=60)',
    'Weighted Moving Average(N=90)',
    'Weighted Moving Average(N=120)'
    ], fontsize=12)


plt.xlim(date.iat[0], date.iat[-1])

plt.title(f'Moving Average(N={N})', fontsize=14)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig('images/wma.svg', format='svg')
