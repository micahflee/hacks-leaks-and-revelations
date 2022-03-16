# Homework 7-4: Command Line Arguments With Click

You can find my solution for this homework assignment in [homework-7-4.py](./homework-7-4py).

If you haven't installed the [Click](https://click.palletsprojects.com/) Python package yet, install it with pip:

```sh
pip3 install click
```

In this solution, the Python script starts by importing the two modules that we need, `os` and `click`:

```python
import os
import click
```

It then defines the `main()` function as a Click command. It takes a `path` argument, and it takes a `password` option. Click is smart enough so that, when the `main()` function is called, it passes in `path` and `password` as arguments to the function.

```python
@click.command()
@click.argument("path")
@click.option("--password", prompt="Enter password", help="Password is required")
def main(path, password):
    """Get information about files and folders"""
```

Just this code alone will create the help text for this CLI command:

```
micah@trapdoor chapter-7 % python3 homework-7-4.py --help         
Usage: homework-7-4.py [OPTIONS] PATH

  Get information about files and folders

Options:
  --password TEXT  Password is required
  --help           Show this message and exit.
```

The first requirement is make sure the password is `yourefired`, and if it's not quit with an error message. Here's the code that does that:

```python
    # Make sure the password is valid
    if password != "yourefired":
        click.echo("Access Denied")
        return
```

Just calling `return` will quit from the `main()` function early. If the password is anything except `yourefired`, the script quits early:

```
micah@trapdoor chapter-7 % python3 homework-7-4.py click-example.py --password letmein
Access Denied
```

The next step is to make sure that `path` is an actual valid path:

```python
    # Make sure the path is valid
    if not os.path.exists(path):
        click.echo("Error: Invalid path")
        return
```

If the path doesn't exist, it displays an error and quits early.

If we've made it past this check, we know for sure that it's a valid path. So the next step is to check to see if it's a file or a folder. In this solution I'm just using an if statement to check if `os.path.isfile(path)` is `True`. If it's false, the code assumes that it's a folder, and the else block runs.

```python
    # See if the path is a file
    if os.path.isfile(path):
        # Display information about this file
        # -

    # See if the path is a folder
    else:
        # Display information about this folder
        # --snip--
```

If the path is a file, the code looks up the file size and displays this information:

```python
        # Display information about this file
        file_size = os.path.getsize(path)
        click.echo(f"{path} is a file that is {file_size} bytes.")
```

If it's a folder, it's slightly more complicated. First, it loops through the output of `os.listdir(path)`, which is a list of all the files in the folder. Then for each filename in the output, if it's a file it displays the filename and its file size, and if it's a folder it just displays its filename:

```python
        # Display information about this folder
        click.echo(f"{path} is a folder. Here are the files inside it:")
        for filename in os.listdir(path):
            if os.path.isfile(os.path.join(path, filename)):
                file_size = os.path.getsize(os.path.join(path, filename))
                click.echo(f"- FILE: {filename} ({file_size} bytes)")
            else:
                click.echo(f"- FOLDER: {filename}")
```

Here is the script in action. In my case, I don't have a file called `does-not-exist` in my working folder, and I have a file called `Docker.dmg` and a few other files, and a folder called `old`, in my _Downloads_ folder.

```
micah@trapdoor chapter-7 % python3 homework-7-4.py does-not-exist
Enter password: letmein
Access Denied
micah@trapdoor chapter-7 % python3 homework-7-4.py does-not-exist
Enter password: yourefired
Error: Invalid path
micah@trapdoor chapter-7 % python3 homework-7-4.py ~/Downloads/Docker.dmg
Enter password: yourefired
/Users/micah/Downloads/Docker.dmg is a file that is 589068342 bytes.
micah@trapdoor chapter-7 % python3 homework-7-4.py ~/Downloads/ --password yourefired
/Users/micah/Downloads/ is a folder. Here are the files inside it:
- FILE: .DS_Store (6148 bytes)
- FILE: .localized (0 bytes)
- FOLDER: old
- FILE: Docker.dmg (589068342 bytes)
```