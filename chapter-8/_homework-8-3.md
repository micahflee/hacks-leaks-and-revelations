# Homework 8-3: Traverse the Filesystem

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

## Find the Largest Files in BlueLeaks

Read this script which uses `os.walk()` to find all of the large files in BlueLeaks. You can also find it in [find-big-files.py](./find-big-files.py).

```py
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
```

When you run it:

```
micah@trapdoor chapter-8 % python3 find-big-files.py 
/Volumes/datasets/BlueLeaks-extracted/usao/usaoflntraining/files/VVSF00000/001.mp4 is 644MB
/Volumes/datasets/BlueLeaks-extracted/chicagoheat/html/ZA-CHICAGO HEaT_LR-20160830-034_Final 
Files.pdf is 102MB
/Volumes/datasets/BlueLeaks-extracted/nmhidta/files/RFIF300000/722.pdf is 148MB
/Volumes/datasets/BlueLeaks-extracted/nmhidta/files/RFIF200000/543.pdf is 161MB
/Volumes/datasets/BlueLeaks-extracted/nmhidta/files/RFIF100000/723.pdf is 206MB
/Volumes/datasets/BlueLeaks-extracted/fbicahouston/files/VVSF00000/002.mp4 is 145MB
/Volumes/datasets/BlueLeaks-extracted/fbicahouston/files/PSAVF100000/009.mp4 is 146MB
/Volumes/datasets/BlueLeaks-extracted/fbicahouston/files/PSAVF100000/026.mp4 is 105MB
--snip--
```