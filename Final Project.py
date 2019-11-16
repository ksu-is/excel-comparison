import pandas as pd
import numpy as np
#putting both files into dataframes
df1 = pd.read_excel('employee-number-1.xlsx', 'Sheet1', na_values=['NA'])
df2 = pd.read_excel('employee-number-2.xlsx', 'Sheet1', na_values=['NA'])
#order by employee number
df1.sort(columns="employee number")
df1=df1.reindex()
df2.sort(columns="employee number")
df2=df2.reindex()
#Diff function to show what changes are
def report_diff(x):
    return x[0] if x[0] == x[1] else '{} ---> {}'.format(*x)
#merge two datasets into a Panel
diff_panel = pd.Panel(dict(df1=df1,df2=df2))