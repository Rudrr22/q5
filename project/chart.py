import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# ---- Generate Synthetic Business Data ----
np.random.seed(42)

categories = ["Electronics", "Home Appliances", "Clothing", "Groceries", "Sports"]
avg_scores = np.random.uniform(3.2, 4.8, size=len(categories))

df = pd.DataFrame({
    "Product Category": categories,
    "Avg Satisfaction Score": avg_scores
})

# ---- Create Barplot ----
plt.figure(figsize=(8, 8))  # 8×8 inches at 64 dpi → 512×512 pixels

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

# ---- Export the Chart ----
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
