import pandas as pd

cheogajip_table = pd.read_csv('cheogajip_table2.csv', encoding='utf-8', index_col=0, header=0)
cheogajip = cheogajip_table.apply(lambda r : r['sido'] + '' + r['gungu'], axis =1).value_counts()
print(cheogajip)

pericana_table = pd.read_csv('pericana_table2.csv', encoding='utf-8', index_col=0, header=0)
pericana = pericana_table.apply(lambda r : r['sido'] + '' + r['gungu'], axis =1).value_counts()
print(pericana)

kyochon_table = pd.read_csv('kyochon_table2.csv', encoding='utf-8', index_col=0, header=0)
kyochon = kyochon_table.apply(lambda r : r['sido'] + '' + r['gungu'], axis =1).value_counts()
print(kyochon)

goobne_table = pd.read_csv('goobne_table2.csv', encoding='utf-8', index_col=0, header=0)
goobne = goobne_table.apply(lambda r : r['sido'] + '' + r['gungu'], axis =1).value_counts()
print(goobne)

chiken_table = pd.DataFrame({'cheogajip': cheogajip, ' pericana':pericana, 'kyochon': kyochon, 'goobne':goobne}).fillna(0)
print(chiken_table)
