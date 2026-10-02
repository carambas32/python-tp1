import pandas as pd

df = pd.DataFrame({"X": [10, 20, 30, 40], "Y": [5, 10, 15, 20], "Z": [4, 8, 12, 16]})
print(df)

print(df["X"])
print(df[["X", "Z"]])
print(df.loc[:2, ["X", "Y"]])
print(df.loc[df["X"] >= 20])
