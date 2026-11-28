import numpy as np

def row_extremes(data: list) -> np.ndarray:
    """
    Returns float64 rows of maxima, maximum indices, minima, and minimum indices.
    """
    arr=np.array(data,dtype=np.float64)
    a=arr.min(axis=1)
    a1=arr.argmin(axis=1)
    b=arr.max(axis=1)
    b1=arr.argmax(axis=1)
    return np.stack([b,b1,a,a1])
    pass
