# Exercise 5-5: Add Part of BlueLeaks to Aleph

You can see example files in the [aleph](./aleph/) folder.

If you're using Windows, use a PowerShell terminal.

## Start Aleph

```sh
docker-compose up
```

Example:

```
micah@trapdoor aleph % docker-compose up
[+] Running 14/14
 ⠿ Network aleph_default               Created                             0.1s
 ⠿ Volume "aleph_archive-data"         Created                             0.0s
 ⠿ Volume "aleph_elasticsearch-data"   Created                             0.0s
 ⠿ Volume "aleph_postgres-data"        Created                             0.0s
 ⠿ Volume "aleph_redis-data"           Created                             0.0s
 ⠿ Container aleph-postgres-1          Created                             0.1s
 ⠿ Container aleph-redis-1             Created                             0.1s
 ⠿ Container aleph-elasticsearch-1     Created                             0.1s
 ⠿ Container aleph-convert-document-1  Created                             0.1s
 ⠿ Container aleph-ingest-file-1       Created                             0.1s
 ⠿ Container aleph-worker-1            Created                             0.1s
 ⠿ Container aleph-shell-1             Created                             0.1s
 ⠿ Container aleph-api-1               Created                             0.1s
 ⠿ Container aleph-ui-1                Created                             0.1s
Attaching to aleph-api-1, aleph-convert-document-1, aleph-elasticsearch-1, aleph-ingest-file-1, aleph-postgres-1, aleph-redis-1, aleph-shell-1, aleph-ui-1, aleph-worker-1
aleph-postgres-1          | The files belonging to this database system will be owned by user "postgres".
aleph-postgres-1          | This user must also own the server process.
aleph-postgres-1          |
aleph-postgres-1          | The database cluster will be initialized with locale "en_US.utf8".
--snip--
```

## Mount Your Datasets into the Aleph Shell

```sh
docker-compose run --rm -v /Volumes/datasets:/datasets:ro shell bash
```

But replace `/Volumes/datasets` with the path to your `datasets` USB disk.

Example:

```
micah@trapdoor aleph % docker-compose run --rm -v /Volumes/datasets:/datasets:ro shell bash
Creating aleph_shell_run ... done
root@26430936533f:/aleph# ls -l /datasets/BlueLeaks-extracted/
total 0
drwx------ 511 root root 16352 Jun 15  2020 211sfbay
drwx------ 471 root root 15072 Jun 15  2020 acprlea
drwx------ 520 root root 16640 Jun 15  2020 acticaz
drwx------ 508 root root 16256 Jun 15  2020 akorca
drwx------ 520 root root 16640 Jun 15  2020 alabamafusioncenter
drwx------ 212 root root  6784 Jun 14  2020 alabamalecc
drwx------ 524 root root 16768 Jun 15  2020 alertmidsouth
--snip--
```

## Index the ICEFISHX Folder

To index `icefishx`, run this inside the Aleph shell:

```sh
aleph crawldir -l eng /datasets/BlueLeaks-extracted/icefishx
```

Example:

```
root@26430936533f:/aleph# aleph crawldir -l eng /datasets/BlueLeaks-extracted/icefishx
/usr/local/lib/python3.8/dist-packages/elasticsearch/connection/base.py:200: ElasticsearchWarning: Elasticsearch built-in security features are not enabled. Without authentication, your cluster could be accessible to anyone. See https://www.elastic.co/guide/en/elasticsearch/reference/7.16/security-minimal-setup.html to enable security.
  warnings.warn(message, category=ElasticsearchWarning)
2022-08-29 03:48:28.325943 [info     ] [directory:datasets-blueleaks-extracted-icefishx] Index: icefishx (0 things)... [aleph.index.collections] 
2022-08-29 03:48:28.339386 [info     ] Crawling /datasets/BlueLeaks-extracted/icefishx to directory:datasets-blueleaks-extracted-icefishx (2)... [aleph] 
2022-08-29 03:48:29.071292 [debug    ] Ingest entity [1.395e0293887ccdcb634e972f557865d43c548bbf]: .well-known [aleph.queues] 
2022-08-29 03:48:29.074166 [info     ] Crawl [2]: /datasets/BlueLeaks-extracted/icefishx/.well-known -> 1 [aleph.logic.documents] 
2022-08-29 03:48:29.088379 [debug    ] Ingest entity [2.a11dfaa9fcad7785c6d9bf2012791323c0a6e738]: acme-challenge [aleph.queues] 
2022-08-29 03:48:29.089654 [info     ] Crawl [2]: /datasets/BlueLeaks-extracted/icefishx/.well-known/acme-challenge -> 2 [aleph.logic.documents] 
2022-08-29 03:48:29.092373 [info     ] Archive: /data                 [servicelayer.archive.file] 
2022-08-29 03:48:29.131123 [debug    ] Ingest entity [3.8c5a4da8344e59452fbc9f82dd147c9c24dc5c2d]: 06uSRBjSlvuTsgGl1LWFHL5YeouWs4apx8sJIVNXuHk [aleph.queues] 
2022-08-29 03:48:29.132697 [info     ] Crawl [2]: /datasets/BlueLeaks-extracted/icefishx/.well-known/acme-challenge/06uSRBjSlvuTsgGl1LWFHL5YeouWs4apx8sJIVNXuHk -> 3 [aleph.logic.documents] 
2022-08-29 03:48:29.147325 [debug    ] Ingest entity [4.d4685ab4ad830bf1a327faef7ed41cdba65a51ad]: 08ZxpBp1CtWeP9IO_m8-f0WsmW9py14MRLCMuYDiYVo [aleph.queues] 
--snip--
```

This will take a long time to finish running. And even when it's done, it will take even longer to finish the actual indexing process. You can see the output of the indexing process in the other terminal running `docker-compose`.

You can see a list of datasets in Aleph by running:

```sh
aleph collections
```

Example:

```
root@bfdfdc1fc5a7:/aleph# aleph collections
Foreign ID                                         ID  Label
-----------------------------------------------  ----  --------
directory:datasets-blueleaks-extracted-icefishx     1  icefishx
```

You can check the status of indexing by running:

```sh
aleph status
```

Example:

```
root@bfdfdc1fc5a7:/aleph# aleph status
  Collection  Job                               Stage      Pending    Running    Finished
------------  --------------------------------  -------  ---------  ---------  ----------
           1                                                 19821          4        1731
           1  cf9c90ed26134bbf87374d2fbb4eae28  ingest       19779          2         606
           1  cf9c90ed26134bbf87374d2fbb4eae28  index            0          0         562
           1  cf9c90ed26134bbf87374d2fbb4eae28  analyze         42          2         563
```

Wait for it to finish indexing. It might take a few hours.

## Explore BlueLeaks Using Aleph

From your local Aleph server at http://127.0.0.1:8080/, starting searching. If you indexed ICEFISHX, try searching for `George Floyd`.
