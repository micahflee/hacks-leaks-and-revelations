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


def was_video_filmed_in_washington_dc(metadata):
    x = gps_degrees_to_decimal(metadata[0]["GPSLongitude"])
    y = gps_degrees_to_decimal(metadata[0]["GPSLatitude"])
    return is_point_in_washington_dc(x, y)


@click.command()
@click.argument("parler_metadata_path")
def main(parler_metadata_path):
    """Filter Parler videos that were filmed in Washington DC and on Jan 6, 2021"""
    count = 0

    for filename in os.listdir(parler_metadata_path):
        abs_filename = os.path.join(parler_metadata_path, filename)
        if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
            with open(abs_filename, "rb") as f:
                json_data = f.read()

            metadata = json.loads(json_data)
            if (
                "GPSLongitude" in metadata[0]
                and "GPSLatitude" in metadata[0]
                and "CreateDate" in metadata[0]
                and metadata[0]["CreateDate"].startswith("2021:01:06 ")
                and was_video_filmed_in_washington_dc(metadata)
            ):
                print(f"Found an insurrection video: {filename}")
                count += 1

    print(f"Total videos filmed in Washington DC on January 6: {count}")


if __name__ == "__main__":
    main()
