import pandas as pd

def select_columns(data: dict, columns: list) -> dict:
    """
    Returns a dictionary of value lists in the requested column order.
    """
    df=pd.DataFrame(data)
    d={}
    new_df=df.loc[:,columns]
    return new_df.to_dict("list")
    pass
