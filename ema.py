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

ema15 = do_ema(price, N=N)
ema30 = do_ema(price, N=30)
ema60 = do_ema(price, N=60)
ema90 = do_ema(price, N=90)
ema120 = do_ema(price, N=120)



ax = pd.DataFrame({
    'Date': date, 
    'Price': price, 
    'EMA-15': ema15, 
    'EMA-30': ema30,
    'EMA-60': ema60, 
    'EMA-90': ema90,
    'EMA-120': ema120
    }).plot(x='Date', kind='line', figsize=(16, 9))

fmt_month = mdates.MonthLocator()
ax.xaxis.set_minor_locator(fmt_month)
# Text in the x axis will be displayed in 'YYYY-mm' format.
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.legend(labels=[
    'Closing Price', 
    'Exponential Moving Average(N=15)',
    'Exponential Moving Average(N=30)',
    'Exponential Moving Average(N=60)',
    'Exponential Moving Average(N=90)',
    'Exponential Moving Average(N=120)'
    ], fontsize=12)


plt.xlim(date.iat[0], date.iat[-1])

plt.title(f'Moving Average(N={N})', fontsize=14)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig('ema.svg', format='svg')
