from anyio import Path
import pandas as pd

df = pd.read_csv("company-data-analysis/data/company_data_1000.csv")

TransactionDates = df["Tarih"] >= "2026-06-07"
TotalSale = df["BirimFiyat"] * df["Adet"]

print("Total Sale on 2026-06-07:", TotalSale[TransactionDates].sum())

