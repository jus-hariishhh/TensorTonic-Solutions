import numpy as np

def scale_cols(data: list, weights: list) -> np.ndarray:
    """
    Returns a float64 matrix with each column multiplied by its weight.
    """
    arr1=np.array(data,dtype=np.float64)
    arr2=np.array(weights,dtype=np.float64)
    arr_new=arr1*arr2[None,:]
    return arr_new
    pass
