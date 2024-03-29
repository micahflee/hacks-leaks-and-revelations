import csv

# Export a CSV that adds up prescriptions and their costs for each category of drug
def main():
    # A dictionary that maps drug categories to another dictionary containing the
    # prescription count and total cost for that drug category
    drug_categories = {}

    # Loop through ravkoo_rxdata.csv, and count prescriptions and costs
    with open("data/horse_around_find_out/ravkoo_rxdata.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if "ivermectin" in row["DrugName"].lower():
                category = "Ivermectin"
            elif "hydroxychloroquine" in row["DrugName"].lower():
                category = "Hydroxychloroquine"
            elif "azithromycin" in row["DrugName"].lower():
                category = "Azithromycin"
            elif "zinc" in row["DrugName"].lower():
                category = "Zinc"
            elif "vitamin c" in row["DrugName"].lower():
                category = "Vitamin C"
            else:
                category = "Other"

            if category not in drug_categories:
                drug_categories[category] = {"prescription_count": 0, "total_cost": 0}

            # Count prescriptions and cost for this drug category
            drug_categories[category]["prescription_count"] += 1
            drug_categories[category]["total_cost"] += float(row["Cost"])

    # Write the CSV file
    headers = [
        "drug_category",
        "prescription_count",
        "total_cost",
    ]
    csv_filename = "ravkoo-categories.csv"
    with open(csv_filename, "w") as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        for category in drug_categories:
            writer.writerow(
                {
                    "drug_category": category,
                    "prescription_count": drug_categories[category][
                        "prescription_count"
                    ],
                    "total_cost": int(drug_categories[category]["total_cost"]),
                }
            )


if __name__ == "__main__":
    main()
