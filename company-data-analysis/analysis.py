import pandas as pd

df = pd.read_csv("company-data-analysis/data/company_data_1000.csv")

df["ToplamSatis"] = df["Adet"] * df["BirimFiyat"]

grup1 = df.groupby("Sehir").agg(
    toplam_satis = ("Adet", "sum"),
    ortalama_satis = ("Adet", "mean"),
    en_yuksek_satis = ("Adet", "max"),
    en_dusuk_satis = ("Adet", "min")
)

print(df.head())