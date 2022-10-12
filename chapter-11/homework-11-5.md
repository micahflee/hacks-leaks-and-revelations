# Homework 10-5: Plot the Parler Videos on a Map

**NOTE:** If you're using Windows, I recommend that you follow the instructions in this chapter using your Ubuntu terminal instead of PowerShell, and that you save this data in your Ubuntu home folder, like in `~/datasets`, instead of using your Windows-formatted USB disk, like in `/mnt/d`. I found that working with this data in Linux was significantly faster than in directly in Windows.

In this homework assignment, you will use geographic information system (GIS) software called [QGIS](https://www.qgis.org/) to map the locations of where Parler videos were filmed, for the videos that include GPS coordinates in their metadata.

## Create a CSV of GPS Coordinates

Here's the code I started with:

```python
import click

@click.command()
@click.argument("parler_metadata_path")
@click.argument("output_csv_path")
def main(parler_metadata_path, output_csv_path):
    """Create a CSV of GPS coordinates from Parler metadata"""

if __name__ == "__main__":
    main()
```

Then I added the `gps_degrees_to_decimal()` and `convert_filename()` functions above the `main()` function:

```python
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


def convert_filename(json_filename):
    return json_filename.split("-")[1].split(".")[0]
```

I needed to write the output CSV file, so I imported the `csv` module at the top of the file:

```python
import csv
```

And in the `main()` function started opening the CSV file for writing, with the appropriate headers:

```python
# Open the output CSV file for writing
with open(output_csv_path, "w") as output_f:
    writer = csv.DictWriter(output_f, fieldnames=["Filename", "Longitude", "Latitude"])
    writer.writeheader()
```

Now that I'm able to write rows to the CSV, I needed to start searching for GPS coordinates in the Parler metadata JSON files. So I imported the `json` and `os` modules at the top of the file:

```python
import json
import os
```

And, still inside the CSV writer code block, I added code to loop through all of the Parler metadata files, looking for GPS coordinates:

```python
for filename in os.listdir(parler_metadata_path):
    abs_filename = os.path.join(parler_metadata_path, filename)
    if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
        with open(abs_filename, "rb") as f:
            json_data = f.read()

        metadata = json.loads(json_data)
        if "GPSLongitude" in metadata[0] and "GPSLatitude" in metadata[0]:
            pass
```

Now that I've found a JSON file with GPS coordinates, I created a dictionary called `row` that contains data for the row in the CSV, and wrote that row to the output file--and also print it to the terminal, just so I can see what's going on while I'm running the script.

```python
# Save the row
row = {
    "Filename": convert_filename(filename),
    "Longitude": gps_degrees_to_decimal(metadata[0]["GPSLongitude"]),
    "Latitude": gps_degrees_to_decimal(metadata[0]["GPSLatitude"]),
}
writer.writerow(row)
print(row)
```

And finally, at the bottom of the `main()` function, I added a `print()` line to say that the CSV is saved:

```python
print(f"Saved: {output_csv_path}")
```

## An Exercise in Debugging

I'm done, right? Let me try running it:

```
micah@cloak:~/code/hacks-leaks-and-revelations/chapter-10$ python3 homework-10-5.py ~/datasets/Parler/metadata parler-gps-coordinates.csv
{'Filename': '27PknKIOwHt6', 'Longitude': -118.4026, 'Latitude': 34.0724}
{'Filename': 'm3Wq53jjPnpw', 'Longitude': -118.2599, 'Latitude': 34.0473}
{'Filename': 'kpKT3stt5LXq', 'Longitude': -80.2949, 'Latitude': 26.334}
--snip--
{'Filename': 'ZuLaQPyY7Goa', 'Longitude': -81.9819, 'Latitude': 35.5031}
{'Filename': 'KJ8t1qELW1nH', 'Longitude': -117.5453, 'Latitude': 33.814}
{'Filename': 'bSPOjbdsm2xF', 'Longitude': -71.32379999999999, 'Latitude': 43.7277}
Traceback (most recent call last):
  File "/home/micah/code/hacks-leaks-and-revelations/chapter-10/homework-10-5.py", line 66, in <module>
    main()
  File "/usr/lib/python3/dist-packages/click/core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "/usr/lib/python3/dist-packages/click/core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "/usr/lib/python3/dist-packages/click/core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/lib/python3/dist-packages/click/core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "/home/micah/code/hacks-leaks-and-revelations/chapter-10/homework-10-5.py", line 54, in main
    "Longitude": gps_degrees_to_decimal(
  File "/home/micah/code/hacks-leaks-and-revelations/chapter-10/homework-10-5.py", line 10, in gps_degrees_to_decimal
    degrees = float(parts[0])
IndexError: list index out of range
```

Hmm, it's crashing in the `gps_degrees_to_decimal()` function on the line `degrees = float(parts[0])`. If you look back at the code of that function, that must mean that the `parts` has zero items on it. Why is that? To debug, I added `print(f"gps_coordinate: {gps_coordinate}")` statement to that function, so I can tell what the `gps_coordinates` getting passed in are:

```python
def gps_degrees_to_decimal(gps_coordinate):
    print(f"gps_coordinate: {gps_coordinate}")
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

And then I ran it again:

```
micah@cloak:~/code/hacks-leaks-and-revelations/chapter-10$ python3 homework-10-5.py ~/datasets/Parler/metadata parler-gps-coordinates.csv
gps_coordinate: 118 deg 24' 9.36" W
gps_coordinate: 34 deg 4' 20.64" N
{'Filename': '27PknKIOwHt6', 'Longitude': -118.4026, 'Latitude': 34.0724}
--snip--
gps_coordinate: 71 deg 19' 25.68" W
gps_coordinate: 43 deg 43' 39.72" N
{'Filename': 'bSPOjbdsm2xF', 'Longitude': -71.32379999999999, 'Latitude': 43.7277}
gps_coordinate:
Traceback (most recent call last):
  File "/home/micah/code/hacks-leaks-and-revelations/chapter-10/homework-10-5.py", line 66, in <module>
    main()
  File "/usr/lib/python3/dist-packages/click/core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "/usr/lib/python3/dist-packages/click/core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "/usr/lib/python3/dist-packages/click/core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/lib/python3/dist-packages/click/core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "/home/micah/code/hacks-leaks-and-revelations/chapter-10/homework-10-5.py", line 54, in main
    "Longitude": gps_degrees_to_decimal(
  File "/home/micah/code/hacks-leaks-and-revelations/chapter-10/homework-10-5.py", line 10, in gps_degrees_to_decimal
    degrees = float(parts[0])
IndexError: list index out of range
```

Each time this function is called it prints out the value of `gps_coordinates` and right before the crash that value was blank. That must mean that `gps_coordinates` is a blank string (`""`), which would make sense that when it gets split into zero parts.

My guess is that I hit a false positive: I found a Parler metadata JSON file that had `GPSLongitude` and `GPSLatitude` fields, they were just empty, so it didn't actually include GPS coordinates.

This if statement isn't good enough:

```python
if "GPSLongitude" in metadata[0] and "GPSLatitude" in metadata[0]:
```

In addition to making sure the `GPSLongitude` and `GPSLatitude` fields exist in the dictionary, I _also_ need to make sure they're not blank. So I changed my if statement to this:

```python
if (
    "GPSLongitude" in metadata[0]
    and "GPSLatitude" in metadata[0]
    and metadata[0]["GPSLongitude"] != ""
    and metadata[0]["GPSLatitude"] != ""
):
```

Then I commented out the `print(f"gps_coordinate: {gps_coordinate}")` line, which I only added for debugging, and ran it again:

```
micah@cloak:~/code/hacks-leaks-and-revelations/chapter-10$ python3 homework-10-5.py ~/datasets/Parler/metadata parler-gps-coordinates.csv
{'Filename': '27PknKIOwHt6', 'Longitude': -118.4026, 'Latitude': 34.0724}
{'Filename': 'm3Wq53jjPnpw', 'Longitude': -118.2599, 'Latitude': 34.0473}
{'Filename': 'kpKT3stt5LXq', 'Longitude': -80.2949, 'Latitude': 26.334}
--snip--
{'Filename': 'pMdvwJuktYPj', 'Longitude': -77.0058, 'Latitude': 38.8907}
{'Filename': '50A0Fl2Fcg89', 'Longitude': -122.6799, 'Latitude': 49.174099999999996}
{'Filename': 'H89ZQPBBfhZA', 'Longitude': -87.40530000000001, 'Latitude': 39.4479}
Saved: parler-gps-coordinates.csv
```

You can find an implementation of this script in [homework-10-5.py](./homework-10-5.py).

## Visualize the GPS Data Using QGIS

Download and install the free and open source geographic information system (GIS) software QGIS from [qgis.org](https://www.qgis.org/).

Open QGIS Desktop and save the new blank project as something like `parler-videos.qgz`.

