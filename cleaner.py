import csv
import argparse
from pathlib import Path


def clean_csv(input_file, output_file):
    source = Path(input_file).resolve()
    destination = Path(output_file).resolve()

    if source == destination:
        print("Error: Input and output files must be different.")
        return

    original = 0
    cleaned = 0
    removed = 0
    seen = set()

    try:
        with open(source, "r", encoding="utf-8-sig", newline="") as infile:
            reader = csv.reader(infile)
            header = next(reader, None)

            if header is None:
                print("Error: CSV file is empty.")
                return

            header = [cell.strip() for cell in header]

            with open(destination, "w", encoding="utf-8", newline="") as outfile:
                writer = csv.writer(outfile)
                writer.writerow(header)

                for row in reader:
                    original += 1
                    row = [cell.strip() for cell in row]

                    if not any(row):
                        removed += 1
                        continue

                    key = tuple(row)

                    if key in seen:
                        removed += 1
                        continue

                    seen.add(key)
                    writer.writerow(row)
                    cleaned += 1

        percentage = (removed / original * 100) if original else 0

        print("\nCSV Cleaner Pro 2.1")
        print("----------------------")
        print(f"Original rows: {original}")
        print(f"Cleaned rows: {cleaned}")
        print(f"Removed rows: {removed}")
        print(f"Cleanup rate: {percentage:.1f}%")
        print(f"Output file: {destination}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except csv.Error as error:
        print(f"CSV Error: {error}")
    except OSError as error:
        print(f"File Error: {error}")


parser = argparse.ArgumentParser(
    description="CSV Cleaner Pro - Clean CSV files"
)
parser.add_argument("input", help="Input CSV file")
parser.add_argument(
    "-o", "--output",
    default="cleaned.csv",
    help="Output CSV file"
)

args = parser.parse_args()
clean_csv(args.input, args.output)
