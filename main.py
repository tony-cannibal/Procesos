import pandas as pd

c_list = pd.read_excel('14100.xlsx')

def clean_checklist(df):
    drop_columns = [1, 11, 12, 13, 17, 20, 22, 23, 24, 25, 26, 27, 28, 29] 
    rename_columns = {'Unnamed: 11': 'Diagrama','Unnamed: 21': 'NP', 'Unnamed: 22': 'Lot', 
                        'Unnamed: 23': 'Cantidad', 'Unnamed: 28': 'Modelo' }
    nan_value = float("NaN")
    for i in ['T', '']:
        df.replace(i, nan_value, inplace=True)
    df.dropna(how="all", axis=1, inplace=True)

    # df.to_excel('check cols.xlsx', index=False)

    df = c_list.drop(c_list.columns[drop_columns], axis=1)
    df.rename(columns= rename_columns, inplace=True)
    df['Unique'] = df['Nº de circuito'] + ' ' + df['NP']
    df.drop_duplicates(subset ="Unique",keep = 'first', inplace = True)
    df = df.reindex(
        columns = ['Unique'] + [col for col in df.columns if col != 'Machine' and col != 'Unique'] + ['Machine']
        )
    machines = df['Machine'].str.split(' ', n=10, expand=True)
    machine_cols = len(machines.axes[1])
    cols = [ f'Machines {i + 1}' for i in range(len(machines.axes[1]))]
    machines.columns = cols
    df2 = pd.concat([df, machines], axis=1)
    return df2, machine_cols



checklist, p_cols = clean_checklist(c_list)

checklist.to_excel('result.xlsx', index=False)

print(checklist)
print(p_cols)