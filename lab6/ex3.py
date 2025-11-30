import pandas as pd
import numpy as np

csv_content = """DenumireArticol,Stoc,PretUnitar
Minge fotbal,50,45.5
Tricou sport,120,35.0
Adidasi,80,120.0
Racheta tenis,10,89.9
Bicicleta,15,450.0
Sac de dormit,40,75.5
"""
with open('inventar_sport.csv', 'w') as f:
    f.write(csv_content)

# Incarcare in DataFrame
df = pd.read_csv('inventar_sport.csv')

print("Primele 3 linii din DataFrame:")
print(df.head(3))
print("\nInformatii despre DataFrame:")
print(df.info())

def  valoare_stoc(stoc, pret_unit):
    return stoc * pret_unit

df['ValoareTotala'] = df.apply(lambda x: valoare_stoc(x['Stoc'], x['PretUnitar']), axis=1)

print("\nDataFrame cu valoarea totala:")
print(df)

valoare_totala_magazin = df['ValoareTotala'].sum()
print(f"\nValoarea totala a tuturor articolelor: {valoare_totala_magazin:.2f}")

df_peste_1000 = df[df['ValoareTotala'] > 1000]
print("\nArticole cu valoare totala peste 1000:")
print(df_peste_1000)

df_peste_1000.to_csv('articole_valoare_peste_1000.csv', index=False)
print("\nDatele au fost salvate in 'articole_valoare_peste_1000.csv'")