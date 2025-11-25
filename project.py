import pandas as pd

# ----------------------------------------------------------
# 1. Load the datasets
# ----------------------------------------------------------
customers = pd.read_csv("customers.csv")
sales = pd.read_csv("sales.csv")

print("Original Customers Data:")
print(customers)
print("\nOriginal Sales Data:")
print(sales)

# ----------------------------------------------------------
# 2. Clean Customer Data
# ----------------------------------------------------------

# Remove duplicate customers
customers = customers.drop_duplicates("customer_id")

# ----------------------------------------------------------
# 3. Clean Sales Data
# ----------------------------------------------------------

# Fill missing amount with 0
sales["amount"] = sales["amount"].fillna(0)

# Remove duplicate rows
sales = sales.drop_duplicates()

# Sort sales by amount (highest first)
sales = sales.sort_values("amount", ascending=False)

# ----------------------------------------------------------
# 4. Merge the datasets (VERY IMPORTANT)
# ----------------------------------------------------------
merged_df = pd.merge(sales, customers, on="customer_id", how="left")

print("\nMerged Data:")
print(merged_df)

# ----------------------------------------------------------
# 5. Analysis
# ----------------------------------------------------------

# (A) Total spending per customer
customer_spending = merged_df.groupby("customer_name")["amount"].sum()
print("\nTotal Spending Per Customer:")
print(customer_spending)

# (B) Total sales by category
category_sales = merged_df.groupby("category")["amount"].sum()
print("\nTotal Sales by Category:")
print(category_sales)

# (C) Top customer (max spending)
top_customer = customer_spending.idxmax()
top_amount = customer_spending.max()
print(f"\nTop Customer: {top_customer} | Amount: {top_amount}")

# ----------------------------------------------------------
# 6. Export results
# ----------------------------------------------------------

merged_df.to_csv("cleaned_merged_data.csv", index=False)
customer_spending.to_csv("customer_spending_report.csv")
category_sales.to_csv("category_sales_report.csv")

print("\nFiles Exported Successfully:")
print("- cleaned_merged_data.csv")
print("- customer_spending_report.csv")
print("- category_sales_report.csv")
