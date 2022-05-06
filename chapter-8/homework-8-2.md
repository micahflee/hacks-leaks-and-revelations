# Homework 8-2: Write a Script to Filter Videos with GPS Coordinates

In this homework assignment you will write a Python script that filters Parler videos down to just the ones that include GPS coordinates in their metadata. Here is the template Python script provided in the book:

```python
import click

@click.command()
@click.argument("parler_metadata_path")
def main(parler_metadata_path):
    """Filter Parler videos that have GPS coordinates"""

if __name__ == "__main__":
    main()
```

## Define the Count Variable

Let's start by defining the `count` variable to keep track of the number of videos with GPS coordinates in their metadata:

```python
# Number of videos with GPS coordinates in their metadata
count = 0
```

# Loop Through the JSON Files

Now we need to loop through all of the files in the `parler_metadata_path` folder. To do this, we can use the `os.listdir()` function, which requires importing the `os` module. So we must add this to the top of the file:

```python
import os
```

Now, in the `main()` function, here's code that loops through all of the metadata files and display the absolute filenames. You can try running this code just to make sure it works so far.

```python
for filename in os.listdir(parler_metadata_path):
    abs_filename = os.path.join(parler_metadata_path, filename)
        print(abs_filename)
```

An example of running this code so far:

```
PS D:\homework\chapter-8> python .\homework-8-2.py D:\Parler\metadata\
D:\Parler\metadata\.aws
D:\Parler\metadata\meta-0002bz1GNsUP.json
D:\Parler\metadata\meta-0003lx5cSwSB.json
D:\Parler\metadata\meta-0004D2lOBGpr.json
--snip--
```

This should list over one million filenames. Great, it works so far. But notice that the first filename is `.aws`, which is an empty folder that's in the `metadata` folder. Change the code to only look for files (not folders) that end in the `.json`, like this:

```python
for filename in os.listdir(parler_metadata_path):
    abs_filename = os.path.join(parler_metadata_path, filename)
    if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
        print(abs_filename)
```

Running this code so far only shows the JSON files:

```
PS D:\homework\chapter-8> python .\homework-8-2.py D:\Parler\metadata\
D:\Parler\metadata\meta-0002bz1GNsUP.json
D:\Parler\metadata\meta-0003lx5cSwSB.json
D:\Parler\metadata\meta-0004D2lOBGpr.json
--snip--
```

## Parse The JSON Files

Now we need to load the content of these JSON files as a string, and then run this content through the `json.loads()` function to convert it into Python object. This requires importing the `json` module. So we must add this to the top of the file:

```python
import json
```

Now change the for loop code to read the content from each JSON file, parse the JSON into a variable called `metadata`, and then display that variable, like this:

```python
for filename in os.listdir(parler_metadata_path):
    abs_filename = os.path.join(parler_metadata_path, filename)
    if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
        with open(abs_filename, "rb") as f:
            json_data = f.read()

        metadata = json.loads(json_data)
        print(metadata)
```

Notice that the `open()` function includes the argument `"rb"`. This means we will be reading the file in binary mode instead of text mode. This normally isn't required for reading JSON files, but I discovered that it in this case, because some of the JSON files (like `meta-01tjNglj83ad.json`) include Chinese characters.

Running this code so far only displays all of the metadata inside all of the JSON objects, which means it's working:

```
PS D:\homework\chapter-8> python .\homework-8-2.py D:\Parler\metadata\
[{'SourceFile': '-', 'ExifToolVersion': 12.0, 'FileType': 'MP4', 'FileTypeExtension': 'mp4', 'MIMEType': 'video/mp4', 'MajorBrand': 'MP4 v2 [ISO 14496-14]', 'MinorVersion': '0.0.0', 'CompatibleBrands': ['isom', 'mp42'], 'MovieHeaderVersion': 0, 'CreateDate': '2020:09:10 03:51:19', 'ModifyDate': '2020:09:10 03:51:19', 'TimeScale': 15360, 'Duration': '0:05:18', 'PreferredRate': 1, 'PreferredVolume': '100.00%', 'PreviewTime': '0 s', 'PreviewDuration': '0 s', 'PosterTime': '0 s', 'SelectionTime': '0 s', 'SelectionDuration': '0 s', 'CurrentTime': '0 s', 'NextTrackID': 3, 'TrackHeaderVersion': 0, 'TrackCreateDate': '2020:09:10 03:51:19', 'TrackModifyDate': '2020:09:10 03:51:19', 'TrackID': 1, 'TrackDuration': '0:05:18', 'TrackLayer': 0, 'TrackVolume': '0.00%', 'ImageWidth': 1280, 'ImageHeight': 720, 'CompressorID': 'avc1', 'SourceImageWidth': 1280, 'SourceImageHeight': 720, 'XResolution': 72, 'YResolution': 72, 'BitDepth': 24, 'VideoFrameRate': 30, 'GraphicsMode': 'srcCopy', 'OpColor': '0 0 0', 'MatrixStructure': '1 0 0 0 1 0 0 0 1', 'MediaHeaderVersion': 0, 'MediaCreateDate': '2020:09:10 03:51:19', 'MediaModifyDate': '2020:09:10 03:51:19', 'MediaTimeScale': 44100, 'MediaDuration': '0:05:18', 'MediaLanguageCode': 'und', 'HandlerDescription': 'ISO Media file produced by Google Inc. Created on: 09/09/2020.', 'AudioFormat': 'mp4a', 'AudioChannels': 2, 'AudioBitsPerSample': 16, 'AudioSampleRate': 44100, 'Balance': 0, 'HandlerType': 'Metadata', 'HandlerVendorID': 'Apple', 'GoogleStartTime': 0, 'GoogleTrackDuration': '0:05:18', 'MediaDataSize': 77496454, 'MediaDataOffset': 136276, 'ImageSize': '1280x720', 'Megapixels': 0.922, 'AvgBitrate': '1.95 Mbps', 'Rotation': 0}]
--snip--
```

## Filtering Videos With GPS Coordinates

Now that we're successfully parsing the JSON, the next step is to check to see if includes the `"GPSCoordinates"` key, like this:

```python
metadata = json.loads(json_data)
if "GPSCoordinates" in metadata[0]:
    print(f"Found GPS coordinates: {abs_filename}")
    count += 1
```

Notice that the if statement checks to see if `"GPSCoordinates"` is in `metadata[0]` instead of `metadata`. This is because each JSON object is technically a list with one element, and the `[0]` part selects that element, which ultimately searches the dictionary for that key.

Finally, when the for loop is finished, you can add a final `print()` that displays the total count.

```python
print(f"Total videos with GPS coordinates: {count}")
```

## The Final Script

Here's what it looks like to run this script:

```
micah@cloak:/mnt/d/homework/chapter-8$ python3 ./homework-8-2.py ~/datasets/Parler/metadata
Found GPS coordinates: /home/micah/datasets/Parler/metadata/meta-27PknKIOwHt6.json
Found GPS coordinates: /home/micah/datasets/Parler/metadata/meta-m3Wq53jjPnpw.json
--snip--
Found GPS coordinates: /home/micah/datasets/Parler/metadata/meta-50A0Fl2Fcg89.json
Found GPS coordinates: /home/micah/datasets/Parler/metadata/meta-H89ZQPBBfhZA.json
Total videos with GPS coordinates: 63983
```

You can find an implementation of this script in [homework-8-2.py](./homework-8-2.py).
