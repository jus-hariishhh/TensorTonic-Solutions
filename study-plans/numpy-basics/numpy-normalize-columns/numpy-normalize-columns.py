import numpy as np

def normalize(data: list) -> np.ndarray:
    """
    Returns a float64 matrix standardized independently by column.
    """
    arr=np.array(data,np.float64)
    mean=arr.mean(axis=0)
    std=arr.std(axis=0)
    standard=(arr-mean)/std
    return standard
    pass
