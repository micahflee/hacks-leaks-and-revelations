import os


def main():
    # The path to the BlueLeaks dataset. Change this to match your path.
    blueleaks_path = "/mnt/f/BlueLeaks-extracted"

    # Loop through each of the filenames returns by os.listdir()
    for filename in os.listdir(blueleaks_path):
        # Display each filename
        print(filename)


main()
