import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    """
    Returns a float64 array of shape (3, m, n): mask, any-row, all-row.
    """
    arr=np.array(data, dtype=np.float64)
    row=np.where(arr>threshold,1,0)
    any=np.any(arr>threshold,axis=1)[:, None]
    any_row=np.where(any,arr,0)
    all=np.all(arr>threshold,axis=1)[:, None]
    all_row=np.where(all,arr,0)
    return np.stack([row, any_row, all_row],axis=0)
    pass
