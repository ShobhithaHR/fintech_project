"""
load.py

This module saves transformed mutual fund datasets
into the processed output location.
"""

import os


def load_data(datasets):

    """
    Saves cleaned datasets as CSV files.

    Parameters:
        datasets (dict): Dictionary containing cleaned DataFrames.

    Returns:
        None
    """

    output_path = "data/processed"

    os.makedirs(output_path, exist_ok=True)

    for name, df in datasets.items():

        file_path = os.path.join(
            output_path,
            f"{name}.csv"
        )

        df.to_csv(
            file_path,
            index=False
        )

    print("Data loading completed successfully.")