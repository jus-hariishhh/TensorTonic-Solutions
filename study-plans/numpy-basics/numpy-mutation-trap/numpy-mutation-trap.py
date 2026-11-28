import numpy as np

def original_and_clipped(data: list, row_idx: int, lo: float, hi: float) -> np.ndarray:
    """
    Returns a (2, n) float64 array: original row, then clipped row.
    """
    arr=np.array(data,dtype=np.float64)
    sub=arr[row_idx]
    cond=np.where(sub<lo,lo,sub)
    cond2=np.where(cond>hi,hi,cond)
    return np.stack([sub,cond2],axis=0)
    pass
