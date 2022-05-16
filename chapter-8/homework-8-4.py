import click
import csv
import os


@click.command()
@click.argument("blueleaks_path")
@click.argument("output_csv_path")
def main(blueleaks_path, output_csv_path):
    """Make a CSV that describes all the BlueLeaks folders"""
    
    # Set up the CSV writer
    headers = ["BlueLeaksFolder", "CompanyID", "CompanyName", "WebsiteTitle", "URL"]
    with open(output_csv_path, "w") as output_f:
        writer = csv.DictWriter(output_f, fieldnames=headers)
        writer.writeheader()

        # List all of the folders in BlueLeaks
        for folder_name in os.listdir(blueleaks_path):
            # Define the Company.csv path for each folder
            company_csv_abs_path = os.path.join(blueleaks_path, folder_name, "Company.csv")
            # If this path exists...
            if os.path.exists(company_csv_abs_path):
                
                # Set up the CSV reader
                with open(company_csv_abs_path) as input_f:
                    reader = csv.DictReader(input_f)
                    for row in reader:
                        output_row = {
                            "BlueLeaksFolder": folder_name,
                            "CompanyID": row["CompanyID"],
                            "CompanyName": row["CompanyName"],
                            "WebsiteTitle": row["WebsiteTitle"],
                            "URL": row["URL"],
                        }
                        writer.writerow(output_row)
            
                print(f"Finished: {folder_name}")


if __name__ == "__main__":
    main()
