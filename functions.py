import pandas as pd

def clean_checklist(df):
    drop_columns = [1, 11, 12, 13, 17, 20, 22, 23, 24, 25, 26, 27, 28, 29]
    rename_columns = {'Unnamed: 11': 'Diagrama','Unnamed: 21': 'NP', 'Unnamed: 22': 'Lot',
                        'Unnamed: 23': 'Cantidad', 'Unnamed: 28': 'Modelo' }
    nan_value = float("NaN")
    for i in ['T', '']:
        df.replace(i, nan_value, inplace=True)
    df.dropna(how="all", axis=1, inplace=True)
    df = df.drop(df.columns[drop_columns], axis=1)
    df.rename(columns= rename_columns, inplace=True)
    df['Unique'] = df['Nº de circuito'] + ' ' + df['NP']
    df.drop_duplicates(subset ="Unique",keep = 'first', inplace = True)
    # Rearange columns
    df = df.reindex(
        columns = ['Unique'] + [col for col in df.columns if col != 'Machine' and col != 'Unique'] + ['Machine']
        )
    # machines = df['Machine'].str.split(' ', n=10, expand=True)
    # machine_cols = len(machines.axes[1])
    # cols = [ f'Machines {i + 1}' for i in range(len(machines.axes[1]))]
    # machines.columns = cols
    # df2 = pd.concat([df, machines], axis=1)
    return df

def checklist_info(df):
    part_num = df.NP.unique()
    qty = [ df[df['NP'] == i ]['Nº de circuito'].count()
            for i in part_num ]
    corte = [ df[(df['NP'] == i ) & (df['Machine'].str.startswith('A'))]['Nº de circuito'].count()
              for i in part_num]
    riv = [ df[(df['NP'] == i ) & (df['Machine'].str.startswith('B'))]['Nº de circuito'].count()
            for i in part_num]
    sl = [ df[(df['NP'] == i )&(df['Machine'].str.startswith('SLD'))]['Nº de circuito'].count()
           for i in part_num]
    joint_sld = [ df[(df['NP'] == i )&(df['Nº de circuito'].str.endswith('#')) & (df['Terminal(L)'].str.startswith('TKT'))]['Nº de circuito'].count() +
                  df[(df['NP'] == i )&(df['Nº de circuito'].str.endswith('#')) & (df['Terminal(R)'].str.startswith('TKT'))]['Nº de circuito'].count()               
                  for i in part_num]
    pret = [ df[(df['NP'] == i )&(df['Materia'].str.contains('XXXX'))]['Nº de circuito'].count()
           for i in part_num]
    pret_lg = [ df[(df['NP'] == i )&(df['Materia'].str.contains('XXXY6'))]['Nº de circuito'].count()
           for i in part_num]
    termistor = [ df[(df['NP'] == i )&(df['Materia'].str.contains('XXXG'))]['Nº de circuito'].count()
           for i in part_num]
    twist = [ df[(df['NP'] == i )&(df['Machine'].str.contains('TW'))]['Nº de circuito'].count()
           for i in part_num]
    sld = []
    for i in range(len(sl)):
        sld.append(sl[i] - (pret[i] + pret_lg[i]))
    df = pd.DataFrame(list(zip(part_num, qty, corte, riv, sld,joint_sld, pret, pret_lg, termistor, twist)),
                      columns=['PN', 'QTY', 'Corte', 'RIVIAN', 'SLD', 'JOINT SLD', 'PRET', 'PRET LG', 'TERMISTOR', 'TWIST'])
    return df

def clean_manual(df):
    df.rename(columns={'P/N' : 'NP'}, inplace=True)
    df['Unique'] = df['NP'] + " " + df['No.circuito'] + " " + df['Terminal de union']
    df.drop_duplicates(subset ="Unique",keep = 'first', inplace = True)
    return df

