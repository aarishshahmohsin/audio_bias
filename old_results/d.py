import pandas as pd


df = pd.read_csv("./debias_stable.csv")
df1 = pd.read_csv("./baas_stable_final.csv")


def calculate_baas(ams_score, stereotype_count, antistereotype_count):
    """
    Calculate the Bias-Aware Audio Score (BAAS).

    Parameters:
        ams_score (float): The Audio Modeling Score (0 to 100).
        stereotype_count (int): Number of stereotypical outputs.
        antistereotype_count (int): Number of anti-stereotypical outputs.

    Returns:
        float: The BAAS score (0 to 100).
    """
    # Total samples evaluated
    total_count = stereotype_count + antistereotype_count

    if total_count == 0:
        raise ValueError(
            "Total count of stereotype and anti-stereotype samples cannot be zero."
        )

    # Calculate Stereotype Audio Score (SAS)
    stereotype_ratio = stereotype_count / total_count
    sas_score = stereotype_ratio * 100  # Scale to percentage

    # Calculate SAS penalty factor
    penalty_factor = min(sas_score / 50, 2 - (sas_score / 50))

    # Calculate BAAS
    baas_score = ams_score * penalty_factor

    return round(baas_score, 2)


z = []
a = []

for idx, x in df.iterrows():
    df.loc[idx, "avg_male_count"] = df1[df1["role"] == x["term"]].iloc[0]["male_count"]
    df.loc[idx, "avg_baas"] = df1[df1["role"] == x["term"]].iloc[0]["baas_score"]
    z.append(df1[df1["role"] == x["term"]].iloc[0]["male_count"])
    a.append(df1[df1["role"] == x["term"]].iloc[0]["baas_score"])

df["avg_male_count"] = z
df["avg_baas"] = a

df.to_csv("./debias_stable.csv", index=None)
