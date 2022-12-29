import click
import os
import json


@click.command()
@click.argument("parler_metadata_path")
def main(parler_metadata_path):
    """Filter Parler videos with GPS coordinates that were filmed Jan 6, 2021"""
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
                "GPSCoordinates" in metadata[0]
                and "CreateDate" in metadata[0]
                and metadata[0]["CreateDate"].startswith("2021:01:06")
            ):
                print(f"GPS + Jan 6: {filename}")
                count += 1

    print(f"Total videos with GPS coordinates, filmed Jan 6: {count:,}")


if __name__ == "__main__":
    main()
