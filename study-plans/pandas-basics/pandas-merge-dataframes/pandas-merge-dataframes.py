import pandas as pd

def merge_dataframes(left: dict, right: dict, on: str, how: str) -> dict:
    """
    Returns a dictionary of merged column lists, with NaN for unmatched cells.
    """
    l=pd.DataFrame(left)
    r=pd.DataFrame(right)
    df=l.merge(r,on=on,how=how)
    return df.to_dict("list")
    pass
