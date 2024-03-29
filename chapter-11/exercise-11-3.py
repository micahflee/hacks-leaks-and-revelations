import click
import os
import json
import math


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


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def was_video_filmed_in_dc(metadata):
    dc_x = -77.0066
    dc_y = 38.8941
    x = gps_degrees_to_decimal(metadata[0]["GPSLongitude"])
    y = gps_degrees_to_decimal(metadata[0]["GPSLatitude"])
    return distance(dc_x, dc_y, x, y) <= 0.25


@click.command()
@click.argument("parler_metadata_path")
def main(parler_metadata_path):
    """Filter Parler videos that were filmed in Washington DC and on Jan 6, 2021"""
    count = 0

    for filename in os.listdir(parler_metadata_path):
        abs_filename = os.path.join(parler_metadata_path, filename)
        if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
            with open(abs_filename) as f:
                json_data = f.read()

            try:
                metadata = json.loads(json_data)
            except json.decoder.JSONDecodeError:
                print(f"Invalid JSON: {filename}")
                continue

            if (
                "GPSLongitude" in metadata[0]
                and "GPSLatitude" in metadata[0]
                and "CreateDate" in metadata[0]
                and metadata[0]["CreateDate"].startswith("2021:01:06")
                and was_video_filmed_in_dc(metadata)
            ):
                print(f"Found an insurrection video: {filename}")
                count += 1

    print(f"Total insurrection videos filmed in Washington DC on January 6: {count:,}")


if __name__ == "__main__":
    main()
