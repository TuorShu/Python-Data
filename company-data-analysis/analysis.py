from anyio import Path
import pandas as pd

df = pd.read_csv("company-data-analysis/data/company_data_1000.csv")

TransactionDates = df["Tarih"] >= "2026-06-07"
TotalSale = df["BirimFiyat"] * df["Adet"]

new_df = pd.DataFrame()
new_df["Tarih"] = df[TransactionDates]["Tarih"]
new_df["BirimFiyat"] = df[TransactionDates]["BirimFiyat"]
new_df["Adet"] = df[TransactionDates]["Adet"]
new_df["ToplamSatış"] = TotalSale[TransactionDates]

new_df.to_csv("company-data-analysis/data/filtered_data.csv", index=False)

print("Total Sale on 2026-06-07:", TotalSale[TransactionDates].sum())

