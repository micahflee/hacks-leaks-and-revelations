import os
import click


@click.command()
@click.argument("blueleaks_path")
def main(blueleaks_path):
    """Map Out the CSVs in BlueLeaks"""

    # A dictionary where the keys are CSV filenames and the values are BlueLeaks folders
    csv_to_folders = {}

    # Loops through all of the folders in BlueLeaks
    for folder in os.listdir(blueleaks_path):
        blueleaks_folder_path = os.path.join(blueleaks_path, folder)

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

    # Display the output
    for filename in csv_to_folders:
        print(f"{len(csv_to_folders[filename])} folders | {filename}")


if __name__ == "__main__":
    main()
