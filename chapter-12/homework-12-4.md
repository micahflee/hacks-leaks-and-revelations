# Homework 12-4: Import Epik Data Into MySQL

In this homework you'll import `api_system.sql` into the MySQL database you started running in [Homework 12-2](./homework-12-2.md). Start by making sure your docker containers are up and running.

## Install `pv`

This is a large SQL file that will take a long time to import, so you'll want to use a CLI program called `pv` (which stands for Pipe Viewer) so you can get a progress bar while you import. Install `pv` like this:

If you're using macOS: `brew install pv`
If you're using Linux or Windows with WSL: `sudo apt install pv`

## Import the database

Open a terminal and change to the folder that has `api_system.sql`.

Import the database, with a `pv` progress bar, by running:

```sh
pv api_system.sql | mysql -h localhost --protocol=tcp -u root -p epikfail_api_system
```

You'll need to enter the root password to your MySQL server, which you'll find in your `docker-compose.yaml` folder. For example:

```
micah@trapdoor sql % pv api_system.sql | mysql -h localhost --protocol=tcp -u root -p epikfail_api_system
Enter password: 
2.89GiB 0:33:47 [ 587KiB/s] [=====>                          ] 14% ETA 3:14:56
```

In that example, I had been running the import for 33 minutes and 47 seconds, it had gone through 2.89GB of the data (14%), it estimated it would finish in 3 hours and 15 minutes, and it was currently importing at the speed of 587KB each second--though, the import speed varies greatly depending on which query it’s currently running. It took me a total of four hours to import `api_system.sql` (although I probably could have made it faster by tweaking the Desktop Desktop settings on my Mac to use more CPUs or memory).