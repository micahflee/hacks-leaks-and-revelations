# Homework 8-2: Write a Script to Filter Videos with GPS Coordinates

**NOTE:** If you're using Windows, I recommend that you follow the instructions in this chapter using your Ubuntu terminal instead of PowerShell, and that you save this data in your Ubuntu home folder, like in `~/datasets`, instead of using your Windows-formatted USB disk, like in `/mnt/d`. I found that working with this data in Linux was significantly faster than in directly in Windows.

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
micah@cloak:~/datasets/homework/chapter-8$ python3 homework-8-2a.py ~/datasets/Parler/metadata
/home/micah/datasets/Parler/metadata/meta-ISVeh218verI.json
/home/micah/datasets/Parler/metadata/meta-BeLykBcFbpEW.json
/home/micah/datasets/Parler/metadata/meta-qQqSthmGdpSn.json
/home/micah/datasets/Parler/metadata/meta-Aswvxy3XDKg8.json
--snip--
```

This should list over one million filenames. Great, it works so far.

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
micah@cloak:~/datasets/homework/chapter-8$ python3 homework-8-2a.py ~/datasets/Parler/metadata
[{'SourceFile': '-', 'ExifToolVersion': 12.0, 'FileType': 'MP4', 'FileTypeExtension': 'mp4', 'MIMEType': 'video/mp4', 'MajorBrand': 'MP4  Base Media v1 [IS0 14496-12:2003]', 'MinorVersion': '0.2.0', 'CompatibleBrands': ['isom', 'iso2', 'avc1', 'mp41'], 'MediaDataSize': 4088795, 'MediaDataOffset': 48, 'MovieHeaderVersion': 0, 'CreateDate': '0000:00:00 00:00:00', 'ModifyDate': '0000:00:00 00:00:00', 'TimeScale': 1000, 'Duration': '0:00:30', 'PreferredRate': 1, 'PreferredVolume': '100.00%', 'PreviewTime': '0 s', 'PreviewDuration': '0 s', 'PosterTime': '0 s', 'SelectionTime': '0 s', 'SelectionDuration': '0 s', 'CurrentTime': '0 s', 'NextTrackID': 3, 'TrackHeaderVersion': 0, 'TrackCreateDate': '0000:00:00 00:00:00', 'TrackModifyDate': '0000:00:00 00:00:00', 'TrackID': 1, 'TrackDuration': '28.03 s', 'TrackLayer': 0, 'TrackVolume': '0.00%', 'ImageWidth': 1280, 'ImageHeight': 720, 'GraphicsMode': 'srcCopy', 'OpColor': '0 0 0', 'CompressorID': 'avc1', 'SourceImageWidth': 1280, 'SourceImageHeight': 720, 'XResolution': 72, 'YResolution': 72, 'BitDepth': 24, 'VideoFrameRate': 23.976, 'MatrixStructure': '1 0 0 0 1 0 0 0 1', 'MediaHeaderVersion': 0, 'MediaCreateDate': '0000:00:00 00:00:00', 'MediaModifyDate': '0000:00:00 00:00:00', 'MediaTimeScale': 48000, 'MediaDuration': '0:00:30', 'MediaLanguageCode': 'eng', 'HandlerDescription': 'SoundHandler', 'Balance': 0, 'AudioFormat': 'mp4a', 'AudioChannels': 2, 'AudioBitsPerSample': 16, 'AudioSampleRate': 48000, 'HandlerType': 'Metadata', 'HandlerVendorID': 'Apple', 'Title': 579413866321053, 'Encoder': 'Lavf57.83.100', 'ImageSize': '1280x720', 'Megapixels': 0.922, 'AvgBitrate': '1.09 Mbps', 'Rotation': 0}]
--snip--
```

If you let this finish running though, you will eventually hit a problem, and your script will crash with an error something like this:

```
Traceback (most recent call last):
  File "homework-8-2.py", line 22, in <module>
    main()
  File "/home/micah/.local/lib/python3.8/site-packages/click/core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "/home/micah/.local/lib/python3.8/site-packages/click/core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "/home/micah/.local/lib/python3.8/site-packages/click/core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/micah/.local/lib/python3.8/site-packages/click/core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "homework-8-2a.py", line 15, in main
    with open(abs_filename, "rb") as f:
IsADirectoryError: [Errno 21] Is a directory: '/home/micah/datasets/Parler/metadata/.aws'
```

This is an `IsADirectoryError` error, and the line of code that triggered the error is `with open(abs_filename, "rb") as f:`. This line is trying to open the file at path `abs_filename`, but it crashed because (in my case) `/home/micah/datasets/Parler/metadata/.aws` is a directory, not a file.

This is because the metadata folder has an empty directory called `.aws` in it. It's easy to fix this though. Let's just modify the code to only try to open `.json` files, by changing this:

```python
for filename in os.listdir(parler_metadata_path):
    abs_filename = os.path.join(parler_metadata_path, filename)
    with open(abs_filename, "rb") as f:
        json_data = f.read()

    metadata = json.loads(json_data)
    print(metadata)
```

To this:

```python
for filename in os.listdir(parler_metadata_path):
    abs_filename = os.path.join(parler_metadata_path, filename)
    if os.path.isfile(abs_filename) and abs_filename.endswith(".json"):
        with open(abs_filename, "rb") as f:
            json_data = f.read()

        metadata = json.loads(json_data)
        print(metadata)
```

Now, it checks to make sure `abs_filename` is a file and not a folder, and that that filename ends with `.json`, before trying to open it.

## Filtering Videos With GPS Coordinates

Now that we're successfully parsing the JSON, the next step is to check to see if includes the `"GPSCoordinates"` key, like this:

```python
metadata = json.loads(json_data)
if "GPSCoordinates" in metadata[0]:
    print(f"Found GPS coordinates: {filename}")
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
micah@cloak:~/datasets/homework/chapter-8$ python3 homework-8-2.py ~/datasets/Parler/metadata
Found GPS coordinates: meta-27PknKIOwHt6.json
Found GPS coordinates: meta-m3Wq53jjPnpw.json
Found GPS coordinates: meta-kpKT3stt5LXq.json
--snip--
Found GPS coordinates: meta-pMdvwJuktYPj.json
Found GPS coordinates: meta-50A0Fl2Fcg89.json
Found GPS coordinates: meta-H89ZQPBBfhZA.json
Total videos with GPS coordinates: 63983
```

You can find an implementation of this script in [homework-8-2.py](./homework-8-2.py).
