# Homework 5-4: Run Aleph Locally in Linux Containers

Make a new homework folder just for this assignment. Follow the [production deployment instructions](https://docs.alephdata.org/developers/installation#production-deployment) in the [Aleph documentation](https://docs.alephdata.org/).

## Configure Aleph and Start the Containers

In short, you'll need to:

Save a copy of Aleph's [docker-compose.yml](https://github.com/alephdata/aleph/blob/main/docker-compose.yml) and [aleph.env.tmpl](https://github.com/alephdata/aleph/blob/main/aleph.env.tmpl) from Aleph’s git repo into your assignment folder. After you do this you should have these two files:

```
micah@trapdoor homework-5-4 % ls -l
total 16
-rw-r--r--  1 micah  staff  2931 Feb 10 20:31 aleph.env.tmpl
-rw-r--r--  1 micah  staff  2247 Feb 10 20:31 docker-compose.yml
```

Make a copy of `aleph.env.tmpl` called `aleph.env`. You can do this by running:

```sh
cp aleph.env.tmpl aleph.env
```

Example:

```
micah@trapdoor homework-5-4 % cp aleph.env.tmpl aleph.env      
micah@trapdoor homework-5-4 % ls -l 
total 24
-rw-r--r--  1 micah  staff  2931 Feb 25 09:20 aleph.env
-rw-r--r--  1 micah  staff  2931 Feb 10 20:31 aleph.env.tmpl
-rw-r--r--  1 micah  staff  2247 Feb 10 20:31 docker-compose.yml
```

Open `aleph.env` in your text editor. Set a random value for `ALEPH_SECRET_KEY`. You can generate this value by running:

```sh
openssl rand -hex 24
```

Example:

```
micah@trapdoor homework-5-4 % openssl rand -hex 24
f8b1afa480cec3574750d0d2a0f19b9484ea49d42a58c236
```

Save the file.