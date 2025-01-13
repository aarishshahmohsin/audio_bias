import pandas as pd


pd.set_option("display.precision", 2)
df = pd.read_csv("terms_355.csv")

for idx, row in df.iterrows():
    if row["total"] == 200:
        df.loc[idx, "total"] /= 2
        df.loc[idx, "male_count"] /= 2
        df.loc[idx, "female_count"] /= 2
    df.loc[idx, "male_percentage"] = (
        row["male_count"] / (row["female_count"] + row["male_count"]) * 100
    )


df["male_percentage"] = df["male_percentage"].apply(lambda x: round(x, 3))

df.to_csv("terms_355_fixed.csv", index=None)
