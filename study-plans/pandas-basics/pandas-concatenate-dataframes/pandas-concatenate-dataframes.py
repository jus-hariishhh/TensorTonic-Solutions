import pandas as pd

def concat_dataframes(dfs: list) -> list:
    """
    Returns [shape, data], with shape [rows, columns] and data a dictionary of lists.
    """
    l=[pd.DataFrame(i) for i in dfs]
    c=pd.concat(l)
    return [list(c.shape), c.to_dict("list")]
    pass
