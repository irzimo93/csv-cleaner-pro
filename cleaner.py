
import pandas as pd
import argparse
from pathlib import Path


def clean_csv(input_file, output_file):
    try:
        df = pd.read_csv(input_file)

        original_rows = len(df)

        df = df.drop_duplicates()
        df = df.dropna(how="all")

        cleaned_rows = len(df)
        removed_rows = original_rows - cleaned_rows

        df.to_csv(output_file, index=False)

        print("\nCSV Cleaner Pro")
        print("----------------------")
        print(f"Original rows: {original_rows}")
        print(f"Cleaned rows: {cleaned_rows}")
        print(f"Removed rows: {removed_rows}")
        print(f"Saved to: {output_file}")

    except FileNotFoundError:
        print("Error: Input file not found.")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CSV Cleaner Pro - Clean CSV files"
    )

    parser.add_argument("input", help="Input CSV file")
    parser.add_argument(
        "-o",
        "--output",
        default="cleaned.csv",
        help="Output CSV file"
    )

    args = parser.parse_args()

    clean_csv(args.input, args.output)
