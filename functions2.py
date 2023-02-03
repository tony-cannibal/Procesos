import pandas as pd
import constants as cn


def clean_checklist(df):
    nan_value = float("NaN")
    for i in ['T', '']:
        df.replace(i, nan_value, inplace=True)
    df.dropna(how="all", axis=1, inplace=True)
    df = df.drop(df.columns[cn.drop_columns], axis=1)
    df.rename(columns=cn.rename_columns, inplace=True)
    df['Unique'] = df['Nº de circuito'] + ' ' + df['NP']
    df.drop_duplicates(subset ="Unique",keep = 'first', inplace = True)
    # Rearange columns
    df = df.reindex(
        columns = ['Unique'] + 
            [col for col in df.columns if col != 'Machine' and col != 'Unique'] +
            ['Machine']
        )
    # machines = df['Machine'].str.split(' ', n=10, expand=True)
    # machine_cols = len(machines.axes[1])
    # cols = [ f'Machines {i + 1}' for i in range(len(machines.axes[1]))]
    # machines.columns = cols
    # df2 = pd.concat([df, machines], axis=1)
    return df


def checklist_info(df):
    part_num = df.NP.unique()

    qty = []
    for i in part_num:
        qty.append(df[df['NP'] == i ]['Nº de circuito'].count())

    corte = []
    for i in part_num:
        corte.append(df[(df['NP'] == i ) &
                        (df['Machine'].str.startswith('A'))]
                     ['Nº de circuito'].count())
    rivian = []
    for i in part_num:
        rivian.append(df[(df['NP'] == i ) &
                         (df['Machine'].str.startswith('B'))]
                      ['Nº de circuito'].count())
    sl = []
    for i in part_num:
        sl.append(df[(df['NP'] == i ) &
                     (df['Machine'].str.startswith('SLD'))]
                  ['Nº de circuito'].count())
    joint_sld = []
    for i in part_num:
        joint_sld.append(
            df[(df['NP'] == i ) &
               (df['Nº de circuito'].str.endswith('#')) &
               (df['Terminal(L)'].str.startswith('TKT'))]
            ['Nº de circuito'].count() +
            df[(df['NP'] == i ) &
               (df['Nº de circuito'].str.endswith('#')) &
               (df['Terminal(R)'].str.startswith('TKT'))]
            ['Nº de circuito'].count())
    pret = []
    for i in part_num:
        pret.append(df[(df['NP'] == i ) &
                       (df['Materia'].str.contains('XXXX'))]
                    ['Nº de circuito'].count())
    pret_lg = []
    for i in part_num:
        pret_lg.append(df[(df['NP'] == i ) &
                          (df['Materia'].str.contains('XXXY6'))]
                       ['Nº de circuito'].count())
    termistor = []
    for i in part_num:
        termistor.append(df[(df['NP'] == i ) &
                            (df['Materia'].str.contains('XXXG'))]
                         ['Nº de circuito'].count())
    twist = []
    for i in part_num:
        twist.append(df[(df['NP'] == i ) &
                        (df['Machine'].str.contains('TW'))]
                     ['Nº de circuito'].count())
    enc_joint= []
    for i in part_num:
        enc_joint.append(df[(df['NP'] == i ) &
                           (df['Machine'].str.contains('SJ')) &
                           (df['Machine'].str.contains('T0'))]
                        ['Nº de circuito'].count())
    enc_sld = []
    for i in part_num:
        enc_sld.append(df[(df['NP'] == i ) &
                          (df['Materia'].str.contains('SLD')) &
                          (df['Machine'].str.contains('T0'))]
                       ['Nº de circuito'].count())
    sld = []
    for i in range(len(sl)):
        sld.append(sl[i] - (pret[i] + pret_lg[i]))
    df = pd.DataFrame(
        list(
            zip(
                part_num, qty, corte, rivian, sld,joint_sld,
                pret, pret_lg, termistor, twist, enc_joint)),
        columns=cn.checklist_columns)
    return df





