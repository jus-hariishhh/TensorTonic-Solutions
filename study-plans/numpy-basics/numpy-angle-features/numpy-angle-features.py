import numpy as np

def angle_features(angles: list) -> np.ndarray:
    """
    Returns a (3, n) float64 array with sine, cosine, and tangent rows.
    """
    arr=np.array(angles)
    sin=np.sin(arr)
    cos=np.cos(arr)
    tan=np.tan(arr)
    arr_new=np.stack([sin,cos,tan],axis=0)
    return arr_new
    pass
