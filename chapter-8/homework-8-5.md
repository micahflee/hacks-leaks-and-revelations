# Homework 8-5: Map Out the CSVs in BlueLeaks

To avoid hardcoding the path to your BlueLeaks data inside the file, this solution gets the path from the user as a CLI argument using Click.

The Python script starts by importing the two modules that we need, `os` and `click`:

```python
import os
import click
```

It then defines the `main()` function as a Click command that takes the `blueleaks_path` argument.

```python
@click.command()
@click.argument("blueleaks_path")
def main(blueleaks_path):
    """Map Out the CSVs in BlueLeaks"""
```

It starts by creating an empty dictionary, `csv_to_folders`, and then loops though all of the BlueLeaks folders.

```python
    # A dictionary where the keys are CSV filenames and the values are BlueLeaks folders
    csv_to_folders = {}

    # Loops through all of the folders in BlueLeaks
    for folder in os.listdir(blueleaks_path):
        blueleaks_folder_path = os.path.join(blueleaks_path, folder)
```

This sets `blueleaks_folder_path` to be the path to the specific BlueLeaks folder for this loop iteration. The rest of this for loop fills up the `csv_to_folders` dictionary with data.

```python
        # Only proceed if this is actually a folder
        if os.path.isdir(blueleaks_folder_path):
            # Loop through the files in this folder
            for filename in os.listdir(blueleaks_folder_path):
                # Is this a CSV file?
                if filename.lower().endswith(".csv"):
                    # If this CSV file isn't in the dict, make it an empty list
                    if filename not in csv_to_folders:
                        csv_to_folders[filename] = []

                    # Add this folder to the list
                    csv_to_folders[filename].append(folder)
```

It makes sure that `blueleaks_folder_path` is actually a folder, which it should be, and then loops through the files in that folder. If the file is a CSV file (if `filename.lower().endswith(".csv")`), then it sees if this file is a key in the dictionary yet. If it's not, it adds it, with the value being a blank list. Finally, it appends the folder name to the list of folders that have this file.

Once the Python script has collected all of the data and stored it in this dictionary, the last step is to display the output.

```python
    # Display the output
    for filename in csv_to_folders:
        print(f"{len(csv_to_folders[filename])} folders | {filename}")
```

This solution just displays, for each CSV filename, how many folders that file exists in. But if you wanted you could also display the actual folders themselves, `csv_to_folders[filename]`.
