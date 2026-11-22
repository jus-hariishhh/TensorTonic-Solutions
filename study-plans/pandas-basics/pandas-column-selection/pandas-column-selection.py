import pandas as pd

def select_column(data: dict, column: str) -> dict:
    """
    Returns a dictionary with values as a list and length as an integer.
    """
    d={}
    df=pd.DataFrame(data)
    series=df[column]
    d["values"]=list(series.values)
    d["length"]=len(series)
    return d
    pass
