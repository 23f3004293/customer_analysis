# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic realistic data
np.random.seed(42)
n = 100
acquisition_cost = np.random.uniform(50, 500, n)  # Marketing spend per customer
lifetime_value = acquisition_cost * np.random.uniform(3, 8, n) + np.random.normal(0, 500, n)

data = pd.DataFrame({
    'Acquisition_Cost': acquisition_cost,
    'Lifetime_Value': lifetime_value
})

# Create 512x512 scatterplot
plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512 pixels
sns.scatterplot(
    x='Acquisition_Cost',
    y='Lifetime_Value',
    data=data,
    palette='viridis',
    hue='Acquisition_Cost',
    legend=False
)

# Titles and labels
plt.title("Customer Lifetime Value vs Acquisition Cost", fontsize=16, weight='bold')
plt.xlabel("Acquisition Cost ($)", fontsize=14)
plt.ylabel("Lifetime Value ($)", fontsize=14)

# Save chart
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.close()
