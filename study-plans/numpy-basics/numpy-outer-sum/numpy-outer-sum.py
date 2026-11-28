import numpy as np

def outer_sum(a: list, b: list) -> np.ndarray:
    """
    Returns an (m, n) float64 array of pairwise sums.
    """
    arr1=np.array(a,dtype=np.float64)
    arr2=np.array(b,dtype=np.float64)
    return np.add.outer(arr1,arr2)
    pass
