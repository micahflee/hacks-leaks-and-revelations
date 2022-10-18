import os


def main():
    blueleaks_path = "/Volumes/datasets/BlueLeaks-extracted"
    for bl_folder in os.listdir(blueleaks_path):
        bl_folder_path = os.path.join(blueleaks_path, bl_folder)

        if not os.path.isdir(bl_folder_path):
            continue

        files_count = 0
        folders_count = 0
        for filename in os.listdir(bl_folder_path):
            filename_path = os.path.join(bl_folder_path, filename)

            if os.path.isfile(filename_path):
                files_count += 1

            if os.path.isdir(filename_path):
                folders_count += 1

        print(f"{bl_folder} has {files_count} files, {folders_count} folders")


if __name__ == "__main__":
    main()
