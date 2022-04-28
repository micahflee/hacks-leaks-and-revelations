# Homework 6-5: Index Part of BlueLeaks in Aleph

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

## Mount Your Datasets Disk as a Volume in the Aleph Shell Container

```sh
docker-compose run --rm -v /Volumes/datasets:/datasets shell bash
```

Example:

```
micah@trapdoor aleph % docker-compose run --rm -v /Volumes/datasets:/datasets shell bash
[+] Running 6/0
 ⠿ Container aleph-convert-document-1  Running                               0.0s
 ⠿ Container aleph-elasticsearch-1     Running                               0.0s
 ⠿ Container aleph-redis-1             Running                               0.0s
 ⠿ Container aleph-postgres-1          Running                               0.0s
 ⠿ Container aleph-ingest-file-1       Running                               0.0s
 ⠿ Container aleph-worker-1            Running                               0.0s
root@43515650c82f:/aleph# ls -l /datasets/BlueLeaks-extracted/
total 0
drwx------ 511 root root 16352 Jun 15  2020 211sfbay
drwx------ 471 root root 15072 Jun 15  2020 acprlea
drwx------ 520 root root 16640 Jun 15  2020 acticaz
drwx------ 508 root root 16256 Jun 15  2020 akorca
drwx------ 520 root root 16640 Jun 15  2020 alabamafusioncenter
drwx------ 212 root root  6784 Jun 14  2020 alabamalecc
drwx------ 524 root root 16768 Jun 15  2020 alertmidsouth
drwx------ 517 root root 16544 Jun 15  2020 aorca
drwx------ 227 root root  7264 Jun 14  2020 arictexas
drwx------ 473 root root 15136 Jun 15  2020 atlantahidta
drwx------ 525 root root 16800 Jun 15  2020 attackwa
drwx------ 490 root root 15680 Jun 15  2020 azhidta
--snip--
```

## Index Part of BlueLeaks

To index `icefishx`:

```sh
aleph crawldir /datasets/BlueLeaks-extracted/icefishx
```

Example:

