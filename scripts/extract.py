"""
extract.py

This module handles data extraction from processed datasets.
"""

import os
import pandas as pd


def extract_data():

    """
    Reads mutual fund datasets from the processed data folder.

    Returns:
        dict: Dictionary containing loaded DataFrames.
    """

    data_path = "data/processed"

    datasets = {}

    for file in os.listdir(data_path):

        if file.endswith(".csv"):

            file_path = os.path.join(data_path, file)

            datasets[file.replace(".csv", "")] = pd.read_csv(file_path)

    return datasets