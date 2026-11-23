import pandas as pd

def groupby_basics(data: dict, group_col: str, value_col: str) -> dict:
    """
    Returns sum, mean, and count dictionaries keyed by group label.
    """
    df=pd.DataFrame(data)
    d={}
    d["sum"]=df.groupby(group_col)[value_col].sum().to_dict()
    d["mean"]=df.groupby(group_col)[value_col].mean().to_dict()
    d["count"]=df.groupby(group_col)[value_col].count().to_dict()
    return d
    pass
