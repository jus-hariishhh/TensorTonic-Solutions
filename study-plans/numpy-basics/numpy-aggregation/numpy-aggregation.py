import numpy as np

def summarize(data: list, axis: int) -> np.ndarray:
    """
    Returns float64 rows of mean, standard deviation, minimum, and maximum.
    """
    arr=np.array(data,dtype=np.float64)
    arr1=np.mean(arr, axis=axis)
    arr2=np.std(arr, axis=axis)
    arr3=np.min(arr, axis=axis)
    arr4=np.max(arr, axis=axis)
    return np.stack([arr1,arr2,arr3,arr4], axis=0)
    pass
