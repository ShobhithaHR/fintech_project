# Data Dictionary

## 01_fund_master.csv

| Column | Description |
|----------|-------------|
| amfi_code | Unique AMFI Scheme Code |
| scheme_name | Fund Name |
| fund_house | AMC Name |
| category | Fund Category |
| risk_grade | Risk Classification |

---

## 02_nav_history.csv

| Column | Description |
|----------|-------------|
| amfi_code | Scheme Code |
| date | NAV Date |
| nav | Net Asset Value |

---

## 08_investor_transactions.csv

| Column | Description |
|----------|-------------|
| investor_id | Investor Identifier |
| transaction_date | Date of Transaction |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Transaction Amount |
| state | Investor State |
| city | Investor City |
| kyc_status | KYC Verification Status |

---

## 07_scheme_performance.csv

| Column | Description |
|----------|-------------|
| return_1yr_pct | One Year Return |
| return_3yr_pct | Three Year Return |
| return_5yr_pct | Five Year Return |
| expense_ratio_pct | Expense Ratio |
| aum_crore | Assets Under Management |
| risk_grade | Risk Classification |