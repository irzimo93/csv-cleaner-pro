
import pandas as pd
import argparse


def clean_csv(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        original_rows = len(df)

        df = df.drop_duplicates()
        df = df.dropna(how="all")

        removed = original_rows - len(df)

        df.to_csv(output_file, index=False)

        print("CSV Cleaner Pro")
        print("--------------------")
        print(f"Original rows: {original_rows}")
        print(f"Cleaned rows: {len(df)}")
        print(f"Removed rows: {removed}")
        print(f"Output file: {output_file}")

    except FileNotFoundError:
        print("Error: File not found.")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CSV Cleaner Pro"
    )

    parser.add_argument("input")
    parser.add_argument(
        "-o", "--output",
        default="cleaned.csv"
    )

    args = parser.parse_args()
    clean_csv(args.input, args.output)
