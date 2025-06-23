import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("attribute_influence/export.csv")

sns.set_theme(style="whitegrid", font_scale=1.2)

plt.figure(figsize=(10, 6))

g = sns.histplot(data=df["reuse_count"], palette="colorblind", log_scale=True, bins=17)

plt.title("Distribution of Reuse Counts")
plt.xlabel("Reuse Count (log)")
plt.ylabel("Frequency")

sns.despine()
plt.tight_layout()
plt.savefig("attribute_influence/reuse_distribution_log.png", dpi=300)
