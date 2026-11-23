import pandas as pd

def iloc_selection(data: dict, row: int, col: int) -> list:
    """
    Returns [element, row_values, col_values], with both value sequences as lists.
    """
    df=pd.DataFrame(data)
    l=[]
    l.append(df.iloc[row,col])
    l.append(list(df.iloc[row,:]))
    l.append(list(df.iloc[:,col]))
    return l
    pass
