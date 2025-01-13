import pandas as pd

df1 = pd.read_csv("./old_results/terms_355.csv")
df2 = pd.read_csv("./old_results/baas_res_100_ams.csv")

df1["baas_score"] = df2["baas_score"]
df1.to_csv("baas_audiogen_final.csv", index=None)
