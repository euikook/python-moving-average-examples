import numpy as np

import pandas as pd

from matplotlib import rcParams
rcParams['font.family'] = 'monospace'
rcParams['font.sans-serif'] = ['Tahoma']
import matplotlib.pyplot as plt

from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


# smoothing factor and number of data points
N = 15
ALPHA = 2/(N+1)

NUM_X = N * 4

# simple moving average
sma = [0 if i > N else 1/N for i in range(NUM_X)]

# weighted moving average
wma =  [0 if i > N else (N - i)/(N * (N + 1) / 2) for i in range(NUM_X)]

# exponential moving average alpha=2/(N+1)
ema = [ALPHA*(1-ALPHA)**i for i in range(NUM_X)]

# store the values in a data frame 
pd.DataFrame({'sma': sma, 'wma': wma, 'ema': ema}).plot(kind='bar', figsize=(16,9))

plt.xticks(np.arange(0, NUM_X, 5), rotation=0)
plt.yticks(fontsize=10)

plt.legend(labels=[
    'SMA', 
    'WMA',
    'EMA, α=2/(N+1)'
    ], fontsize=12)

# title and labels
plt.title(f'Weights of Moving Average(N={N})', fontsize=14)
plt.ylabel('Weights', fontsize=12)
plt.xlabel('n-th Most Recent Smple', fontsize=12)
plt.tight_layout()

# plt.savefig('weight.svg', format='svg')
plt.show()

