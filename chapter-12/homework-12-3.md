# Homework 12-3: Extract the Epik Data

In [Homework 12-1](./homework-12-1.md) you downloaded 25GB of Epik data from two separate torrents. In this homework you'll extract this data.

The MySQL database data is in the `EpikFail/sql` folder, and the Texas GOP website data is in the `EpikFailYouLostTheGame` folder. Here's what's in these folders:

```
micah@trapdoor ~ % ls -lh /Volumes/datasets/Epik/EpikFail/sql
total 27626816
-rw-r--r--  1 micah  staff   1.2G Jun 10 13:46 api_system.sql.gz
-rw-r--r--  1 micah  staff   1.7M Jun 10 13:46 epik_anonymize.sql.gz
-rw-r--r--  1 micah  staff    50M Jun 10 13:45 epik_mydns.sql.gz
-rw-r--r--  1 micah  staff   7.9G Jun 10 13:52 intrust.sql.gz
-rw-r--r--  1 micah  staff    18M Jun 10 13:52 mydns.sql.gz
-rw-r--r--  1 micah  staff   839K Jun 10 13:52 mysql.sql.gz
-rw-r--r--  1 micah  staff   581M Jun 10 13:45 pdns.sql.gz
-rw-r--r--  1 micah  staff    37M Jun 10 13:45 redirmail.sql.gz
-rw-r--r--  1 micah  staff   3.4G Jun 10 13:54 whois.sql.gz
micah@trapdoor ~ % ls -lh /Volumes/datasets/Epik/EpikFailYouLostTheGame 
total 20744384
-rw-r--r--  1 micah  staff   8.9K Jun  5 19:52 README.TXT
-rw-r--r--  1 micah  staff   9.9G Jun  5 21:48 gopfiles.tar.gz
-rw-r--r--  1 micah  staff    33M Jun  5 20:05 texasgop.sql.gz
````

## Extract the MySQL Databases

Open a terminal, change to the `EpikFail/sql` folder, and run this for loop in your shell to extract all of the gzip-compressed files:

```sh
for FILENAME in $(ls *.gz)
do
    echo "extracting $FILENAME"
    gunzip $FILENAME
done
```

For example:

```
micah@trapdoor sql % for FILENAME in $(ls *.gz)
do
    echo "extracting $FILENAME"
    gunzip $FILENAME
done
extracting api_system.sql.gz
extracting epik_anonymize.sql.gz
extracting epik_mydns.sql.gz
extracting intrust.sql.gz
extracting mydns.sql.gz
extracting mysql.sql.gz
extracting pdns.sql.gz
extracting redirmail.sql.gz
extracting whois.sql.gz
```

It took me 40 minutes to extract this data on my USB hard disk, on my Mac. When it's done, you'll end up with 145GB of extracted data.

## Extract the Texas GOP Data

In your terminal, change to your `EpikFailYouLostTheGame` folder.

Extract `gopfiles.tar.gz` like this:

```sh
tar -xvf gopfiles.tar.gz
```

For example:

```
micah@trapdoor EpikFailYouLostTheGame % time tar -xvf gopfiles.tar.gz
x backup-9.8.2021_03-00-16_texa2910/
x backup-9.8.2021_03-00-16_texa2910/mysql_host_notes.json
x backup-9.8.2021_03-00-16_texa2910/bandwidth_db.json
x backup-9.8.2021_03-00-16_texa2910/vf/
x backup-9.8.2021_03-00-16_texa2910/vf/demo.texasgop.org
x backup-9.8.2021_03-00-16_texa2910/vf/dev.texasgop.org
x backup-9.8.2021_03-00-16_texa2910/vf/texasgop.org
x backup-9.8.2021_03-00-16_texa2910/autossl.json
x backup-9.8.2021_03-00-16_texa2910/quota
x backup-9.8.2021_03-00-16_texa2910/suspendinfo/
x backup-9.8.2021_03-00-16_texa2910/sds
x backup-9.8.2021_03-00-16_texa2910/httpfiles/
x backup-9.8.2021_03-00-16_texa2910/userdata/
x backup-9.8.2021_03-00-16_texa2910/userdata/texasgop.org_SSL
x backup-9.8.2021_03-00-16_texa2910/userdata/dev.texasgop.org.php-fpm.yaml
x backup-9.8.2021_03-00-16_texa2910/userdata/demo.texasgop.org
x backup-9.8.2021_03-00-16_texa2910/userdata/main
x backup-9.8.2021_03-00-16_texa2910/userdata/cache.json
x backup-9.8.2021_03-00-16_texa2910/userdata/demo.texasgop.org_SSL
x backup-9.8.2021_03-00-16_texa2910/userdata/demo.texasgop.org.php-fpm.yaml
x backup-9.8.2021_03-00-16_texa2910/userdata/dev.texasgop.org
x backup-9.8.2021_03-00-16_texa2910/userdata/texasgop.org
--snip--
```

This is a very large file so it will take some time to finish extracting. It took me 15 minutes.

And extract `texasgop.sql.gz` like this:

```sh
gunzip texasgop.sql.gz
```
