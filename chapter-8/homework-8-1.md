# Homework 8-1: Traverse the Filesystem

## List the Filenames in a Folder

Read this simple script, which you can also find in [list-files1.py](./list-files1.py):

```py
import os


def main():
    blueleaks_path = "/Volumes/datasets/BlueLeaks-extracted"

    for filename in os.listdir(blueleaks_path):
        print(filename)


if __name__ == "__main__":
    main()
```

When you run it:

```
micah@trapdoor chapter-8 % python3 list-files.py
211sfbay
Securitypartnership
acprlea
acticaz
akorca
--snip--
```

## Count the Files and Folders in a Folder

Read this more complicated script, which you can also find in [list-files2.py](./list-files2.py):

```py
import os


def main():
    blueleaks_path = "/Volumes/datasets/BlueLeaks-extracted"
    for bl_folder in os.listdir(blueleaks_path):
        bl_folder_path = os.path.join(blueleaks_path, bl_folder)

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
```

When you run it:

```
micah@trapdoor chapter-8 % python3 list-files2.py
bostonbric has 506 files, 10 folders
terrorismtip has 207 files, 0 folders
ociac has 216 files, 1 folders
usao has 0 files, 84 folders
alertmidsouth has 512 files, 10 folders
chicagoheat has 499 files, 10 folders
--snip--
```
