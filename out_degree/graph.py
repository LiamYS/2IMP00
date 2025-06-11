import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set publication-style aesthetics
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 16,
    "axes.labelsize": 14,
    "figure.figsize": (12, 7),
    "axes.spines.top": False,
    "axes.spines.right": False
})

# Load CSV file
df = pd.read_csv("out_degree/data.csv")

top10 = df.sort_values(by="out_degree", ascending=False).head(10)

# Optional: Shorten long model names for clarity
def shorten(name, max_len=40):
    return name if len(name) <= max_len else name[:max_len] + "..."

top10["short_model"] = top10["model"].apply(shorten)

# Bar plot
plt.figure(figsize=(12, 7))
barplot = sns.barplot(
    data=top10,
    x="out_degree",
    y="short_model",
    palette="Blues_d",
    edgecolor='black'
)

# Add value labels to bars
for index, row in top10.iterrows():
    plt.text(row.out_degree + 50, index, f"{row.out_degree:,}", va='center', fontsize=11)

# Labels and title
plt.xlabel("Number of Downstream Models (Out-Degree)")
plt.ylabel("Model")
plt.title("Top 10 Most Reusing Models in the Hugging Face Ecosystem")

# Tight layout and optional save
plt.tight_layout()
plt.savefig("out_degree/graph.png", dpi=300)
plt.show()
