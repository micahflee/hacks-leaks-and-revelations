import json
import csv
import os


# Turn a JSON file into a Python dict or list
def data_from_json(filename):
    with open(filename) as f:
        return json.loads(f.read())


# Export a CSV full of AFLDS patients
def main():
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
    patient_rows = []

    # Load patient data
    patients_data = data_from_json(
        "data/horse_around_find_out/cadence_allpatients_all.json"
    )
    patient_ids_to_created = {}
    for patient in patients_data["patients"]:
        patient_ids_to_created[patient["id"]] = patient["created_at"]

    # Make a list of patients from Cadence's AFLDS partner, and that have had
    # at least one consultation
    for patient_id in os.listdir("data/hipaa_special"):
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
                    [
                        data["provider"]["user_id"],
                        patient_ids_to_created[data["provider"]["user_id"]],
                        data["provider"]["fname"],
                        data["provider"]["lname"],
                        data["provider"]["email"],
                        data["provider"]["city"],
                        data["provider"]["state"],
                        data["provider"]["gender"],
                        data["provider"]["birthdate"],
                        num_consultations,
                    ]
                )

    # Write the CSV file
    csv_filename = "aflds-patients.csv"
    with open(csv_filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(patient_rows)


main()
