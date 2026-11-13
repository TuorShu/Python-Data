import pandas as pd

df = pd.read_csv("company-data-analysis/data/company_data_1000.csv")

Fiyatlar = pd.DataFrame({
    "Taksit": [
        12,
        6,
        24,
        6,
        6,
        24
    ],
    "Fiyat": [
        28000,
        3500,
        72000,
        6000,
        2000,
        109000
    ],
    "Tedarikci": [
        "Samsung",
        "Logitech",
        "Lenovo",
        "Logitech",
        "HyperX",
        "Apple"
    ]
})

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
        6,
        12,
        36
    ]
})

birlesmis = pd.merge(Fiyatlar,urunler,
          how="left", on="Tedarikci"
          )

print(birlesmis.head(10))