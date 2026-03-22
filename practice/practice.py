import pandas as pd

s = pd.Series([1, 2, 3,], index=['a', "b", "c"])
print(s)

df = pd.DataFrame({"name": ["anil", "rohan", "kummble",], "marks": [90, 0, 0]})
print(df)