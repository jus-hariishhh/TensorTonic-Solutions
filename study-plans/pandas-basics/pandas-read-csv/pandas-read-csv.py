import pandas as pd

def create_dataframe(data: dict) -> dict:
    """
    Returns a dictionary with data, shape [rows, columns], and ordered column names.
    """
    d={}
    df=pd.DataFrame(data)
    d["data"]=df.to_dict(orient="list")
    d["shape"]=[int(df.shape[0]),int(df.shape[1])]
    d["columns"]=[str(c) for c in df.columns]
    return d
    pass
