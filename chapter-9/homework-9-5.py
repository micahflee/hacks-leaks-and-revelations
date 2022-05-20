import click
import csv
import json
import os


def gps_degrees_to_decimal(gps_coordinate):
    # print(f"gps_coordinate: {gps_coordinate}")
    parts = gps_coordinate.split()
    degrees = float(parts[0])
    minutes = float(parts[2].replace("'", ""))
    seconds = float(parts[3].replace('"', ""))
    hemisphere = parts[4]
    gps_decimal = degrees + (minutes / 60) + (seconds / 3600)
    if hemisphere == "W" or hemisphere == "S":
        gps_decimal *= -1
    return gps_decimal


def convert_filename(json_filename):
    return json_filename.split("-")[1].split(".")[0]


@click.command()
@click.argument("parler_metadata_path")
@click.argument("output_csv_path")
def main(parler_metadata_path, output_csv_path):
    """Create a CSV of GPS coordinates from Parler metadata"""

    # Open the output CSV file for writing
    with open(output_csv_path, "w") as output_f:
        writer = csv.DictWriter(
            output_f, fieldnames=["Filename", "Longitude", "Latitude"]
        )
        writer.writeheader()

        for filename in os.listdir(parler_metadata_path):
            abs_filename = os.path.join(parler_metadata_path, filename)
            if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
                with open(abs_filename, "rb") as f:
                    json_data = f.read()

                metadata = json.loads(json_data)
                if (
                    "GPSLongitude" in metadata[0]
                    and "GPSLatitude" in metadata[0]
                    and metadata[0]["GPSLongitude"] != ""
                    and metadata[0]["GPSLatitude"] != ""
                ):
                    # Save the row
                    row = {
                        "Filename": convert_filename(filename),
                        "Longitude": gps_degrees_to_decimal(
                            metadata[0]["GPSLongitude"]
                        ),
                        "Latitude": gps_degrees_to_decimal(metadata[0]["GPSLatitude"]),
                    }
                    writer.writerow(row)
                    print(row)

    print(f"Saved: {output_csv_path}")


if __name__ == "__main__":
    main()
