import click
import os
import json


@click.command()
@click.argument("parler_metadata_path")
def main(parler_metadata_path):
    """Filter Parler videos that have GPS coordinates"""
    # Number of videos with GPS coordinates in their metadata
    count = 0

    for filename in os.listdir(parler_metadata_path):
        abs_filename = os.path.join(parler_metadata_path, filename)
        if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
            with open(abs_filename, "rb") as f:
                json_data = f.read()

            metadata = json.loads(json_data)
            if "GPSCoordinates" in metadata[0]:
                print(f"Found GPS coordinates: {abs_filename}")
                count += 1

    print(f"Total videos with GPS coordinates: {count}")


if __name__ == "__main__":
    main()
