import click
import os
import json


@click.command()
@click.argument("parler_metadata_path")
def main(parler_metadata_path):
    """Filter Parler videos that have GPS coordinates and were filmed Jan 6, 2021"""
    count = 0

    nw_latitude = 38.993388
    nw_longitude = -77.140210
    se_latitude = 38.851288
    se_longitude = -76.875830

    for filename in os.listdir(parler_metadata_path):
        abs_filename = os.path.join(parler_metadata_path, filename)
        if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
            with open(abs_filename, "rb") as f:
                json_data = f.read()

            metadata = json.loads(json_data)
            if "GPSCoordinates" in metadata[0] and metadata[0]["CreateDate"].startswith(
                "2021:01:06 "
            ):
                print(f"Found GPS coordinates, filmed Jan 6: {filename}")
                count += 1

    print(f"Total videos with GPS coordinates, filmed Jan 6: {count}")


if __name__ == "__main__":
    main()
