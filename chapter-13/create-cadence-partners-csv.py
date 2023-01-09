import json
import csv

# Turn a JSON file into a Python dict or list
def data_from_json(filename):
    with open(filename) as f:
        return json.loads(f.read())


# Convert the comma-separated list of partners, like ",3,", into a Python list
# of partners, like ["America's Frontline Doctors"]
def get_partners(partner_lookup, patient):
    partners = []
    partner_ids = patient["partner"].split(",")
    for partner_id in partner_ids:
        if partner_id != "":
            partners.append(partner_lookup[int(partner_id)])

    return partners


# Export a CSV that lists Cadence partners
def main():
    """
    List Cadence partners
    """
    partner_rows = []

    # Load the Cadence patient data
    patients_data = data_from_json(
        "data/horse_around_find_out/cadence_allpatients_all.json"
    )

    # Load the Cadence partners data
    partners_data = data_from_json(
        "data/horse_around_find_out/cadence_health_partners.json"
    )

    # Create a dictionary that maps a partner ID with its name
    partner_lookup = {}
    for partner in partners_data:
        partner_lookup[partner["id"]] = partner["name"]

    # Loop through all of the partners
    for partner in partners_data:
        # Count how many patients use this partner
        patients = 0
        for patient in patients_data["patients"]:
            patient_partners = get_partners(partner_lookup, patient)
            for patient_partner in patient_partners:
                if patient_partner == partner["name"]:
                    patients += 1

        # Add the partner's row
        partner_rows.append(
            {
                "ID": partner["id"],
                "Name": partner["name"],
                "Domain": partner["domain"],
                "Patients": patients,
            }
        )

    # Write the CSV file
    headers = ["ID", "Name", "Domain", "Patients"]
    csv_filename = "cadence-partners.csv"
    with open(csv_filename, "w") as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(partner_rows)


if __name__ == "__main__":
    main()
