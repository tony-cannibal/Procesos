
drop_columns = [1, 11, 12, 13, 17, 20, 22, 23, 24, 25, 26, 27, 28, 29]

rename_columns = {'Unnamed: 11': 'Diagrama','Unnamed: 21': 'NP', 'Unnamed: 22': 'Lot',
                    'Unnamed: 23': 'Cantidad', 'Unnamed: 28': 'Modelo' }


checklist_columns = ['PN', 'QTY', 'Corte', 'RIVIAN', 'SLD', 'JOINT SLD',
                     'PRET', 'PRET LG', 'TERMISTOR', 'TWIST', 'ENCINTE JOINT']

fmt_cols = {
    'PRENSAS': 'int',
    'JOINT': 'int',
    'PRENSAS SLD': 'int',
    'SELLO': 'int',
    'DESFORRE MEDIO': 'int',
    'DESFORRE DE PUNTA': 'int',
    'ENCINTE AUTOMATICO': 'int',
    'INSERCION DE TUBO TERMO': 'int',
    'INSERCION DE TUBO': 'int',
    'TERMO': 'int'
}
