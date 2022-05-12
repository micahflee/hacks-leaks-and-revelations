# Homework 8-3: Update the Script to Filter Videos from January 6, 2021

**NOTE:** If you're using Windows, I recommend that you follow the instructions in this chapter using your Ubuntu terminal instead of PowerShell, and that you save this data in your Ubuntu home folder, like in `~/datasets`, instead of using your Windows-formatted USB disk, like in `/mnt/d`. I found that working with this data in Linux was significantly faster than in directly in Windows.

In this homework assignment you'll modify the script from Homework 8-2 to not only filter Parler videos down to just the ones that include GPS coordinates in their metadata, but also to those filmed on January 6, 2021. Start by copying your solution from Homework 8-2 into a new file for Homework-8-3.

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

## Updating the Script

The first thing I'm changing is the comments at the top of the `main()` function.

```python
def main(parler_metadata_path):
    """Filter Parler videos that have GPS coordinates and were filmed Jan 6, 2021"""
    # Number of videos with GPS coordinates, filmed January 6, 2021
    count = 0
```

The next step is to modify the code to filter it by date. I can do that by changing this code:

```python
if "GPSCoordinates" in metadata[0]:
    print(f"Found GPS coordinates: {filename}")
```

To this:

```python
if "GPSCoordinates" in metadata[0] and metadata[0]["CreateDate"].startswith("2021:01:06 "):
    print(f"GPS + Jan 6: {filename}")
```

Finally, I'll change the text that gets displayed at the end from:

```python
print(f"Total videos with GPS coordinates: {count}")
```

To:

```python
print(f"Total videos with GPS coordinates, filmed Jan 6: {count}")
```

## The Final Script

Here's what it looks like to run this script:

```
micah@cloak:~/datasets/homework/chapter-8$ python3 homework-8-3.py ~/datasets/Parler/metadata
GPS + Jan 6: meta-8YA6CeYMxHh4.json
GPS + Jan 6: meta-91Vga2rHrrID.json
GPS + Jan 6: meta-a3NbAuIyNM3v.json
--snip--
GPS + Jan 6: meta-diIeD4Ne7Ear.json
GPS + Jan 6: meta-q7BpcYyFpX7J.json
GPS + Jan 6: meta-OUJYa3npW0oE.json
Total videos with GPS coordinates, filmed Jan 6: 1958
```

You can find an implementation of this script in [homework-8-3.py](./homework-8-3.py).
