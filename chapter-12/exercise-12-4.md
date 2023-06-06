# Exercise 12-4: Download and Extract Part of the Epik Dataset

You can read about the Epik dataset, and find links to the torrents to download it, at https://ddosecrets.com/wiki/Epik.

This dataset is split into three parts and it's very large: Part one is 180GB, part two is 72GB, and part three is 104GB. 

Download the `api_system.sql.gz`, a backup of a MySQL database, from https://data.ddosecrets.com/Epik/EpikFail/sql/api_system.sql.gz.

Extract `api_system.sql.gz` by running:

```sh
gunzip api_system.sql.gz
```

The origin `.sql.gz` file is 1.2GB, but the extracted one should be 20GB.