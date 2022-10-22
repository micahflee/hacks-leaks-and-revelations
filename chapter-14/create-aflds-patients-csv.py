import json
import csv
import os


# Turn a JSON file into a Python dict or list
def data_from_json(filename):
    with open(filename) as f:
        return json.loads(f.read())


# Export a CSV full of AFLDS patients
def main():
    # Load patient data from cadence_allpatients_all.json
    patients_data = data_from_json(
        "data/horse_around_find_out/cadence_allpatients_all.json"
    )
    # Keep track of the created_at timestamps for each patient's id
    patient_ids_to_created_at = {}
    for patient in patients_data["patients"]:
        patient_ids_to_created_at[patient["id"]] = patient["created_at"]

    # Start the list of AFLDS patients that have had at least one consultation
    patient_rows = []

    # Loop through every file in the hipaa_special folder
    for patient_id in os.listdir("data/hipaa_special"):
        # Load the patient data
        data = data_from_json(os.path.join("data/hipaa_special", patient_id))

        # Some of the patient records are empty. This skips them
        if not data["result"]:
            continue

        # Make sure AFLDS (id 3) is in the list of partners
        partner_ids = data["provider"]["partner"].split(",")
        if "3" in partner_ids:
            # Count how many consultations this patient has
            num_consultations = len(data["provider"]["consultationNotes"])

            # If they have had more than one, add them to the list
            if num_consultations > 0:
                patient_rows.append(
                    {
                        "user_id": data["provider"]["user_id"],
                        "created_at": patient_ids_to_created_at[data["provider"]["user_id"]],
                        "fname": data["provider"]["fname"],
                        "lname": data["provider"]["lname"],
                        "email": data["provider"]["email"],
                        "city": data["provider"]["city"],
                        "state": data["provider"]["state"],
                        "gender": data["provider"]["gender"],
                        "birthdate": data["provider"]["birthdate"],
                        "num_consultations": num_consultations,
                    }
                )

    # Write the CSV file
    csv_filename = "aflds-patients.csv"
    headers = [
        "user_id",
        "created_at",
        "fname",
        "lname",
        "email",
        "city",
        "state",
        "gender",
        "birthdate",
        "num_consultations",
    ]
    with open(csv_filename, "w") as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(patient_rows)


main()
