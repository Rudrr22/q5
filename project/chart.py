import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy.random as npr

# Professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data
npr.seed(42)
categories = ["Electronics", "Home Appliances", "Clothing", "Groceries", "Sports"]
scores = npr.uniform(3.2, 4.8, size=len(categories))

df = pd.DataFrame({
    "Product Category": categories,
    "Avg Satisfaction Score": scores
})

# Create exact 512×512 figure
plt.figure(figsize=(8, 8), dpi=64)  # 8 inches * 64 DPI = 512 px

sns.barplot(
    data=df,
    x="Product Category",
    y="Avg Satisfaction Score",
    palette="viridis"
)

plt.title("Average Customer Satisfaction by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Avg Satisfaction Score (1–5)")
plt.xticks(rotation=30)

plt.tight_layout()  # Do NOT use bbox_inches='tight' when saving

# Save WITHOUT bbox_inches to keep exact size
plt.savefig("chart.png", dpi=64)
plt.close()
