import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# 🔧 editable region
# ===============================
INPUT_CSV = "altitude_processed.csv"
OUTPUT_NPZ = "input_data.npz"
OUTPUT_FIG = "altitude_plot.png"

start_row = 0
end_row = None   # last row: end_row = None
# ===============================


def main():
    df = pd.read_csv(INPUT_CSV)

    required = ["e", "de", "dde"]
    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing column '{col}'. Found columns: {list(df.columns)}")

    total_rows = len(df)

    global end_row
    if end_row is None:
        end = total_rows - 1
    else:
        end = end_row

    if start_row < 0 or start_row >= total_rows:
        raise ValueError(f"start_row out of range: {start_row}")
    if end < start_row or end >= total_rows:
        raise ValueError(f"end_row out of range: {end}")

    selected_df = df.iloc[start_row:end + 1][["e", "de", "dde"]]
    selected = selected_df.to_numpy(dtype=np.float64)

    e = selected[:, 0]
    de = selected[:, 1]
    dde = selected[:, 2]

    # ===== build arrays for npz =====
    e_array = np.stack([e, de], axis=1)
    de_array = np.stack([de, dde], axis=1)

    np.savez(OUTPUT_NPZ, e=e_array, de=de_array)

    print("===================================")
    print(f"Saved: {OUTPUT_NPZ}")
    print(f"Rows used: {start_row} → {end}")
    print(f"Total samples: {len(e_array)}")
    print(f"e shape: {e_array.shape}")
    print(f"de shape: {de_array.shape}")
    print("===================================")

    # ===== plotting =====
    x = np.arange(len(e))

    plt.figure(figsize=(10, 6))
    plt.plot(x, e, label="e")
    plt.plot(x, de, label="de")
    plt.plot(x, dde, label="dde")

    plt.xlabel("Sample Index")
    plt.ylabel("Value")
    plt.title("e, de, dde vs Sample Index")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()