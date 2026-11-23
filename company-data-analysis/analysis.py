import pandas as pd

df = pd.read_csv("company-data-analysis/data/company_data_1000.csv")

df["ToplamSatis"] = df["Adet"] * df["BirimFiyat"]

grup1 = df.groupby("Sehir").agg(
    ToplamSatis=("ToplamSatis", "sum")
).reset_index()

print(df.head())