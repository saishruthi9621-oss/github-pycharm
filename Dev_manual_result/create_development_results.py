import pandas as pd

df = pd.DataFrame({
    "AUC": [0.72],
    "KS": [0.35],
    "GINI": [0.44]
})

df.to_excel(
    "input/development_results.xlsx",
    index=False
)

print("development_results.xlsx created")