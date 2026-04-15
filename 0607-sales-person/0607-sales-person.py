import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_comp = company[company['name'] == "RED"]['com_id']
    red_sales_id = orders[orders['com_id'].isin(red_comp)]['sales_id']
    result = sales_person[~sales_person['sales_id'].isin(red_sales_id)]
    return result[['name']]