import numpy as np

def norm_diff(a: list, b: list, lo: float, hi: float) -> np.ndarray:
    """
    Returns a float64 array of absolute normalized differences.
    """
    arr1=np.array(a,dtype=np.float64)
    arr2=np.array(b,dtype=np.float64)
    arr1_clip=np.clip(arr1,lo,hi)
    arr2_clip=np.clip(arr2,lo,hi)
    arr_new=np.abs(arr1_clip-arr2_clip)
    return arr_new/(hi-lo)
    pass
