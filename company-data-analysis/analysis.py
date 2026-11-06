import pandas as pd

df = pd.read_csv("company-data-analysis/data/company_data_1000.csv")

kosul1 = df.groupby("Sehir").agg(
    toplam_adet=("Adet", "sum"),
    ort_satis_adedi=("Adet", "mean"),
    en_yuksek_urun_fiyat=("BirimFiyat", "max"),
    islem_sayisi=("Adet", "count")
)
kosul2 = df.groupby("Sehir").agg(
    ort_urun_fiyat=("BirimFiyat", "mean")
)

print(kosul1)