# Homework 8-3: List All the Videos in BlueLeaks

You can find my solution for this homework assignment in [homework-8-3.py](./homework-8-3py).

This solution defines a function called `is_video_file()` which takes a filename as a parameter and returns either `True` or `False`, depending on the filename's extension.

```py
# This function take a filename as a parameter, returns True if the file is a video,
# and otherwise returns False
def is_video_file(filename):
    video_extensions = [".mp4", ".avi", ".mov", ".mpeg", ".ogv"]
    for ext in video_extensions:
        if filename.lower().endswith(ext):
            return True

    return False
```

To avoid having a really long if statement, this creates a list of video file extensions called `video_extensions` and loops through this list, to check each extension one at a time. If it finds one, it immediately returns `True`, which quits the function early. If it doesn't find any, then it returns `False`.

Here's another way to implement this same function using a large if statement instead of a for loop:

```python
def is_video_file(filename):
    if (
        filename.lower().endswith(".mp4")
        or filename.lower().endswith(".avi")
        or filename.lower().endswith(".mov")
        or filename.lower().endswith(".mpeg")
        or filename.lower().endswith(".ogv")
    ):
        return True

    return False
```

Either way works fine.

Then, in the `main()` function, my solution uses `os.walk()` to walk through the BlueLeaks folder and calls `is_video_file()` on every file in BlueLeaks, printing out the filenames that are videos.

```python
def main():
    # Walk the BlueLeaks folder tree
    blueleaks_path = "/Volumes/datasets/BlueLeaks-extracted"
    for dirname, dirnames, filenames in os.walk(blueleaks_path):
        for filename in filenames:
            absolute_filename = os.path.join(dirname, filename)
            if is_video_file(absolute_filename):
                print(absolute_filename)
```

Finally, the last line in my solution calls the `main()` function, which kicks off the actual script.
