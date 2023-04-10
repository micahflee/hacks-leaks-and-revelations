# Homework 11-1: Download the Parler Video Metadata

**NOTE:** If you're using Windows, I recommend that you follow the instructions in this chapter using your Ubuntu terminal instead of PowerShell, and that you save this data in your Ubuntu home folder, like in `~/datasets`, instead of using your Windows-formatted USB disk, like in `/mnt/d`. I found that working with this data in Linux was significantly faster than in directly in Windows.

Read the instructions on the _DDoSecrets_ [Parler page](https://ddosecrets.com/wiki/Parler).

Open a terminal, change to your datasets USB disk (or, in Windows, create a `~/datasets` folder and change to that), create a _Parler_ folder, and use the `wget` command to download the list of filenames and the video metadata:

```sh
cd ~/datasets
mkdir Parler
cd Parler
wget https://data.ddosecrets.com/Parler/Videos/ddosecrets-parler-listing.txt.gz
wget https://data.ddosecrets.com/Parler/Videos/metadata.tar.gz
```

For example:

```
micah@cloak:~$ cd ~/datasets
micah@cloak:~/datasets$ mkdir Parler
micah@cloak:~/datasets$ cd Parler/
micah@cloak:~/datasets/Parler$
micah@cloak:~/datasets/Parler$ wget https://data.ddosecrets.com/Parler/Videos/ddosecrets-parler-listing.txt.gz
--2023-04-09 17:34:36--  https://data.ddosecrets.com/Parler/Videos/ddosecrets-parler-listing.txt.gz
Resolving data.ddosecrets.com (data.ddosecrets.com)... 172.67.75.15, 104.26.3.199, 104.26.2.199
Connecting to data.ddosecrets.com (data.ddosecrets.com)|172.67.75.15|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17790173 (17M) [application/octet-stream]
Saving to: ‘ddosecrets-parler-listing.txt.gz’

ddosecrets-parler-listin 100%[================================>]  16.97M  13.5MB/s    in 1.3s    

2023-04-09 17:34:38 (13.5 MB/s) - ‘ddosecrets-parler-listing.txt.gz’ saved [17790173/17790173]

micah@cloak:~/datasets/Parler$ wget https://data.ddosecrets.com/Parler/Videos/metadata.tar.gz
--2023-04-09 17:34:55--  https://data.ddosecrets.com/Parler/Videos/metadata.tar.gz
Resolving data.ddosecrets.com (data.ddosecrets.com)... 172.67.75.15, 104.26.3.199, 104.26.2.199
Connecting to data.ddosecrets.com (data.ddosecrets.com)|172.67.75.15|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 212461278 (203M) [application/octet-stream]
Saving to: ‘metadata.tar.gz’

metadata.tar.gz          100%[================================>] 202.62M  21.3MB/s    in 9.6s    

2023-04-09 17:35:06 (21.0 MB/s) - ‘metadata.tar.gz’ saved [212461278/212461278]

micah@cloak:~/datasets/Parler$ ls -lh
total 220M
-rw-r--r-- 1 micah micah  17M Mar 28  2021 ddosecrets-parler-listing.txt.gz
-rw-r--r-- 1 micah micah 203M Mar 15  2021 metadata.tar.gz
micah@cloak:~/datasets/Parler$
```

Both of these files are compressed.

## List of Video Filenames

Decompress the list of video filenames:

```sh
gunzip ddosecrets-parler-listing.txt.gz
```

For example:

```
micah@cloak:~/datasets/Parler$ gunzip ddosecrets-parler-listing.txt.gz
micah@cloak:~/datasets/Parler$ ls -lh
total 246M
-rw-r--r-- 1 micah micah  44M Mar 28  2021 ddosecrets-parler-listing.txt
-rw-r--r-- 1 micah micah 203M Mar 15  2021 metadata.tar.gz
micah@cloak:~/datasets/Parler$ cat ddosecrets-parler-listing.txt | wc -l
1031509
```

It has 1,031,509 lines. Open _ddosecrets-parler-listing.txt_ in a text editor. Here's what it looks like:

![Viewing filenames in a text editor](./homework-11-1-filenames.png)

The last column of each line is a filename. For example, if you want to download the video with the filename of _0003lx5cSwSB_, you will download `https://data.ddosecrets.com/Parler/Videos/0003lx5cSwSB`. Give it a try. In this case, I’m creating a new folder called videos to download the videos into.

```sh
mkdir videos
cd videos
wget https://data.ddosecrets.com/Parler/Videos/0003lx5cSwSB
```

For example:

```
micah@cloak:~/datasets/Parler$ mkdir videos
micah@cloak:~/datasets/Parler$ cd videos/
micah@cloak:~/datasets/Parler/videos$ wget https://data.ddosecrets.com/Parler/Videos/0003lx5cSwSB
--2022-04-22 14:54:51--  https://data.ddosecrets.com/Parler/Videos/0003lx5cSwSB
--2023-04-09 17:35:29--  https://data.ddosecrets.com/Parler/Videos/0003lx5cSwSB
Resolving data.ddosecrets.com (data.ddosecrets.com)... 104.26.2.199, 172.67.75.15, 104.26.3.199
Connecting to data.ddosecrets.com (data.ddosecrets.com)|104.26.2.199|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 14586730 (14M) [application/octet-stream]
Saving to: ‘0003lx5cSwSB’

0003lx5cSwSB             100%[================================>]  13.91M  9.64MB/s    in 1.4s    

2023-04-09 17:35:32 (9.64 MB/s) - ‘0003lx5cSwSB’ saved [14586730/14586730]
```

To watch the videos, you must rename them to have the file extension _.mp4_. You can rename this file like:

```sh
mv 0003lx5cSwSB 0003lx5cSwSB.mp4
```

Now you can watch the video using software like [VLC Media Player](https://www.videolan.org/).

## Video Metadata

In your terminal, change back to the _Parler_ dataset folder and decompress _metadata.tar.gz` like this:

```sh
tar -xvf metadata.tar.gz
```

For example:

```
micah@cloak:~/datasets/Parler/videos$ cd ..
micah@cloak:~/datasets/Parler$ tar -xvf metadata.tar.gz
metadata/
metadata/.aws/
metadata/meta-00CnBY5xCdca.json
metadata/meta-0003lx5cSwSB.json
metadata/meta-0070HNolzi3z.json
metadata/meta-00BIFOMnOyi1.json
metadata/meta-0002bz1GNsUP.json
metadata/meta-0015NlY0yUB5.json
metadata/meta-00DeGeeF9M25.json
--snip--
```