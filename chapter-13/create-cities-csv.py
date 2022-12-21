import csv
import json
import time
import httpx

# This script requires the third-party module httpx, which you can install like:
# python3 -m pip install httpx

# This also requires an API key for https://geocodeapi.io, a service I used to do
# geocoding. They have a free plan
geocode_api_key = "PUT_GEOCODE_API_KEY_HERE"


# Export a CSV that for each city lists its GPS coordinates and the number of patients there
def main():
    # This dictionary maps names of cities (in format "City, State", like "New York, NY")
    # to a dictionary with info about that city (number of patients, GPS coordinates)
    cities = {}

    # Count how many patients are in each city
    with open("aflds-patients.csv") as f:
        reader = csv.DictReader(f)

        for row in reader:
            city = f"{row['city']}, {row['state']}"

            if city not in cities:
                cities[city] = {"count": 0}

            cities[city]["count"] += 1

    print(f"Found patients in {len(cities):,} cities")

    # Look up GPS coordinates for each city
    for city in cities:

        # Give each API request 3 tries, in case a connection fails
        tries = 0
        success = False
        while not success:
            try:
                print(
                    f"Loading GPS coordinates for: {city} ({cities[city]['count']} patients)"
                )
                r = httpx.get(
                    "https://app.geocodeapi.io/api/v1/search",
                    params={
                        "apikey": geocode_api_key,
                        "text": city,
                        "size": 1,
                        "boundary.country": "US",
                    },
                )
                success = True

            # The connection failed
            except:
                tries += 1
                if tries == 3:
                    print("Failed, skipping")

                print("Sleeping 2s and trying again")
                time.sleep(2)

        try:
            data = json.loads(r.text)
            if "features" in data and len(data["features"]) > 0:
                cities[city]["lon"] = data["features"][0]["geometry"]["coordinates"][0]
                cities[city]["lat"] = data["features"][0]["geometry"]["coordinates"][1]
        except:
            cities[city]["lon"] = None
            cities[city]["lat"] = None

    # Write the CSV file
    headers = [
        "count",
        "city",
        "lon",
        "lat",
        "label",
    ]
    csv_filename = "cities.csv"
    with open(csv_filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for city in cities:
            writer.writerow(
                {
                    "count": cities[city]["count"],
                    "city": city,
                    "lon": cities[city]["lat"],
                    "lat": cities[city]["lon"],
                    "label": f"{city} ({cities[city]['count']})",
                }
            )


main()
