import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("topological_patterns/export.csv")

sns.set_theme(style="whitegrid", font_scale=1.2)

plt.figure(figsize=(10, 6))

g = sns.histplot(data=df["size"], palette="colorblind")
g.set_yscale("log")

plt.title("Distribution of Community Sizes")
plt.xlabel("Community Size")
plt.ylabel("Frequency (log)")

sns.despine()
plt.tight_layout()
plt.savefig("topological_patterns/community_size_distribution.png", dpi=300)
