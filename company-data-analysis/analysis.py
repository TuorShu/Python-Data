import pandas as pd

df = pd.read_csv("company-data-analysis/data/company_data_1000.csv")

urunler = pd.DataFrame({
    "Urun": [
        "Tablet",
        "Mouse",
        "Laptop",
        "Klavye",
        "Mikrofon",
        "Telefon"
    ],
    "Tedarikci": [
        "Samsung",
        "Logitech",
        "Lenovo",
        "Logitech",
        "HyperX",
        "Apple"
    ],
    "Garanti_Ayi": [
        24,
        12,
        24,
        12,
        24,
        16
    ]
})

birlesmis = pd.merge(df,urunler,
          how="right", 
          on="Urun"
          )

print(birlesmis.head(10))