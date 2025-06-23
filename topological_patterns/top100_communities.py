import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("topological_patterns/top100_models_communities.csv")

test = df.groupby("m.community")

print(test.size().sort_values(ascending=False))