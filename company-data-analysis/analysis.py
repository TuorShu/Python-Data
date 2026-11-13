import pandas as pd

df = pd.read_csv("company-data-analysis/data/company_data_1000.csv")

Fiyatlar = pd.DataFrame({
    "Taksit": [
        12,
        6,
        24,
        12,
        24,
        16
    ],
    "Fiyat": [
        2000,
        1500,
        3000,
        1000,
        2500,
        2000
    ],
    "Tedarikci": [
        "Samsung",
        "Logitech",
        "Lenovo",
        "",
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
        "",
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

birlesmis = pd.merge(Fiyatlar,urunler,
          how="inner", on="Tedarikci"
          )

print(birlesmis.head(10))