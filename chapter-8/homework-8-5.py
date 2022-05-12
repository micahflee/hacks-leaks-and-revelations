import click
import os
import json
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def is_point_in_washington_dc(x, y):
    washington_dc_x = -77.00667073028771
    washington_dc_y = 38.894101636006035
    return distance(washington_dc_x, washington_dc_y, x, y) <= 0.25


def gps_degrees_to_decimal(gps_coordinate):
    parts = gps_coordinate.split()
    degrees = float(parts[0])
    minutes = float(parts[2].replace("'", ""))
    seconds = float(parts[3].replace('"', ""))
    hemisphere = parts[4]
    gps_decimal = degrees + (minutes / 60) + (seconds / 3600)
    if hemisphere == "W" or hemisphere == "S":
        gps_decimal *= -1
    return gps_decimal


@click.command()
@click.argument("parler_metadata_path")
def main(parler_metadata_path):
    """Create a GeoJSON file containing Parler GPS coordinates"""
    # The list of GPS points
    points = []

    # Number of videos with GPS coordinates in their metadata
    count = 0

    for filename in os.listdir(parler_metadata_path):
        abs_filename = os.path.join(parler_metadata_path, filename)
        if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
            with open(abs_filename, "rb") as f:
                json_data = f.read()

            metadata = json.loads(json_data)
            if "GPSCoordinates" in metadata[0]:
                count += 1
                print(f"\rFound {count:,} videos with GPS coordinates", end="")

                longitude_decimal = gps_degrees_to_decimal(metadata[0]["GPSLongitude"])
                latitude_decimal = gps_degrees_to_decimal(metadata[0]["GPSLatitude"])
                points.append([longitude_decimal, latitude_decimal, filename])

    print()

    # Save the CSV spreadsheet
    with open("parler-videos.csv", "w") as f:
        for point in points:
            f.write(f"{point[0]},{point[1]},{point[2]}\n")

    print("Wrote file: parler-videos.csv")


if __name__ == "__main__":
    main()
