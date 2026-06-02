import pandas as pd
import pickle

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("input/dev_data.csv")

X = df.drop(
    columns=[
        "customer_id",
        "snapshot_month",
        "bad_flag"
    ]
)

y = df["bad_flag"]

model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("classifier", LogisticRegression(
        solver="liblinear",
        max_iter=500
    ))
])

model.fit(X, y)

with open("input/LR_SCorecard.pkl", "wb") as f:
    pickle.dump(model, f)

print("LR_SCorecard.pkl created successfully")
print("Features:", X.columns.tolist())