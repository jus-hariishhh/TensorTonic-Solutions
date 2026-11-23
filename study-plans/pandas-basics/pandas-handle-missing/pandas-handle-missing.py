import pandas as pd

def handle_missing(data: dict, fill_value: float) -> dict:
    """
    Returns null_counts as a dictionary of integers and cleaned_data as a dictionary of lists.
    """
    df=pd.DataFrame(data)
    d={}
    d["null_counts"]=df.isna().sum().to_dict()
    df=df.fillna(fill_value)
    d["cleaned_data"]=df.to_dict("list")
    return d
    pass
