import pandas as pd

def reset_index_demo(data: dict, index_col: str) -> list:
    """
    Returns [columns_before_reset, columns_after_reset], both lists of strings.
    """
    df=pd.DataFrame(data)
    l=[]
    df=df.set_index(index_col)
    l.append(list(df.columns))
    df=df.reset_index()
    l.append(list(df.columns))
    return l
    pass
