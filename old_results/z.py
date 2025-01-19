import pandas as pd

df = pd.read_csv("./old_results/Bias_Types_Term_Category.csv")

for _, x in df.iterrows():
    if x["category"] not in ["Religion", "Portrayal in Media"]:
        print(x["category"])
