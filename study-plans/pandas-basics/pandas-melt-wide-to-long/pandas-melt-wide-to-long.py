import pandas as pd

def melt_dataframe(data: dict, id_vars: list, value_vars: list) -> dict:
    """
    Returns identifier column lists together with variable and value lists.
    """
    df=pd.DataFrame(data) 
    long=pd.melt(df,id_vars=id_vars,value_vars=value_vars,
                                       var_name="variable",
                                       value_name="value")
    return long.to_dict("list")
    pass
