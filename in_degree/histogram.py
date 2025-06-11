import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 16,
    "axes.labelsize": 14,
    "figure.figsize": (10, 6),
    "axes.spines.top": False,
    "axes.spines.right": False
})

df = pd.read_csv("in_degree/data.csv")

nonzero = df[df['in_degree'] > 0]

bins = np.logspace(0, np.log10(nonzero['in_degree'].max()), 50)

plt.figure(figsize=(10, 6))
plt.hist(nonzero['in_degree'], bins=bins, color='#1f77b4', edgecolor='black', alpha=0.8)

plt.xscale('log')
plt.yscale('log')

plt.xlabel("In-degree (Number of Models Reusing a Given Model)")
plt.ylabel("Frequency (Number of Models)")
plt.title("Log-Log Histogram of Model Reuse (In-Degree)")

plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()

plt.savefig("in_degree/histogram.png", dpi=300)

plt.show()
