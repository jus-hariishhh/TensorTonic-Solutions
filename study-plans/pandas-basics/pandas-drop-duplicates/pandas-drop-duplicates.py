import pandas as pd

def drop_duplicates(data: dict) -> list:
    """
    Returns [rows_before, rows_after, cleaned_data], with integer counts and a dictionary of lists.
    """
    df=pd.DataFrame(data)
    l=[]
    l.append(df.shape[0])
    df=df.drop_duplicates()
    l.append(df.shape[0])
    l.append(df.to_dict("list"))
    return l
    pass
