import pandas as pd

df = pd.read_csv("company-data-analysis/data/company_data_1000.csv")

filtre = df[
    (df['BirimFiyat'] > 30000) &
    (df['Sehir'] == 'Istanbul')]

print(filtre)