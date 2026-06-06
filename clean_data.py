import pandas as pd

print("Cleaning nav_history...")

nav = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", nav.shape)

# Convert date column
nav["date"] = pd.to_datetime(nav["date"], errors="coerce")

# Sort records
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicates
before = len(nav)
nav = nav.drop_duplicates()
after = len(nav)

print("Duplicates Removed:", before - after)

# Forward fill NAV within each fund
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Check invalid NAV values
invalid_nav = nav[nav["nav"] <= 0]

print("Invalid NAV Records:", len(invalid_nav))

# Save cleaned file
nav.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("nav_history cleaned successfully")
print("\nCleaning investor_transactions...")

txn = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", txn.shape)

# Check columns
print("\nColumns:")
print(txn.columns.tolist())

# Standardize transaction type

txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

txn["transaction_type"] = txn["transaction_type"].replace({
    "SIP": "SIP",
    "LUMPSUM": "Lumpsum",
    "REDEMPTION": "Redemption"
})

print("\nTransaction Types:")
print(txn["transaction_type"].value_counts())

# Fix dates

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

print("\nInvalid Dates:",
      txn["transaction_date"].isna().sum())

# Validate amount

invalid_amount = txn[
    txn["amount_inr"] <= 0
]

print("Invalid Amount Records:",
      len(invalid_amount))

# Validate KYC

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

invalid_kyc = txn[
    ~txn["kyc_status"].isin(valid_kyc)
]

print("Invalid KYC Records:",
      len(invalid_kyc))

# Remove duplicate rows

before = len(txn)
txn = txn.drop_duplicates()
after = len(txn)

print("Duplicates Removed:",
      before - after)

# Save cleaned file

txn.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("investor_transactions cleaned successfully")

print("\nCleaning scheme_performance...")

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Original Shape:", perf.shape)

print("\nColumns:")
print(perf.columns.tolist())

# Convert return columns to numeric

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Check missing values after conversion

print("\nMissing values after numeric conversion:")

for col in return_cols:
    print(col, ":", perf[col].isna().sum())

# Validate expense ratio

expense_anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]

print(
    "\nExpense Ratio Anomalies:",
    len(expense_anomalies)
)

# Check negative AUM

invalid_aum = perf[
    perf["aum_crore"] <= 0
]

print(
    "Invalid AUM Records:",
    len(invalid_aum)
)

# Remove duplicates

before = len(perf)
perf = perf.drop_duplicates()
after = len(perf)

print(
    "Duplicates Removed:",
    before - after
)

# Save cleaned file

perf.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print(
    "scheme_performance cleaned successfully"
)

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    df = pd.read_csv(f"data/raw/{file}")

    print(f"\nProcessing {file}")

    print("Shape:", df.shape)

    print("Missing Values:")
    print(df.isnull().sum().sum())

    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print("Duplicates Removed:", before - after)

    clean_name = file.replace(".csv", "_clean.csv")

    df.to_csv(
        f"data/processed/{clean_name}",
        index=False
    )