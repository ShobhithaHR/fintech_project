import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

tables = {
    "dim_fund":
        "data/raw/01_fund_master.csv",

    "fact_nav":
        "data/processed/02_nav_history_clean.csv",

    "fact_performance":
        "data/processed/07_scheme_performance_clean.csv",

    "fact_transactions":
        "data/processed/08_investor_transactions_clean.csv",

    "fact_aum":
        "data/raw/03_aum_by_fund_house.csv"
}

for table, path in tables.items():

    df = pd.read_csv(path)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table} loaded:",
        len(df),
        "rows"
    )

print("\nDatabase created successfully")