"""
run_pipeline.py

Master script to execute the complete
Mutual Fund ETL pipeline.
"""


from extract import extract_data
from transform import transform_data
from load import load_data


def main():

    """
    Executes the complete ETL workflow.
    """

    print("Starting ETL Pipeline...")

    # Extract data
    raw_data = extract_data()

    print("Data extraction completed.")

    # Transform data
    cleaned_data = transform_data(raw_data)

    print("Data transformation completed.")

    # Load data
    load_data(cleaned_data)

    print("ETL Pipeline completed successfully.")


if __name__ == "__main__":
    main()