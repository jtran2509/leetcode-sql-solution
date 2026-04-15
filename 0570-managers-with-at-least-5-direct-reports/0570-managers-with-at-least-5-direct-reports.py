import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    result = employee.groupby('managerId').size().reset_index(name="count")
    result = result[result['count'] >= 5]['managerId']
    return employee[employee['id'].isin(result)][['name']]