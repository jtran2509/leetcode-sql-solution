import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    result = employee_uni.merge(employees, how="right", left_on="id",
                                right_on="id",
                                suffixes=('_UNI', '_norm'))
    return result[['unique_id', 'name']]