def manual_info(df):
    part_num = df.NP.unique()
    prensas =[df[(df['NP'] == i ) & (df['Maquina'].str.startswith('C'))]['No.circuito'].count()
              for i in part_num]
    joint = [df[(df['NP'] == i ) & (df['Maquina'].str.startswith('SJ'))]['No.circuito'].count()
             for i in part_num]
    prensas_sld = [df[(df['NP'] == i ) & (df['Maquina'] == 'SL04')]['No.circuito'].count() +
                df[(df['NP'] == i ) & (df['Maquina'] == 'SL05')]['No.circuito'].count() +
                df[(df['NP'] == i ) & (df['Maquina'] == 'SL06')]['No.circuito'].count() +
                df[(df['NP'] == i ) & (df['Maquina'] == 'SL07')]['No.circuito'].count()
                   for i in part_num]
    df = pd.DataFrame(list(zip(part_num, prensas, joint, prensas_sld)),
                   columns = ['PN', 'PRENSAS', 'JONT', 'PRENSAS SLD'])
    return df

def clean_postp(df):
    df.rename(columns={'P/N' : 'NP'}, inplace=True)
    df['Unique'] = df['NP'] + " " +df['Nº de circuito'] + " " + df['Ruta']
    df.drop_duplicates(subset ="Unique",keep = 'first', inplace = True)
    return df

def postp_info(df):
    part_num = df.NP.unique()
    twist = [df[(df['NP'] == i ) & (df['Maquina'].str.startswith('TW'))]['Nº de circuito'].count()
             for i in part_num]
    sello = [df[(df['NP'] == i ) & (df['Ruta'] == 'Insert Sub-materials [Seal]')]['Nº de circuito'].count()
             for i in part_num]
    desforre_medio = [df[(df['NP'] == i ) & (df['Ruta'] == 'Manual stripping(Middle)')]['Nº de circuito'].count()
                      for i in part_num]
    desforre_punta = [df[(df['NP'] == i ) & (df['Ruta'] == 'Shield Wire Inner Sheath stripping')]['Nº de circuito'].count() * 2
                      for i in part_num]
    encinte_auto = [df[(df['NP'] == i ) & (df['Ruta'] == 'Manual Taping')]['Nº de circuito'].count()
                    for i in part_num]
    inser_tuboter = [df[(df['NP'] == i ) & (df['Ruta'] == 'Insert Sub-materials [HMT,HSC]')]['Nº de circuito'].count()
                     for i in part_num]
    inser_tubo = [df[(df['NP'] == i ) & (df['Ruta'] == 'lnsert Sub-materials [PVC,COT,SLEEVE]')]['Nº de circuito'].count()
                  for i in part_num]
    termo = [df[(df['NP'] == i ) & (df['Ruta'] == 'Heat-melting')]['Nº de circuito'].count()
             for i in part_num]
    df = pd.DataFrame(list(zip(part_num, sello, desforre_medio, desforre_punta, encinte_auto, inser_tuboter, inser_tubo, termo)),
                  columns = ['PN', 'SELLO', 'DESFORRE MEDIO', 'DESFORRE DE PUNTA',
                             'ENCINTE AUTOMATICO', 'INSERCION DE TUBO TERMO', 'INSERCION DE TUBO', 'TERMO'])
    return df

def combinar(df1, df2, df3):
    procesos= pd.merge(df1, df2, on ='PN', how ='left')
    procesos= pd.merge(procesos, df3, on = 'PN', how = 'left')
    procesos = procesos.fillna(0)
    return procesos


if __name__ == '__main__':

    c_list = pd.read_excel('14100.xlsx')
    manual = pd.read_excel('10500.xlsx')

    checklist, p_cols = clean_checklist(c_list)
    checklist_proces = checklist_info(checklist)

    manual_proces = manual_info(clean_manual(manual))

    # checklist.to_excel('result.xlsx', index=False)
    # procesos.to_excel('procesos.xlsx', index=False)

    # print(checklist_proces)
    # print(procesos)
    print(manual_proces)

