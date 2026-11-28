import numpy as np

def sort_with_indices(data: list, axis: int) -> np.ndarray:
    """
    Returns a (2, m, n) float64 array of sorted values and source indices.
    """
    arr=np.array(data,dtype=np.float64)
    a=np.argsort(arr,axis=axis)
    b=np.take_along_axis(arr,a,axis=axis)
    return np.stack([b,a],axis=0)
    pass
