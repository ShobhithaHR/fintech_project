"""
transform.py

This module performs data cleaning and transformation
for mutual fund datasets.
"""


def transform_data(datasets):

    """
    Cleans extracted datasets.

    Parameters:
        datasets (dict): Dictionary of pandas DataFrames.

    Returns:
        dict: Cleaned datasets.
    """

    cleaned_data = {}

    for name, df in datasets.items():

        # Remove duplicate records
        df = df.drop_duplicates()

        # Standardize column names
        df.columns = (
            df.columns
            .str.lower()
            .str.strip()
            .str.replace(" ", "_")
        )

        # Handle missing values
        df = df.dropna()

        cleaned_data[name] = df

    return cleaned_data