import os


def main():
    # The path to the BlueLeaks dataset. Change this to match your path.
    blueleaks_path = "/mnt/f/BlueLeaks-extracted"

    # Loop through each of the filenames returns by os.listdir()
    for bl_folder in os.listdir(blueleaks_path):
        # The os.path.join() function is useful for combining parts of paths
        # For example, if bl_folder is "sfbay211", then bl_folder_path will be
        # "/Volumes/datasets/BlueLeaks-extracted/sfbay211".
        bl_folder_path = os.path.join(blueleaks_path, bl_folder)

        # For each BlueLeaks folder, count the files and folders inside
        files_count = 0
        folders_count = 0
        for filename in os.listdir(bl_folder_path):
            # Create the absolute path of the filename
            filename_path = os.path.join(bl_folder_path, filename)

            # Check if it's a file
            if os.path.isfile(filename_path):
                files_count += 1

            # Check if it's a folder
            if os.path.isdir(filename_path):
                folders_count += 1

        # Display the results
        print(f"{bl_folder} has {files_count} files, {folders_count} folders")


main()
