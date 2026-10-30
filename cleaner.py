import csv
import argparse


def clean_csv(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8-sig", newline="") as f:
            rows = list(csv.reader(f))

        if not rows:
            print("Error: CSV file is empty.")
            return

        header = rows[0]
        data = rows[1:]

        unique_rows = []
        seen = set()

        for row in data:
            if not any(cell.strip() for cell in row):
                continue

            key = tuple(row)

            if key not in seen:
                seen.add(key)
                unique_rows.append(row)

        removed = len(data) - len(unique_rows)

        with open(output_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(unique_rows)

        print("\nCSV Cleaner Pro")
        print("----------------------")
        print(f"Original rows: {len(data)}")
        print(f"Cleaned rows: {len(unique_rows)}")
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
    parser.add_argument("-o", "--output", default="cleaned.csv")

    args = parser.parse_args()
    clean_csv(args.input, args.output)
