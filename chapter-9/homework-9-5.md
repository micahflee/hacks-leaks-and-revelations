# Homework 8-5: Plot the Parler Videos on a Map

**NOTE:** If you're using Windows, I recommend that you follow the instructions in this chapter using your Ubuntu terminal instead of PowerShell, and that you save this data in your Ubuntu home folder, like in `~/datasets`, instead of using your Windows-formatted USB disk, like in `/mnt/d`. I found that working with this data in Linux was significantly faster than in directly in Windows.

## Install QGIS

Download and install the free and open source geographic information system (GIS) software QGIS from [qgis.org](https://www.qgis.org/).

Open QGIS Desktop and Save the new blank project as `parler-videos.qgz`.

## Create a GeoJSON file

Since Homework 8-2 already has code that filters all of the Parler videos with GPS coordinates, start by copying your solution from that assignment into a new file for homework-9-5.

Here's the code I'm starting with:

```python
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
                print(f"Found GPS coordinates: {filename}")
                count += 1

    print(f"Total videos with GPS coordinates: {count}")

if __name__ == "__main__":
    main()
```

The first thing I changed is the docstring on the `main()` function to describe what this new script does instead.

```python
@click.command()
@click.argument("parler_metadata_path")
def main(parler_metadata_path):
    """Create a GeoJSON file containing Parler GPS coordinates"""
```

At the top of the `main()` function, I also defined a new variable called `features` and set its value to an empty list.

```python
# The list of GeoJSON features to export
features = []
```

Then, in the for loop, after finding metadata that includes GPS coordinates, I added some code add a GoeJSON-formatted dictionary to the features list:

```python
metadata = json.loads(json_data)
if "GPSCoordinates" in metadata[0]:
    print(f"Found GPS coordinates: {filename}")
    longitude_decimal = 0  # TODO: Figure out the longitude
    latitude_decimal = 0  # TODO: Figure out the latitude
    features.append(
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [longitude_decimal, latitude_decimal],
            },
            "properties": {"name": filename},
        }
    )
```

For now I just set the two variables `longitude_decimal` and `latitude_decimal` to 0, but I will fix that soon.

After the for loop, I then saved the output of this script as `parler-videos.geojson`:

```python
# Save the GeoJSON file
with open("parler-videos.geojson", "w") as f:
    f.write(json.dumps(features))

print("Wrote file: parler-videos.geojson")
```

Here's the script so far:

```python
import click
import os
import json

@click.command()
@click.argument("parler_metadata_path")
def main(parler_metadata_path):
    """Create a GeoJSON file containing Parler GPS coordinates"""
    # The list of GeoJSON features to export
    features = []

    for filename in os.listdir(parler_metadata_path):
        abs_filename = os.path.join(parler_metadata_path, filename)
        if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
            with open(abs_filename, "rb") as f:
                json_data = f.read()

            metadata = json.loads(json_data)
            if "GPSCoordinates" in metadata[0]:
                print(f"Found GPS coordinates: {filename}")
                longitude_decimal = 0  # TODO: Figure out the longitude
                latitude_decimal = 0  # TODO: Figure out the latitude
                features.append(
                    {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [longitude_decimal, latitude_decimal],
                        },
                        "properties": {"name": filename},
                    }
                )

    # Save the GeoJSON file
    with open("parler-videos.geojson", "w") as f:
        f.write(json.dumps(features))

    print("Wrote file: parler-videos.geojson")

if __name__ == "__main__":
    main()
```
Now I need to calculate `longitude_decimal` and `latitude_decimal`. I'll do that by adding the functions defined Homework 8-4 to the top of the Python script:

```python
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
```

And I replace setting the decimal GPS coordinates to 0 with their actual decimal values:

```python
longitude_decimal = gps_degrees_to_decimal(metadata[0]["GPSLongitude"])
latitude_decimal = gps_degrees_to_decimal(metadata[0]["GPSLatitude"])
```

And finally, just to make the output while running this script a little nicer, I replaced this `print()` line:

```python
print(f"Total videos with GPS coordinates: {count}")
```

With this one:

```python
print(f"\rFound {count:,} videos with GPS coordinates", end="")
```

This includes a few tricks:

- The first character that gets displayed in `\r`, which a special character known as a carriage return. Basically, it makes sure the cursor goes back to the beginning of the line before starting to print output, overwriting whatever was there before.
- The `print()` function includes the argument `end=""`. Normally every time you call `print()` and pass in a string, it adds a newline character (`\n`) to the end of your string. This tells it to just not add a newline character.
- Both of these combined mean that when you run the script, it will just continually overwrite the same line with an updated count rather than printing nearly 64,000 lines.
- Also, when using the f-string to display the `count` variable I used `{count:,}` instead of just `{count}`. This makes it include a comma every three digits, making the number much easier to read.

Since we're constantly printing the count, I replaced the `print()` line:

```python
print(f"Total videos with GPS coordinates: {count}")
```

With just:

```python
print()
```

This will basically _just_ print a newline character.

## The Final Script

Here's what it looks like to run this script:

```
micah@cloak:~/datasets/homework/chapter-9$ python3 homework-9-5.py ~/datasets/Parler/metadata
Found 63,983 videos with GPS coordinates
Wrote file: parler-videos.geojson
```

You should also now have an 8.7mb file called `parler-videos.geojson` in your working folder. This is your GeoJSON file that you just created, containing all of the GPS coordinates from the Parler metadata.

You can find an implementation of this script in [homework-9-5.py](./homework-9-5.py).
