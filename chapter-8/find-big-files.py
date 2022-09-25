import os


def main():
    one_hundred_mb = 1024 * 1024 * 100

    blueleaks_path = "/Volumes/datasets/BlueLeaks-extracted"
    for dirname, dirnames, filenames in os.walk(blueleaks_path):
        for filename in filenames:
            absolute_filename = os.path.join(dirname, filename)
            file_size = os.path.getsize(absolute_filename)
            if file_size >= one_hundred_mb:
                # Convert file_size from bytes to megabytes
                size_in_mb = int(file_size / 1024 / 1024)
                print(f"{absolute_filename} is {size_in_mb}MB")


if __name__ == "__main__":
    main()
