import pandas as pd
import functions as fn
import functions2 as f2



c_list = pd.read_excel('data/14100.xlsx')
manual = pd.read_excel('data/10500.xlsx')
post = pd.read_excel('data/10600.xlsx')


# Checklist Proces
checklist_proces = f2.checklist_info(fn.clean_checklist(c_list))
print(checklist_proces)

# checklist_proces.to_excel('output\checklist.xlsx')

# Manual Proces
# manual_proces = fn.manual_info(fn.clean_manual(manual))
# Post Proces
# post_porces = fn.postp_info(fn.clean_postp(post))


# combinado = fn.combinar(checklist_proces, manual_proces, post_porces)


# print(checklist_proces)
# print(manual_proces)
# print(post_porces)

# print(combinado)
# print(combinado.dtypes)
