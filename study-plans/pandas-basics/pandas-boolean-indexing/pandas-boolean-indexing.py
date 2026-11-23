import pandas as pd

def boolean_filter(data: dict, column: str, threshold: float) -> dict:
    """
    Returns filtered_data as a dictionary of lists and count as an integer.
    """
    df=pd.DataFrame(data)
    d={}
    d["filtered_data"]=df.loc[df[column]>threshold,df.columns].to_dict("list")
    d["count"]=df.loc[df[column]>threshold,df.columns].shape[0]
    return d
    pass
