CREATE TABLE dim_fund (
    fund_key INTEGER PRIMARY KEY,
    amfi_code INTEGER UNIQUE,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    risk_grade TEXT
);

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    quarter INTEGER,
    day INTEGER
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    nav_date DATE,
    nav REAL,
    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    investor_id TEXT,
    amfi_code INTEGER,
    transaction_date DATE,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    kyc_status TEXT,
    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,
    aum_crore REAL,
    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    aum_crore REAL,
    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);