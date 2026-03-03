import pandas as pd

dt = 0.007999999999995566

df = pd.read_csv("altitude_pairs.csv")

df_new = pd.DataFrame()
df_new["e"] = df["e"]
df_new["de"] = df["edot"]

df_new["dde"] = (df["edot_next"] - df["edot"]) / dt

df_new.to_csv("altitude_processed.csv", index=False)