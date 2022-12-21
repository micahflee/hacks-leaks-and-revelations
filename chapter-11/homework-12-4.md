# Homework 12-4: Update the Script to Filter Videos Filmed in Washington, DC

**NOTE:** If you're using Windows, I recommend that you follow the instructions in this chapter using your Ubuntu terminal instead of PowerShell, and that you save this data in your Ubuntu home folder, like in `~/datasets`, instead of using your Windows-formatted USB disk, like in `/mnt/d`. I found that working with this data in Linux was significantly faster than in directly in Windows.

In this homework assignment, you'll make a modified version of the scripts from [Homework 12-2](./homework-12-2.md) and [12-3](./homework-12-3.md), but this time filter it down to just videos with GPS coordinates that are (roughly) inside the city of Washington DC.

I'm starting with my solution for Homework [12-3](./homework-12-3.md), and then modifying. Here's the starting code:

```python
import click
import os
import json

@click.command()
@click.argument("parler_metadata_path")
def main(parler_metadata_path):
    """Filter Parler videos that have GPS coordinates and were filmed Jan 6, 2021"""
    # Number of videos with GPS coordinates, filmed January 6, 2021
    count = 0

    for filename in os.listdir(parler_metadata_path):
        abs_filename = os.path.join(parler_metadata_path, filename)
        if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
            with open(abs_filename, "rb") as f:
                json_data = f.read()

            metadata = json.loads(json_data)
            if "GPSCoordinates" in metadata[0] and metadata[0]["CreateDate"].startswith(
                "2021:01:06 "
            ):
                print(f"GPS + Jan 6: {filename}")
                count += 1

    print(f"Total videos with GPS coordinates, filmed Jan 6: {count}")

if __name__ == "__main__":
    main()
```

The first thing I changed is the docstring on the `main()` function to describe what this new script does instead:

```python
@click.command()
@click.argument("parler_metadata_path")
def main(parler_metadata_path):
    """Filter Parler videos that were filmed in Washington DC and on Jan 6, 2021"""
```

## Add Functions From the Chapter

Next, I'm adding the important functions defined in the chapter above the `main()` function.

Here's the `distance()` function, which implements the distance formula.

```python
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y2) ** 2)
```

This function uses the `math.sqrt()` function, so I also imported the `math` module by adding this to the top of the Python script, next to the other imports:

```python
import math
```

Here's the `is_point_in_washington_dc()` function, which uses the `distance()` function to roughly determine if the (_x_, _y_) coordinates passed in are a point within 20 kilometers of the center of Washington DC.

```python
def is_point_in_washington_dc(x, y):
    washington_dc_x = -77.00667073028771
    washington_dc_y = 38.894101636006035
    return distance(washington_dc_x, washington_dc_y, x, y) <= 0.25
```

And here's the `gps_degrees_to_decimal()` function, which converts GPS coordinates from the degrees, minutes, seconds format, exactly as they're represented in the Parler video metadata, into the decimal format, which will make it simpler to compare.

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
```

## Filter the Videos

Here's some of the code that I'm starting with:

```python
if "GPSCoordinates" in metadata[0] and metadata[0]["CreateDate"].startswith(
    "2021:01:06 "
):
    print(f"GPS + Jan 6: {filename}")
    count += 1
```

For every metadata file, it opens it and parses the JSON into the a variable called `metadata`. Then it checks to make sure that:

1. `GPSCoordinates` is in the metadata
2. `CreateDate` starts with `2021:01:06`

In order to filter videos down to videos of the insurrection, we need to add one more check:

3. The video's GPS coordinates are located in Washington DC

So I modified this if statement to include that check:

```python
if (
    "GPSCoordinates" in metadata[0]
    and metadata[0]["CreateDate"].startswith("2021:01:06 ")
    and was_video_filmed_in_washington_dc(metadata)
):
    print(f"Found an insurrection video: {filename}")
    count += 1
```

In my case, I made it ensure that the return value of `was_video_filmed_in_washington_dc(metadata)` is `True`, and if it is I add it to the count of insurrection videos. Now all that's left is to actually define the `was_video_filmed_in_washington_dc()` function.

Here's how I defined it:

```python
def was_video_filmed_in_washington_dc(metadata):
    x = gps_degrees_to_decimal(metadata[0]["GPSLongitude"])
    y = gps_degrees_to_decimal(metadata[0]["GPSLatitude"])
    return is_point_in_washington_dc(x, y)
```

It takes Parler metadata a san argument. It sets the variable `x` equal to the longitude value, converted to degrees, and it sets the variable `y` equal to the latitude value, converted to degrees. Then it just return the return value of `is_point_in_washington_dc(x, y)`.


## The Final Script

Here's what it looks like to run this script:

```
micah@cloak:~/datasets/homework/chapter-10$ python3 homework-12-4.py ~/datasets/Parler/metadata
Found an insurrection video: meta-8YA6CeYMxHh4.json
Found an insurrection video: meta-91Vga2rHrrID.json
Found an insurrection video: meta-mtR54fIOsU8Y.json
--snip--
Found an insurrection video: meta-diIeD4Ne7Ear.json
Found an insurrection video: meta-q7BpcYyFpX7J.json
Found an insurrection video: meta-OUJYa3npW0oE.json
Total videos filmed in Washington DC on January 6: 1199
```

You can find an implementation of this script in [homework-9-10.py](./homework-12-4.py).
