import pandas as pd
import functions as fn



c_list = pd.read_excel('data/14100.xlsx')
manual = pd.read_excel('data/10500.xlsx')
post = pd.read_excel('data/10600.xlsx')


# Checklist Proces
checklist_proces = fn.checklist_info(fn .clean_checklist(c_list))
# Manual Proces
manual_proces = fn.manual_info(fn.clean_manual(manual))

post_porces = fn.postp_info(fn.clean_postp(post))

combinado = fn.combinar(checklist_proces, manual_proces, post_porces)


# print(checklist_proces)
# print(manual_proces)
# print(post_porces)

print(combinado)
print(combinado.dtypes)
