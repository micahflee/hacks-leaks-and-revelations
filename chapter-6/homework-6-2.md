# Homework 6-2 for Linux users: Install Docker CE

Find instructions for installing Docker CE in Linux [here](https://docs.docker.com/engine/install/). My Linux computer is running Ubuntu, so I'm going to follow the [Ubuntu instructions](https://docs.docker.com/engine/install/ubuntu/).

First, I will make sure I have some important packages installed:

```sh
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

For example:

```
micah@rogue:~$ sudo apt-get update
Hit:1 https://updates.signal.org/desktop/apt xenial InRelease
Hit:3 http://us.archive.ubuntu.com/ubuntu impish InRelease                                                                                            
Hit:4 http://security.ubuntu.com/ubuntu impish-security InRelease
Hit:5 http://us.archive.ubuntu.com/ubuntu impish-updates InRelease
Hit:6 http://us.archive.ubuntu.com/ubuntu impish-backports InRelease  
Hit:2 https://packagecloud.io/firstlookmedia/code/ubuntu impish InRelease
Reading package lists... Done
micah@rogue:~$ sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
ca-certificates is already the newest version (20210119ubuntu1).
curl is already the newest version (7.74.0-1.3ubuntu2).
gnupg is already the newest version (2.2.20-1ubuntu4).
lsb-release is already the newest version (11.1.0ubuntu3).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

Then I will import the signing key that Docker uses to make its Ubuntu repository secure:

```sh
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

Then I will add the Docker repository to my computer:

```sh
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Finally, I will install Docker CE:

```sh
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

For example:

```
micah@rogue:~$ sudo apt-get update
Hit:1 https://download.docker.com/linux/ubuntu impish InRelease
Hit:3 https://updates.signal.org/desktop/apt xenial InRelease                                           
Hit:4 http://us.archive.ubuntu.com/ubuntu impish InRelease                        
Hit:5 http://us.archive.ubuntu.com/ubuntu impish-updates InRelease                                                                        
Hit:2 https://packagecloud.io/firstlookmedia/code/ubuntu impish InRelease                                                                 
Hit:6 http://security.ubuntu.com/ubuntu impish-security InRelease   
Hit:7 http://us.archive.ubuntu.com/ubuntu impish-backports InRelease
Reading package lists... Done
micah@rogue:~$ sudo apt-get install docker-ce docker-ce-cli containerd.io
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  docker-ce-rootless-extras docker-scan-plugin pigz
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-ce docker-ce-cli docker-ce-rootless-extras docker-scan-plugin pigz
0 upgraded, 6 newly installed, 0 to remove and 0 not upgraded.
Need to get 0 B/96.3 MB of archives.
After this operation, 405 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Selecting previously unselected package pigz.
(Reading database ... 190869 files and directories currently installed.)
Preparing to unpack .../0-pigz_2.6-1_amd64.deb ...
Unpacking pigz (2.6-1) ...
Selecting previously unselected package containerd.io.
Preparing to unpack .../1-containerd.io_1.5.11-1_amd64.deb ...
Unpacking containerd.io (1.5.11-1) ...
Selecting previously unselected package docker-ce-cli.
Preparing to unpack .../2-docker-ce-cli_5%3a20.10.14~3-0~ubuntu-impish_amd64.deb ...
Unpacking docker-ce-cli (5:20.10.14~3-0~ubuntu-impish) ...
Selecting previously unselected package docker-ce.
Preparing to unpack .../3-docker-ce_5%3a20.10.14~3-0~ubuntu-impish_amd64.deb ...
Unpacking docker-ce (5:20.10.14~3-0~ubuntu-impish) ...
Selecting previously unselected package docker-ce-rootless-extras.
Preparing to unpack .../4-docker-ce-rootless-extras_5%3a20.10.14~3-0~ubuntu-impish_amd64.deb ...
Unpacking docker-ce-rootless-extras (5:20.10.14~3-0~ubuntu-impish) ...
Selecting previously unselected package docker-scan-plugin.
Preparing to unpack .../5-docker-scan-plugin_0.17.0~ubuntu-impish_amd64.deb ...
Unpacking docker-scan-plugin (0.17.0~ubuntu-impish) ...
Setting up docker-scan-plugin (0.17.0~ubuntu-impish) ...
Setting up containerd.io (1.5.11-1) ...
Setting up docker-ce-cli (5:20.10.14~3-0~ubuntu-impish) ...
Setting up pigz (2.6-1) ...
Setting up docker-ce-rootless-extras (5:20.10.14~3-0~ubuntu-impish) ...
Setting up docker-ce (5:20.10.14~3-0~ubuntu-impish) ...
Processing triggers for man-db (2.9.4-2) ...
```

You will also need to install the `docker-compose` package:

```sh
sudo apt install docker-compose
```

Docker CE is now installed. To make sure it works properly, run:

```sh
sudo docker run hello-world
```

For example:

```
micah@rogue:~$ sudo docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete 
Digest: sha256:bfea6278a0a267fad2634554f4f0c6f31981eea41c553fdf5a83e95a41d40c38
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

micah@rogue:~$ 
```
