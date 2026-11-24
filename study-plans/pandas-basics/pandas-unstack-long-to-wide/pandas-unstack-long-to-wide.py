import pandas as pd

def unstack_to_wide(data: dict, index_col: str, columns_col: str, values_col: str) -> dict:
    """
    Returns identifier and category column lists, with NaN for missing pairs.
    """
    df = pd.DataFrame(data)
    result = df.set_index([index_col, columns_col])[values_col]
    wide=result.unstack()
    wide.columns.name = None
    wide = wide.reset_index()
    return wide.to_dict("list")
    pass
