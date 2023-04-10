# Homework 12-2: Install and Test the Command Line MySQL Client

## Install the Command Line MySQL Client

If you're using macOS: `brew install mariadb`

If you're using Linux or Windows with WSL: `sudo apt install mariadb-client`

## Connect to MySQL

Make sure you MySQL server is from [Homework 12-2](./homework-12-2.md) is running, and then connect to it with:

```sh
mysql -h localhost --protocol=tcp -u root -p
```

You'll need to type the root database password. For example:

```
user@chaos chapter-12 % mysql -h localhost --protocol=tcp -u root -p                                                                                    (git)-[main] 
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3
Server version: 10.9.4-MariaDB-1:10.9.4+maria~ubu2204 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 
```

## Practice Queries

Practice the MySQL-specific queries described in the book.