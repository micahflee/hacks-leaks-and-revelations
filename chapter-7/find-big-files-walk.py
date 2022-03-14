import os


def main():
    # 100mb, in bytes
    one_hundred_mb = 1024 * 1024 * 100

    # Walk the NCRIC folder tree
    ncric_path = "/Volumes/datasets/BlueLeaks-extracted/ncric"
    for dirname, dirnames, filenames in os.walk(ncric_path):
        # Each time this for loop runs, dirname is the path to a folder, dirnames
        # is a list of subfolders inside it, and filenames is a list of files
        # inside it. This will loop for each folder or subfolder it finds.

        # Look at each file in this folder
        for filename in filenames:
            # Figure out the absolute path of this file
            absolute_filename = os.path.join(dirname, filename)

            # If it's a file, check to see if it's big enough
            if os.path.isfile(absolute_filename):
                file_size = os.path.getsize(absolute_filename)
                if file_size >= one_hundred_mb:
                    # Convert file_size from bytes to megabytes
                    size_in_mb = int(file_size / 1024 / 1024)
                    print(f"{absolute_filename} is {size_in_mb}mb")


main()
