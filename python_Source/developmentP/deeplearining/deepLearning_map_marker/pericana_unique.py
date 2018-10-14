import pandas as pd

pericana_table = pd.read_csv('pericana_table2.csv', encoding='utf-8', index_col=0, header=0)
print(pericana_table.sido.unique())

print('--------------------------------')
print(pericana_table[pericana_table['store'] == '가양동점'])

print('--------------------------------')
print(pericana_table[pericana_table['sido'] == ''])
print('--------------------------------')
pericana_table = pericana_table.drop(1012)
print(pericana_table[pericana_table['sido']==''])
print('---------------------------------')