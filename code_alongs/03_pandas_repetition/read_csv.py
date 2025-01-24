import pandas as pd

from pathlib import Path

# print (Path(__file__).parent)

data_path = print (Path(__file__).parent)

df = pd.read_csv(data_path / "calories.csv")

print(df.head)