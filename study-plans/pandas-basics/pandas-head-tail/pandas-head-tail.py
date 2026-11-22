import pandas as pd

def head_tail(data: dict, n: int) -> dict:
    """
    Returns head and tail as dictionaries mapping columns to value lists.
    """
    df=pd.DataFrame(data)
    d={}
    d["head"]=df.head(n).to_dict("list")
    d["tail"]=df.tail(n).to_dict("list")
    return d
    pass
