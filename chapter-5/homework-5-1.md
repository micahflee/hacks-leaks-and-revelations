# Homework 5-1: Unzip BlueLeaks

## macOS and Linux Users

The simple shell script that unzips all of the files in BlueLeaks is [homework-5-1-unzip.sh](./homework-5-1-unzip.sh).

## Windows Users

Because decompressing files is very disk intensive, it's much faster to use Windows tools directly instead of Linux tools in WSL. Install 7-Zip, which you can [download from here](https://www.7-zip.org/). Then add `C:\Program Files\7-Zip` [to your path](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/), which will allow you to use the CLI version of 7-Zip just by running the `7z` command.

The simple PowerShell script that unzips all of the files in BlueLeaks is [homework-5-1-unzip.ps1](./homework-5-1-unzip.ps1).

## Organize Your Files

After unzipping BlueLeaks, open a terminal (Windows users should use a WSL terminal), change to your datasets USB disk, and run this:

```sh
mv BlueLeaks BlueLeaks-extracted
mkdir BlueLeaks
mv BlueLeaks-extracted/*.zip BlueLeaks
```