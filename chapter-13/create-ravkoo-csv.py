import csv


# Export a CSV that adds up prescriptions and their costs for each drug
def main():
    # A dictionary that maps drug names to another dictionary containing the
    # prescription count and total cost for that drug
    drugs = {}

    # Add up the number of prescriptions and total cost for all drugs, to display
    # at the end
    prescription_count = 0
    total_cost = 0

    # Loop through ravkoo_rxdata.csv, and count prescriptions and costs
    with open("data/horse_around_find_out/ravkoo_rxdata.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["DrugName"] not in drugs:
                drugs[row["DrugName"]] = {"prescription_count": 0, "total_cost": 0}

            # Count prescriptions and cost for this drug
            drugs[row["DrugName"]]["prescription_count"] += 1
            drugs[row["DrugName"]]["total_cost"] += float(row["Cost"])

            # Count prescriptions and cost for _all_ drugs
            prescription_count += 1
            total_cost += float(row["Cost"])

    # Write the CSV file
    headers = [
        "drug_name",
        "prescription_count",
        "total_cost",
    ]
    csv_filename = "ravkoo.csv"
    with open(csv_filename, "w") as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        for drug_name in drugs:
            writer.writerow(
                {
                    "drug_name": drug_name,
                    "prescription_count": drugs[drug_name]["prescription_count"],
                    "total_cost": int(drugs[drug_name]["total_cost"]),
                }
            )

    print(f"Number of prescriptions: {prescription_count:,}")
    print(f"Total cost: ${int(total_cost):,}")


if __name__ == "__main__":
    main()
