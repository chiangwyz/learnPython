import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda x: x['salary'] if x['employee_id'] % 2 and not x['name'].startswith('M') else 0, 
        axis=1
    )

    df = employees[['employee_id', 'bonus']].sort_values('employee_id')
    
    return df
