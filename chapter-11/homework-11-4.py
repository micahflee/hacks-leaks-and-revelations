import click
import os
import json
import math
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
    """Create KML files of GPS coordinates from Parler metadata"""
    kml_all = simplekml.Kml()
    kml_january6 = simplekml.Kml()
    kml_insurrection = simplekml.Kml()

    for filename in os.listdir(parler_metadata_path):
        abs_filename = os.path.join(parler_metadata_path, filename)
        if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
            with open(abs_filename, "rb") as f:
                json_data = f.read()

            try:
                metadata = json.loads(json_data)
            except json.decoder.JSONDecodeError:
                print(f"Invalid JSON: {filename}")
                continue

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

                print(f"Adding point {name} to kml_all: {lon}, {lat}")
                kml_all.newpoint(name=name, description=url, coords=[(lon, lat)])

                if "CreateDate" in metadata[0] and metadata[0]["CreateDate"].startswith(
                    "2021:01:06"
                ):
                    print(f"Adding point {name} to kml_january6: {lon}, {lat}")
                    kml_january6.newpoint(
                        name=name, description=url, coords=[(lon, lat)]
                    )

                    if was_video_filmed_in_dc(metadata):
                        print(f"Adding point {name} to kml_insurrection: {lon}, {lat}")
                        kml_insurrection.newpoint(
                            name=name, description=url, coords=[(lon, lat)]
                        )

    kml_all.save("parler-videos-all.kml")
    kml_january6.save("parler-videos-january6.kml")
    kml_insurrection.save("parler-videos-insurrection.kml")


if __name__ == "__main__":
    main()
