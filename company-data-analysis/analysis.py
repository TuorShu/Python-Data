import pandas as pd

df = pd.read_csv("company-data-analysis/data/company_data_1000.csv")

temsilciler = pd.DataFrame({
    "Temsilci": [
        "Ahmet", "Mehmet", "Ayse", "Zeynep",
        "Elif", "Can", "Mert", "Derya"
    ],
    "Bolge": [
        "Marmara", "Ege", "Akdeniz", "İç Anadolu",
        "Karadeniz", "Marmara", "Ege", "Akdeniz"
    ]
})

merged_temsilciler = pd.merge(
    df,
    temsilciler,
    on="Temsilci",
    how="right"
)
print(merged_temsilciler)