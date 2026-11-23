import pandas as pd

def set_index_column(data: dict, index_col: str) -> dict:
    """
    Returns index_values and columns as lists, plus data as a dictionary of lists.
    """
    df=pd.DataFrame(data)
    d={}
    df=df.set_index(index_col)
    d["index_values"]=list(df.index)
    d["columns"]=list(df.columns)
    d["data"]=df.to_dict("list")
    return d
    pass
