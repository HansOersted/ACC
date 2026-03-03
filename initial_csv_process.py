import numpy as np
import pandas as pd

dt = 0.007999999999995566

df = pd.read_csv("altitude_pairs.csv")

e = df["e"].to_numpy(dtype=np.float64)
N = len(e)
if N < 3:
    raise ValueError(f"Need at least 3 samples to compute de and dde. Got N={N}")

# de: forward difference
de = (e[1:] - e[:-1]) / dt          # length N-1

# dde: forward difference of de
dde = (de[1:] - de[:-1]) / dt       # length N-2

# N-2
e_aligned = e[:-2]                  # e[0 .. N-3]
de_aligned = de[:-1]                # de[0 .. N-3]
dde_aligned = dde                   # dde[0 .. N-3]

df_new = pd.DataFrame({
    "e": e_aligned,
    "de": de_aligned,
    "dde": dde_aligned
})

df_new.to_csv("altitude_processed.csv", index=False)