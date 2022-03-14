import os

# This function take a filename as a parameter, return True if the file is a video,
# and otherwise returns False
def is_video_file(filename):
    video_extensions = [".mp4", ".avi", ".mov", ".mpeg", ".ogv"]
    for ext in video_extensions:
        if filename.lower().endswith(ext):
            return True

    return False


def main():
    # Walk the BlueLeaks folder tree
    blueleaks_path = "/Volumes/datasets/BlueLeaks-extracted"
    for dirname, dirnames, filenames in os.walk(blueleaks_path):
        for filename in filenames:
            absolute_filename = os.path.join(dirname, filename)
            if is_video_file(absolute_filename):
                print(absolute_filename)


main()