```
root@bfdfdc1fc5a7:/aleph# aleph crawldir /datasets/BlueLeaks-extracted/icefishx
/usr/local/lib/python3.8/dist-packages/elasticsearch/connection/base.py:200: ElasticsearchWarning: Elasticsearch built-in security features are not enabled. Without authentication, your cluster could be accessible to anyone. See https://www.elastic.co/guide/en/elasticsearch/reference/7.16/security-minimal-setup.html to enable security.
  warnings.warn(message, category=ElasticsearchWarning)
{"logger": "aleph.index.collections", "timestamp": "2022-02-25 20:32:50.846809", "message": "[directory:datasets-blueleaks-extracted-icefishx] Index: icefishx (0 things)...", "severity": "INFO"}
{"logger": "aleph", "timestamp": "2022-02-25 20:32:50.870573", "message": "Crawling /datasets/BlueLeaks-extracted/icefishx to directory:datasets-blueleaks-extracted-icefishx (1)...", "severity": "INFO"}
{"logger": "aleph.queues", "timestamp": "2022-02-25 20:32:54.277962", "message": "Ingest entity [1.395e0293887ccdcb634e972f557865d43c548bbf]: .well-known", "severity": "DEBUG"}
{"logger": "aleph.logic.documents", "timestamp": "2022-02-25 20:32:54.280696", "message": "Crawl [1]: /datasets/BlueLeaks-extracted/icefishx/.well-known -> 1", "severity": "INFO"}
{"logger": "aleph.queues", "timestamp": "2022-02-25 20:32:54.306067", "message": "Ingest entity [2.a11dfaa9fcad7785c6d9bf2012791323c0a6e738]: acme-challenge", "severity": "DEBUG"}
{"logger": "aleph.logic.documents", "timestamp": "2022-02-25 20:32:54.307944", "message": "Crawl [1]: /datasets/BlueLeaks-extracted/icefishx/.well-known/acme-challenge -> 2", "severity": "INFO"}
{"logger": "servicelayer.archive.file", "timestamp": "2022-02-25 20:32:54.311600", "message": "Archive: /data", "severity": "INFO"}
{"logger": "aleph.queues", "timestamp": "2022-02-25 20:32:54.365209", "message": "Ingest entity [3.8c5a4da8344e59452fbc9f82dd147c9c24dc5c2d]: 06uSRBjSlvuTsgGl1LWFHL5YeouWs4apx8sJIVNXuHk", "severity": "DEBUG"}
{"logger": "aleph.logic.documents", "timestamp": "2022-02-25 20:32:54.367499", "message": "Crawl [1]: /datasets/BlueLeaks-extracted/icefishx/.well-known/acme-challenge/06uSRBjSlvuTsgGl1LWFHL5YeouWs4apx8sJIVNXuHk -> 3", "severity": "INFO"}
{"logger": "aleph.queues", "timestamp": "2022-02-25 20:32:54.385031", "message": "Ingest entity [4.d4685ab4ad830bf1a327faef7ed41cdba65a51ad]: 08ZxpBp1CtWeP9IO_m8-f0WsmW9py14MRLCMuYDiYVo", "severity": "DEBUG"}
{"logger": "aleph.logic.documents", "timestamp": "2022-02-25 20:32:54.386638", "message": "Crawl [1]: /datasets/BlueLeaks-extracted/icefishx/.well-known/acme-challenge/08ZxpBp1CtWeP9IO_m8-f0WsmW9py14MRLCMuYDiYVo -> 4", "severity": "INFO"}
{"logger": "aleph.queues", "timestamp": "2022-02-25 20:32:54.409336", "message": "Ingest entity [5.06a6da1dc9cb9a4c3cf3143fb7863c1df3d7d9e0]: 6rNQ_2f9Wa3rKeXnbhfB5hPYI3ISQ4X7LPLTm3J8JRo", "severity": "DEBUG"}
{"logger": "aleph.logic.documents", "timestamp": "2022-02-25 20:32:54.411273", "message": "Crawl [1]: /datasets/BlueLeaks-extracted/icefishx/.well-known/acme-challenge/6rNQ_2f9Wa3rKeXnbhfB5hPYI3ISQ4X7LPLTm3J8JRo -> 5", "severity": "INFO"}
{"logger": "aleph.queues", "timestamp": "2022-02-25 20:32:54.429754", "message": "Ingest entity [6.a63daaf043182f19917db460ce2fa64fd042e3f8]: C_HHhMTvTuz3R7ZHtQC4FzVcsfCANM0Q1eEUJq_3qlQ", "severity": "DEBUG"}
{"logger": "aleph.logic.documents", "timestamp": "2022-02-25 20:32:54.431552", "message": "Crawl [1]: /datasets/BlueLeaks-extracted/icefishx/.well-known/acme-challenge/C_HHhMTvTuz3R7ZHtQC4FzVcsfCANM0Q1eEUJq_3qlQ -> 6", "severity": "INFO"}
{"logger": "aleph.queues", "timestamp": "2022-02-25 20:32:54.500918", "message": "Ingest entity [7.77c326fe5d0484746c34594d48842593b3ee122f]: PZt7cxnNvzaZRfHlxNWYQLhgkGZ_8UAZXgYPFOe5Aps", "severity": "DEBUG"}
{"logger": "aleph.logic.documents", "timestamp": "2022-02-25 20:32:54.502582", "message": "Crawl [1]: /datasets/BlueLeaks-extracted/icefishx/.well-known/acme-challenge/PZt7cxnNvzaZRfHlxNWYQLhgkGZ_8UAZXgYPFOe5Aps -> 7", "severity": "INFO"}
{"logger": "aleph.queues", "timestamp": "2022-02-25 20:32:54.536177", "message": "Ingest entity [8.a0efc5dd9c5ae7135a3a84bee81cfa2a312cc5b6]: Ps3yr1AqRLM23JJKtTkggSYqQCBGg-BCEpd3nxwj2pE", "severity": "DEBUG"}
{"logger": "aleph.logic.documents", "timestamp": "2022-02-25 20:32:54.538296", "message": "Crawl [1]: /datasets/BlueLeaks-extracted/icefishx/.well-known/acme-challenge/Ps3yr1AqRLM23JJKtTkggSYqQCBGg-BCEpd3nxwj2pE -> 8", "severity": "INFO"}
{"logger": "aleph.queues", "timestamp": "2022-02-25 20:32:54.560787", "message": "Ingest entity [9.b00101715e8f0224ae571567ed92784c7658539c]: ltxAhEpDBfXe4xh_quYDAHsI3wGwl5sGDU4FhUzCDK4", "severity": "DEBUG"}
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
