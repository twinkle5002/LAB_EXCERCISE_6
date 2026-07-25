import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# Generate 50 records for a Retail/E-Commerce domain
categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Sports"]
regions = ["North", "South", "East", "West"]

data = {
    "OrderID": [100 + i for i in range(1, 51)],
    "Category": np.random.choice(categories, size=50),
    "Region": np.random.choice(regions, size=50),
    "Quantity": np.random.randint(1, 10, size=50),
    "UnitPrice": np.round(np.random.uniform(10.0, 500.0, size=50), 2),
    "Rating": np.round(np.random.uniform(1.0, 5.0, size=50), 1),
}

df = pd.DataFrame(data)
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]

# Save to CSV
df.to_csv("data.csv", index=False)
print("data.csv with 50 records generated successfully!")