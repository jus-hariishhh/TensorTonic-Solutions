import pandas as pd

def inspect_dataframe(data: dict) -> dict:
    """
    Returns rows, cols, columns, dtypes, and total_values in a dictionary.
    """
    df=pd.DataFrame(data)
    d={}
    d["rows"]=int(len(df))
    d["cols"]=int(df.size/len(df))
    d["columns"]=list(df.columns)
    d["dtypes"] = df.dtypes.astype("str").to_dict()
    d["total_values"]=int(df.size)
    return d
    pass
