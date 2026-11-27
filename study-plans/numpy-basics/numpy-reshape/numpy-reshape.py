import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    a=np.array(data,dtype=np.float64)
    if operation=="flatten":
        a=a.flatten()
        return a
    elif operation=="transpose":
        a=a.T
        return a
    else:
        a=np.expand_dims(a,axis=0)
        return a
    pass
