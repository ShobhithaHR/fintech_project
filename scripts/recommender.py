import pandas as pd

def recommend_funds(sharpe_df, risk_appetite):

    result = (
        sharpe_df[
            sharpe_df['risk_grade'] == risk_appetite
        ]
        .nlargest(3, 'sharpe_ratio')
    )

    return result[
        ['amfi_code',
         'sharpe_ratio',
         'risk_grade']
    ]