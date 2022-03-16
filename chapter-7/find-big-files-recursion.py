import os


# Recursive function that prints the filename of every file larger than 10mb
def files_bigger_than_100mb(path):
    # 100mb, in bytes
    one_hundred_mb = 1024 * 1024 * 100

    # Loop through all the files in path
    for filename in os.listdir(path):
        # Figure out the absolute path of this file
        absolute_filename = os.path.join(path, filename)

        # If it's a file, check to see if it's big enough
        if os.path.isfile(absolute_filename):
            file_size = os.path.getsize(absolute_filename)
            if file_size >= one_hundred_mb:
                # Convert file_size from bytes to megabytes. The int() function
                # makes size_in_mb an integer, basically chopping off the decimals
                size_in_mb = int(file_size / 1024 / 1024)
                print(f"{absolute_filename} is {size_in_mb}mb")

        # If it's a folder, then re-run this recursive function for the new folder
        if os.path.isdir(absolute_filename):
            files_bigger_than_100mb(absolute_filename)


def main():
    ncric_path = "/Volumes/datasets/BlueLeaks-extracted/ncric"
    files_bigger_than_100mb(ncric_path)


if __name__ == "__main__":
    main()
