import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("attribute_influence/export.csv")

attributes = ["pipeline_tag", "license", "library_name", "model_type"]

results = []
for attr in attributes:
    flag_col = f"has_{attr}"
    
    df[flag_col] = df[attr].notna().astype(int)
    
    summary = df.groupby(flag_col)["reuse_count"].agg(["count", "mean", "median"])
    summary.index = [f"No {attr}", f"Has {attr}"]

    results.append({
        "attribute": attr,
        "count_present": summary.loc[f"Has {attr}", "count"],
        "mean_present": summary.loc[f"Has {attr}", "mean"],
        "count_absent": summary.loc[f"No {attr}", "count"],
        "mean_absent": summary.loc[f"No {attr}", "mean"],
    })

summary_df = pd.DataFrame(results)

plot_df = pd.melt(
    summary_df,
    id_vars="attribute",
    value_vars=["mean_present", "mean_absent"],
    var_name="presence",
    value_name="mean_reuse"
)

plot_df["presence"] = plot_df["presence"].map({
    "mean_present": "Has Attribute",
    "mean_absent": "No Attribute"
})

sns.set_theme(style="whitegrid", font_scale=1.2)
plt.figure(figsize=(10, 6))
ax = sns.barplot(
    data=plot_df,
    x="attribute", y="mean_reuse", hue="presence",
)

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f", label_type="edge", fontsize=10, padding=3)

plt.xlabel("Attribute")
plt.ylabel("Mean Reuse Count")
plt.title("Influence of Metadata Attributes on Model Reuse")
plt.legend(title="", loc="upper right")
sns.despine()
plt.tight_layout()
plt.savefig("attribute_influence/attribute_influence.png", dpi=300)