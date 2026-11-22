import pandas as pd

def data_types_overview(data: dict) -> dict:
    """
    Returns a dictionary with dtypes, type_counts, and num_columns.
    """
    df=pd.DataFrame(data)
    d={}
    d["dtypes"]=df.dtypes.astype(str).to_dict()
    d["type_counts"]=df.dtypes.astype(str).value_counts().to_dict()
    d["num_columns"]=len(df.columns)
    return d
    pass
