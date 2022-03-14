import csv
from datetime import datetime, timedelta

# Export a CSV that shows how many patients are part of each age group
def main():
    headers = [
        "age_group",
        "patients",
    ]

    # Age groups, the same ones used in CDC data
    # https://www.cdc.gov/coronavirus/2019-ncov/covid-data/investigations-discovery/hospitalization-death-by-age.html
    age_groups = {
        "<0": 0,
        "0-4": 0,
        "5-17": 0,
        "18-29": 0,
        "30-39": 0,
        "40-49": 0,
        "50-64": 0,
        "65-74": 0,
        "75-84": 0,
        "85+": 0,
        ">100": 0,
    }

    sept2021 = datetime(2021, 9, 11)

    with open("aflds-patients.csv") as f:
        reader = csv.DictReader(f)

        for row in reader:
            birthdate = datetime.strptime(row["birthdate"], "%m/%d/%Y")
            age = sept2021 - birthdate

            if age < timedelta(0):
                age_groups["<0"] += 1
            elif age < timedelta(365 * 5):
                age_groups["0-4"] += 1
            elif age < timedelta(365 * 18):
                age_groups["5-17"] += 1
            elif age < timedelta(365 * 30):
                age_groups["18-29"] += 1
            elif age < timedelta(365 * 40):
                age_groups["30-39"] += 1
            elif age < timedelta(365 * 50):
                age_groups["40-49"] += 1
            elif age < timedelta(365 * 65):
                age_groups["50-64"] += 1
            elif age < timedelta(365 * 75):
                age_groups["65-74"] += 1
            elif age < timedelta(365 * 85):
                age_groups["75-84"] += 1
            elif age < timedelta(365 * 100):
                age_groups["85+"] += 1
            else:
                age_groups[">100"] += 1

    # Write the CSV file
    csv_filename = "ages.csv"
    with open(csv_filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for age_group in age_groups:
            writer.writerow(
                [
                    age_group,
                    age_groups[age_group],
                ]
            )


main()
