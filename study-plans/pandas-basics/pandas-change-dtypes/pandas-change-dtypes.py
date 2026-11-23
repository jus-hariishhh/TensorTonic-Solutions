import pandas as pd

def change_dtype(data: dict, column: str, target_type: str) -> list:
    """
    Returns [dtypes_before, dtypes_after], both dictionaries of column names to dtype strings.
    """
    df=pd.DataFrame(data)
    l=[]
    l.append(df.dtypes.astype(str).to_dict())
    df[column]=df[column].astype(target_type)
    l.append(df.dtypes.astype(str).to_dict())
    return l
    pass
