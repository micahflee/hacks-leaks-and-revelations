import click
import os
import json
import simplekml


def json_filename_to_parler_id(json_filename):
    return json_filename.split("-")[1].split(".")[0]


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
    """Create a KML file of GPS coordinates from Parler metadata"""
    kml = simplekml.Kml()

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
                name = json_filename_to_parler_id(filename)
                url = f"https://s3.wasabisys.com/ddosecrets-parler/{name}"
                lon = gps_degrees_to_decimal(metadata[0]["GPSLongitude"])
                lat = gps_degrees_to_decimal(metadata[0]["GPSLatitude"])

                print(f"Adding point {name}: {lon},{lat}")
                kml.newpoint(name=name, description=url, coords=[(lon, lat)])

    kml.save("parler-videos.kml")


if __name__ == "__main__":
    main()
