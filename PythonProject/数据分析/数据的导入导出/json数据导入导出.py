import pandas as pd

df = pd.read_json('../data/data1.json')
print(type(df))

df = pd.read_json('../data/test.json')
print(type(df))

import json
with open('../data/test.json') as f:
    data = json.load(f)
print(data)