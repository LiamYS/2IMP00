import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", font_scale=1.2)

df = pd.read_csv("page_rank/export.csv")

top10 = df.sort_values(by="score", ascending=False).head(10)

def shorten(name, max_len=40):
    return name if len(name) <= max_len else name[:max_len] + "..."

top10["short_model"] = top10["name"].apply(shorten)

plt.figure(figsize=(10, 6))
barplot = sns.barplot(
    data=top10,
    x="score",
    y="short_model"
)

for container in barplot.containers:
    barplot.bar_label(container, fmt="%.1f", label_type="edge", fontsize=10, padding=3)

plt.xlabel("PageRank Score")
plt.ylabel("Model")
plt.title("Top 10 Most Reused Models in the Hugging Face Ecosystem")

plt.tight_layout()
plt.savefig("page_rank/graph.png", dpi=300)
plt.show()
