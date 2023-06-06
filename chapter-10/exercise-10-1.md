# Exercise 10-1: Install BlueLeaks Explorer

In this exercise assignment you will install BlueLeaks Explorer. You must have Docker and Docker Compose installed. If you don't, go back and follow along in Chapter 6.

You can find the source code and instructions for installing BlueLeaks Explorer at https://github.com/micahflee/blueleaks-explorer.

## Create the Docker Compose Configuration File

Start by creating a new folder called `blueleaks-explorer` on your datasets USB disk, or somewhere else where you have at least 5GB of free disk space. Inside that folder, open a file called `docker-compose.yaml` in your text editor.

Here's how I did it on my Ubuntu computer:

```
micah@rogue:~$ cd /media/micah/datasets/
micah@rogue:/media/micah/datasets$ mkdir blueleaks-explorer
micah@rogue:/media/micah/datasets$ cd blueleaks-explorer/
micah@rogue:/media/micah/datasets/blueleaks-explorer$ code docker-compose.yaml
```

Here's how I did it in PowerShell on my Windows computer:

```
PS C:\Users\micah\code> cd D:\
PS D:\> mkdir blueleaks-explorer


    Directory: D:\


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         5/22/2022   7:06 PM                blueleaks-explorer


PS D:\> cd blueleaks-explorer
PS D:\blueleaks-explorer> code docker-compose.yaml
```

Inside this file, copy and paste this:

```yaml
version: "3.9"

services:
  app:
    image: micahflee/blueleaks-explorer:latest
    ports:
      - "8000:80"
    volumes:
      - /media/micah/datasets/BlueLeaks-extracted:/data/blueleaks
      - ./databases:/data/databases
      - ./structures:/data/structures
```

Change `/media/micah/datasets/BlueLeaks-extracted` to the path to the `BlueLeaks-extracted` folder on your computer.

If you're using Windows, use slashes (`/`) instead of backslashes (`\`) when specifying the path to the BlueLeaks data. For example, my data in Windows is at `D:\BlueLeaks-extracted`, so I set that volume line to:

```
      - D:/BlueLeaks-extracted:/data/blueleaks
```

## Bring Up the Containers

Now, in your terminal, in the `blueleaks-explorer` folder you just created, run:

```sh
docker-compose up
```

This will download the container image from Docker Hub and start running it on your computer. Here's what it looks like on mine:

```
micah@rogue:/media/micah/datasets/blueleaks-explorer$ docker-compose up
Creating network "blueleaks-explorer_default" with the default driver
Pulling app (micahflee/blueleaks-explorer:latest)...
latest: Pulling from micahflee/blueleaks-explorer
67e8aa6c8bbc: Pull complete
627e6c1e1055: Pull complete
0670968926f6: Pull complete
5a8b0e20be4b: Pull complete
b0b10a3a2784: Pull complete
e16cd24209e8: Pull complete
c8428195afac: Pull complete
45ae7839fda5: Pull complete
5ae8ff85c381: Pull complete
ea661cfc83d7: Pull complete
1fd3ea365e61: Pull complete
b5e3a2971758: Pull complete
031a4cb823a6: Pull complete
ac3249973cd0: Pull complete
21d53874befa: Pull complete
808d8b18683b: Pull complete
408248133d5a: Pull complete
b312070690e2: Pull complete
da13bd560733: Pull complete
15955ecc634c: Pull complete
0065bfbd6265: Pull complete
adf5a92be88f: Pull complete
37bfce78adfd: Pull complete
2417ebf6135a: Pull complete
307d5ae7538a: Pull complete
40fa082d7f45: Pull complete
Digest: sha256:83ce8cec1b8d5ff4f2fffef50b750d8aef7318ae8bf01827e22dbb7f30e1692b
Status: Downloaded newer image for micahflee/blueleaks-explorer:latest
Creating blueleaks-explorer_app_1 ... done
Attaching to blueleaks-explorer_app_1
app_1  |  * Serving Flask app 'app' (lazy loading)
app_1  |  * Environment: production
app_1  |    WARNING: This is a development server. Do not use it in a production deployment.
app_1  |    Use a production WSGI server instead.
app_1  |  * Debug mode: off
app_1  |  * Running on all addresses (0.0.0.0)
app_1  |    WARNING: This is a development server. Do not use it in a production deployment.
app_1  |  * Running on http://127.0.0.1:80
app_1  |  * Running on http://172.20.0.2:80 (Press CTRL+C to quit)
app_1  | 172.20.0.1 - - [22/May/2022 23:41:43] "GET / HTTP/1.1" 200 -
app_1  | 172.20.0.1 - - [22/May/2022 23:41:43] "GET /favicon.ico HTTP/1.1" 200 -
```

## Initialize the Database

Next, initialize the SQLite3 databases. Open a second terminal window, change to your `blueleaks-explorer` folder, and run this command:

```sh
docker-compose exec app poetry run python ./initialize.py
```

This will take a long time to finish running, and when it's done the `databases` folder inside your `blueleaks-explorer` folder will have 4.7GB of `.sqlite3` files in it.

Now, you can start using BlueLeaks Explorer by going to http://localhost:8000.
