import numpy as np


def do_cma(s):
    return s.expanding().mean()

def do_sma(s, N=15):
    return s.rolling(N, min_periods=1).mean()

def do_ema(s, N=15):
    return s.ewm(alpha=2/(N+1)).mean()


w = lambda x: np.arange(1, len(x) + 1)
def do_wma(s, N=15):
    # w = np.arange(1, N + 1)
    return s.rolling(N, min_periods=2).apply(lambda x: np.dot(x, w(x))/w(x).sum(), raw=True)
