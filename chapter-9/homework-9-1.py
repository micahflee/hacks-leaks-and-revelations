import click
import csv


@click.command()
@click.argument("csv_path")
def main(csv_path):
    """Make BlueLeaks CSVs easier to read"""
    # Loop through the rows of the CSV
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Loop through the keys in the dictionary
            for key in row:
                if row[key] != "":
                    print(f"{key}: {row[key]}")
            print("===")


if __name__ == "__main__":
    main()
