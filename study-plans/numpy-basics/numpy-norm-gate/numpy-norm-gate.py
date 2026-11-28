import numpy as np

def norm_gate(X: list, W: list, threshold: float) -> np.ndarray:
    """
    Returns an (n, k) float64 matrix of norm-gated transformed rows.
    """
    x=np.array(X,dtype=np.float64)
    w=np.array(W,dtype=np.float64)
    z=np.dot(x,w)
    norms=np.linalg.norm(z,axis=1)
    gate=norms>=threshold
    y=z*gate[:,None]
    return np.stack(y,axis=0)
    pass
