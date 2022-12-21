# Homework 5-2 for Linux users: Install Docker Engine

Find instructions for installing Docker Engine in Linux [here](https://docs.docker.com/engine/install/). My Linux computer is running Ubuntu, so I'm going to follow the [Ubuntu instructions](https://docs.docker.com/engine/install/ubuntu/).

First, I will make sure I have some important packages installed:

```sh
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
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

Finally, I will install Docker Engine:

```sh
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Docker Engine is now installed. To make sure it works properly, run:

```sh
sudo docker run hello-world
```

You will also need to install the `docker-compose` package:

```sh
sudo apt install docker-compose
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
