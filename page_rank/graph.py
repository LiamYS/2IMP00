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
df = pd.read_csv("page_rank/data.csv")

top10 = df.sort_values(by="score", ascending=False).head(10)

def shorten(name, max_len=40):
    return name if len(name) <= max_len else name[:max_len] + "..."

top10["short_model"] = top10["name"].apply(shorten)

# Bar plot
plt.figure(figsize=(12, 7))
barplot = sns.barplot(
    data=top10,
    x="score",
    y="short_model",
    palette="Blues_d",
    edgecolor='black'
)

# Add value labels to bars
for index, row in top10.iterrows():
    plt.text(row.score + 50, index, f"{row.score:,}", va='center', fontsize=11)

# Labels and title
plt.xlabel("PageRank Score")
plt.ylabel("Model")
plt.title("Top 10 Most Reused Models in the Hugging Face Ecosystem")

# Tight layout and optional save
plt.tight_layout()
plt.savefig("page_rank/graph.png", dpi=300)
plt.show()
