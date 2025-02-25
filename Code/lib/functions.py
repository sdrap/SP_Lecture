import numpy as np
from scipy.stats import norm

# random walk

def random_walk(T, paths = 1, start = 100, p = 0.5, seed = None):
    rng = np.random.default_rng(seed)
    x = np.zeros((T+1, paths))
    x[0, :] = start
    cointoss = rng.choice([-1, 1], size=(T, paths), p=[1-p, p])
    cointoss = cointoss.cumsum(axis=0)
    x[1:, :] = cointoss + start
    return x.squeeze()

def geom_walk(T, paths = 1, start = 100, p=0.5, u = 0.1, d = -0.1, seed = None):
    rng = np.random.default_rng(seed)
    x = np.zeros((T+1, paths))
    x[0, :] = start
    cointoss = rng.choice([u, d], size=(T, paths), p=[p, 1-p])
    cointoss = (1+cointoss).cumprod(axis=0)
    x[1:, :] = cointoss * start
    return x.squeeze()



__all__ = [
    "random_walk",
    "geom_walk",
]