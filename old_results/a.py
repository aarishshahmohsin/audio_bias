import pandas as pd
import numpy as np

df0 = pd.read_csv("./old_results/Bias_Types_Term_Category.csv")
# df1 = pd.read_csv("./baas_audiogen_final.csv")
# df2 = pd.read_csv("./baas_audioldm_final.csv")
# df3 = pd.read_csv("./baas_stable_final.csv")
#
# # result = pd.merge(df0, df1, on="role", how="inner")
# result = df1
# result = pd.merge(result, df2, on="role", how="inner")
# result = pd.merge(result, df3, on="role", how="inner")
#
# result.to_csv("fin.csv", index=None)
res = pd.read_csv("baas_audiogen_final.csv")

z = {}
for idx, x in df0.iterrows():
    if x["category"] != "Religion" and x["category"] != "Portrayal in Media":
        z[x["role"]] = x["category"]


l = []
for idx, x in res.iterrows():
    l.append(z[x["role"]])

res["category"] = l
res.to_csv("baas_audiogen_final.csv", index=None)
#
#
df = pd.read_csv("./baas_audiogen_final.csv")

new_df = pd.DataFrame()
new_df["term"] = df["role"]
new_df["category"] = df["category"]
new_df["male_count"] = df["male_count"]
new_df["male_count"] = new_df["male_count"].apply(lambda x: round(x, 2))
new_df["avg_baas"] = df["baas_score"]
new_df["avg_baas"] = new_df["avg_baas"].apply(lambda x: round(x, 2))

new_df_sorted = new_df.sort_values(by=["category", "avg_baas"], ascending=[True, True])

toptwo = new_df_sorted.groupby("category").head(2)
toptwo.to_csv("debias.csv", index=None)
