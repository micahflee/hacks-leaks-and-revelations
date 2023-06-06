# Exercise 5-4: Run Aleph Locally in Linux Containers

Make a new folder just for this assignment. Follow the [production deployment instructions](https://docs.alephdata.org/developers/installation#production-deployment) in the [Aleph documentation](https://docs.alephdata.org/).

You can see example files in the [aleph](./aleph/) folder.

If you're using Windows, use a PowerShell terminal.

## Configure Aleph and Start the Containers

In short, you'll need to:

Save a copy of Aleph's [docker-compose.yml](https://github.com/alephdata/aleph/blob/main/docker-compose.yml) and [aleph.env.tmpl](https://github.com/alephdata/aleph/blob/main/aleph.env.tmpl) from Aleph’s git repo into your `aleph` folder. After you do this you should have these two files:

```
micah@trapdoor aleph % ls -l
total 16
-rw-r--r--  1 micah  staff  2931 Feb 10 20:31 aleph.env.tmpl
-rw-r--r--  1 micah  staff  2247 Feb 10 20:31 docker-compose.yml
```

Edit `docker-compose.yml` to delete, or comment out, this line in the `shell` container:

```
- "~:/host"
```

Make a copy of `aleph.env.tmpl` called `aleph.env`. You can do this by running:

```sh
cp aleph.env.tmpl aleph.env
```

Open `aleph.env` in your text editor. Set a random value for `ALEPH_SECRET_KEY`. You can generate this value by running:

```sh
openssl rand -hex 24
```

Example:

```
micah@trapdoor aleph % openssl rand -hex 24
f8b1afa480cec3574750d0d2a0f19b9484ea49d42a58c236
```

![Editing aleph.env](./exercise-5-4-aleph-env.png)

Save the file.

## Allow Elasticsearch to Map Its Own Memory

For Aleph to work properly, you must change the `vm.max_map_count` Linux kernel setting.

If you're using Linux or Windows with WSL, you can do this just by running this command:

```sh
sudo sysctl -w vm.max_map_count=262144
```

If you're using macOS with Docker Desktop, enabling Elasticsearch is more complicated because you actually have to run this command in Docker Desktop's Linux VM rather than on your Mac. Here's how you can run it there:

```sh
docker run -it --rm --privileged --pid=host alpine:edge \
    nsenter -t 1 -m -u -n -i \
    sysctl -w vm.max_map_count=262144
```

Each time you restart Docker Desktop, this change gets undone and you’ll need to run it again if you want your Elasticsearch database to not run out of memory. The file [fix-es-memory.sh](./aleph/fix-es-memory.sh) is a shell script that includes this command, so you can run it before starting Aleph containers like this:

```sh
./fix-es-memory.sh
docker-compose up
```

## Start Aleph

```sh
docker-compose up
```

The first time you run this it will download several gigabytes of Linux container images.

Example:

```
micah@trapdoor aleph % docker-compose up
[+] Running 75/75
 ⠿ redis Pulled                                                            142.9s
   ⠿ 719adce26c52 Pull complete                                            137.0s
   ⠿ b8f35e378c31 Pull complete                                            137.8s
   ⠿ d034517f789c Pull complete                                            138.7s
   ⠿ 3772d4d76753 Pull complete                                            138.8s
   ⠿ 211a7f52febb Pull complete                                            138.9s
 ⠿ postgres Pulled                                                         143.4s
   ⠿ 3e17c6eae66c Pull complete                                            133.3s
   ⠿ edb9dc1cfcb8 Pull complete                                            133.8s
   ⠿ 7a344e5b3663 Pull complete                                            133.8s
   ⠿ d619f9c5def6 Pull complete                                            134.1s
   ⠿ 225b82de1e67 Pull complete                                            134.7s
   ⠿ 10daa23c1d9a Pull complete                                            134.8s
   ⠿ 4ba4a4b2d69b Pull complete                                            134.9s
   ⠿ 3fc3e282a06c Pull complete                                            139.4s
   ⠿ db8508199c1a Pull complete                                            139.5s
   ⠿ 99445470b9b6 Pull complete                                            139.5s
   ⠿ dd01bf2076d4 Pull complete                                            139.6s
   ⠿ 292c6e56e62f Pull complete                                            139.7s
   ⠿ 7a07813393c7 Pull complete                                            139.8s
 ⠿ worker Pulled                                                           129.8s
   ⠿ 8fd1d8c5af6a Pull complete                                            113.0s
   ⠿ bc9b21090f47 Pull complete                                            124.2s
 ⠿ convert-document Pulled                                                 108.9s
   ⠿ ffb17fa303bd Pull complete                                            105.2s
   ⠿ 9d736a7ea3fb Pull complete                                            105.4s
   ⠿ 0a4c5a5bf69b Pull complete                                            105.5s
   ⠿ a48c18e72288 Pull complete                                            105.8s
   ⠿ 5bf07daa5c47 Pull complete                                            106.2s
   ⠿ d43ee58cac0f Pull complete                                            106.4s
   ⠿ 5760a0f555b4 Pull complete                                            106.5s
   ⠿ c8aae845228a Pull complete                                            106.6s
 ⠿ ui Pulled                                                               124.3s
   ⠿ 59bf1c3509f3 Pull complete                                            116.2s
   ⠿ 8d6ba530f648 Pull complete                                            117.2s
   ⠿ 5288d7ad7a7f Pull complete                                            117.3s
   ⠿ 39e51c61c033 Pull complete                                            117.4s
   ⠿ ee6f71c6f4a8 Pull complete                                            117.6s
   ⠿ f2303c6c8865 Pull complete                                            117.7s
   ⠿ 8357a4ef2c90 Pull complete                                            118.6s
   ⠿ f1d450f2a23c Pull complete                                            121.1s
 ⠿ elasticsearch Pulled                                                    175.8s
   ⠿ 7b1a6ab2e44d Pull complete                                             15.0s
   ⠿ f85c3fdbf085 Pull complete                                            120.7s
   ⠿ 0ee9ef16ef16 Pull complete                                            120.8s
   ⠿ 1b555fc21eda Pull complete                                            171.2s
   ⠿ 5195df1d2493 Pull complete                                            171.3s
   ⠿ b22dfd95268f Pull complete                                            171.4s
   ⠿ 762293acfd23 Pull complete                                            171.5s
   ⠿ e7d18a44f390 Pull complete                                            171.5s
   ⠿ 652e33f15f45 Pull complete                                            172.2s
   ⠿ 2d14ac7b460a Pull complete                                            172.2s
   ⠿ c85072c2f18a Pull complete                                            172.3s
 ⠿ api Pulled                                                              129.8s
   ⠿ ea362f368469 Pull complete                                             99.9s
   ⠿ 6f0e9d0b2a15 Pull complete                                            113.7s
   ⠿ 94d0a3aecec3 Pull complete                                            124.6s
   ⠿ 6c069ee7cd8e Pull complete                                            124.7s
 ⠿ shell Pulled                                                            129.8s
   ⠿ c5a7997119f7 Pull complete                                            112.8s
   ⠿ 49a1a2798723 Pull complete                                            113.8s
   ⠿ 138fa9f664f7 Pull complete                                            126.6s
 ⠿ ingest-file Pulled                                                      140.9s
   ⠿ ca3b09ffcfd6 Pull complete                                             74.6s
   ⠿ 44bcf0985803 Pull complete                                             74.7s
   ⠿ dedb4870a65f Pull complete                                             93.2s
   ⠿ 20cfd754b918 Pull complete                                             93.8s
   ⠿ b63b92d355c4 Pull complete                                             93.9s
   ⠿ 259112fa402a Pull complete                                            109.6s
   ⠿ ed84f8a0b122 Pull complete                                            113.7s
   ⠿ 9ee0f4cb3510 Pull complete                                            120.1s
   ⠿ 8332487593cb Pull complete                                            137.1s
   ⠿ 57109e207b44 Pull complete                                            137.6s
   ⠿ 98f8f3825eff Pull complete                                            137.7s
   ⠿ 50fda763c0d6 Pull complete                                            138.4s
[+] Running 10/10
 ⠿ Network exercise-5-4_default               Created                        0.1s
 ⠿ Container exercise-5-4-postgres-1          Created                        0.1s
 ⠿ Container exercise-5-4-convert-document-1  Created                        0.1s
 ⠿ Container exercise-5-4-elasticsearch-1     Created                        0.1s
 ⠿ Container exercise-5-4-redis-1             Created                        0.1s
 ⠿ Container exercise-5-4-ingest-file-1       Created                        0.0s
 ⠿ Container exercise-5-4-worker-1            Created                        0.1s
 ⠿ Container exercise-5-4-api-1               Created                        0.1s
 ⠿ Container exercise-5-4-shell-1             Created                        0.1s
 ⠿ Container exercise-5-4-ui-1                Created                        0.0s
Attaching to exercise-5-4-api-1, exercise-5-4-convert-document-1, exercise-5-4-elasticsearch-1, exercise-5-4-ingest-file-1, exercise-5-4-postgres-1, exercise-5-4-redis-1, exercise-5-4-shell-1, exercise-5-4-ui-1, exercise-5-4-worker-1
exercise-5-4-redis-1             | 1:C 25 Feb 2022 18:12:53.586 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
exercise-5-4-redis-1             | 1:C 25 Feb 2022 18:12:53.587 # Redis version=6.2.6, bits=64, commit=00000000, modified=0, pid=1, just started
exercise-5-4-redis-1             | 1:C 25 Feb 2022 18:12:53.587 # Configuration loaded
exercise-5-4-redis-1             | 1:M 25 Feb 2022 18:12:53.588 * monotonic clock: POSIX clock_gettime
exercise-5-4-redis-1             | 1:M 25 Feb 2022 18:12:53.589 * Running mode=standalone, port=6379.
exercise-5-4-redis-1             | 1:M 25 Feb 2022 18:12:53.589 # Server initialized
exercise-5-4-redis-1             | 1:M 25 Feb 2022 18:12:53.591 * Loading RDB produced by version 6.2.6
exercise-5-4-redis-1             | 1:M 25 Feb 2022 18:12:53.591 * RDB age 196 seconds
exercise-5-4-redis-1             | 1:M 25 Feb 2022 18:12:53.591 * RDB memory usage when created 0.77 Mb
exercise-5-4-redis-1             | 1:M 25 Feb 2022 18:12:53.591 # Done loading RDB, keys loaded: 25, keys expired: 0.
exercise-5-4-redis-1             | 1:M 25 Feb 2022 18:12:53.591 * DB loaded from disk: 0.001 seconds
exercise-5-4-redis-1             | 1:M 25 Feb 2022 18:12:53.591 * Ready to accept connections
exercise-5-4-elasticsearch-1     | create keystore
exercise-5-4-postgres-1          | 2022-02-25 18:12:53.674 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
exercise-5-4-postgres-1          | 2022-02-25 18:12:53.674 UTC [1] LOG:  listening on IPv6 address "::", port 5432
exercise-5-4-postgres-1          | 2022-02-25 18:12:53.676 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
exercise-5-4-convert-document-1  | [2022-02-25 18:12:53 +0000] [1] [INFO] Starting gunicorn 20.1.0
exercise-5-4-convert-document-1  | [2022-02-25 18:12:53 +0000] [1] [INFO] Listening at: http://0.0.0.0:3000 (1)
exercise-5-4-convert-document-1  | [2022-02-25 18:12:53 +0000] [1] [INFO] Using worker: sync
exercise-5-4-convert-document-1  | [2022-02-25 18:12:53 +0000] [10] [INFO] Booting worker with pid: 10
exercise-5-4-postgres-1          | 2022-02-25 18:12:53.693 UTC [29] LOG:  database system was shut down at 2022-02-25 18:09:37 UTC
exercise-5-4-postgres-1          | 2022-02-25 18:12:53.704 UTC [1] LOG:  database system is ready to accept connections
exercise-5-4-convert-document-1  | [2022-02-25 18:12:53 +0000] [11] [INFO] Booting worker with pid: 11
exercise-5-4-convert-document-1  | [2022-02-25 18:12:53 +0000] [12] [INFO] Booting worker with pid: 12
exercise-5-4-convert-document-1  | [2022-02-25 18:12:53 +0000] [13] [INFO] Booting worker with pid: 13
exercise-5-4-elasticsearch-1     | Created elasticsearch keystore in /usr/share/elasticsearch/config/elasticsearch.keystore
exercise-5-4-shell-1 exited with code 0
exercise-5-4-api-1               | [2022-02-25 18:12:56 +0000] [1] [DEBUG] Current configuration:
exercise-5-4-api-1               |   config: ./gunicorn.conf.py
exercise-5-4-api-1               |   wsgi_app: None
exercise-5-4-api-1               |   bind: ['0.0.0.0:8000']
exercise-5-4-api-1               |   backlog: 2048
exercise-5-4-api-1               |   workers: 6
--snip--
```

## "Upgrade" the Aleph Database the First Time

Open a separate terminal window and run:

```sh
docker-compose run --rm shell aleph upgrade
```

Example:

```
micah@trapdoor aleph % docker-compose run --rm shell aleph upgrade
[+] Running 6/0
 ⠿ Container exercise-5-4-elasticsearch-1     Running                      0.0s
 ⠿ Container exercise-5-4-convert-document-1  Running                      0.0s
 ⠿ Container exercise-5-4-redis-1             Running                      0.0s
 ⠿ Container exercise-5-4-postgres-1          Running                      0.0s
 ⠿ Container exercise-5-4-ingest-file-1       Running                      0.0s
 ⠿ Container exercise-5-4-worker-1            Running                      0.0s
{"logger": "alembic.runtime.migration", "timestamp": "2022-02-25 18:38:24.240581", "message": "Context impl PostgresqlImpl.", "severity": "INFO"}
{"logger": "alembic.runtime.migration", "timestamp": "2022-02-25 18:38:24.240763", "message": "Will assume transactional DDL.", "severity": "INFO"}
{"logger": "servicelayer.archive.file", "timestamp": "2022-02-25 18:38:24.265702", "message": "Archive: /data", "severity": "INFO"}
{"logger": "aleph.logic.roles", "timestamp": "2022-02-25 18:38:24.265874", "message": "Creating system roles...", "severity": "INFO"}
/usr/local/lib/python3.8/dist-packages/elasticsearch/connection/base.py:200: ElasticsearchWarning: Elasticsearch built-in security features are not enabled. Without authentication, your cluster could be accessible to anyone. See https://www.elastic.co/guide/en/elasticsearch/reference/7.16/security-minimal-setup.html to enable security.
  warnings.warn(message, category=ElasticsearchWarning)
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:24.440236", "message": "Creating index: aleph-collection-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:25.594232", "message": "Creating index: aleph-notifications-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:26.255927", "message": "Creating index: aleph-entity-airplane-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:26.844667", "message": "Creating index: aleph-entity-person-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:27.567198", "message": "Creating index: aleph-entity-company-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:28.320704", "message": "Creating index: aleph-entity-representation-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:28.944303", "message": "Creating index: aleph-entity-vessel-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:29.612999", "message": "Creating index: aleph-entity-payment-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:30.208057", "message": "Creating index: aleph-entity-unknownlink-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:30.831330", "message": "Creating index: aleph-entity-organization-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:31.623136", "message": "Creating index: aleph-entity-page-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:32.350666", "message": "Creating index: aleph-entity-workbook-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:32.842468", "message": "Creating index: aleph-entity-table-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:33.600293", "message": "Creating index: aleph-entity-sanction-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:34.278753", "message": "Creating index: aleph-entity-hypertext-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:34.907842", "message": "Creating index: aleph-entity-folder-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:35.378273", "message": "Creating index: aleph-entity-plaintext-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:36.136378", "message": "Creating index: aleph-entity-membership-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:36.788913", "message": "Creating index: aleph-entity-mention-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:37.413392", "message": "Creating index: aleph-entity-bankaccount-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:38.087367", "message": "Creating index: aleph-entity-security-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:38.728879", "message": "Creating index: aleph-entity-package-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:39.235386", "message": "Creating index: aleph-entity-project-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:39.943382", "message": "Creating index: aleph-entity-asset-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:40.552525", "message": "Creating index: aleph-entity-documentation-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:41.187900", "message": "Creating index: aleph-entity-directorship-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:41.874500", "message": "Creating index: aleph-entity-passport-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:42.398196", "message": "Creating index: aleph-entity-publicbody-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:43.031384", "message": "Creating index: aleph-entity-taxroll-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:43.777893", "message": "Creating index: aleph-entity-identification-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:44.422236", "message": "Creating index: aleph-entity-event-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:45.072737", "message": "Creating index: aleph-entity-projectparticipant-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:45.764117", "message": "Creating index: aleph-entity-realestate-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:46.473516", "message": "Creating index: aleph-entity-pages-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:47.400724", "message": "Creating index: aleph-entity-ownership-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:48.093833", "message": "Creating index: aleph-entity-legalentity-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:48.838173", "message": "Creating index: aleph-entity-useraccount-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:49.530878", "message": "Creating index: aleph-entity-economicactivity-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:50.208326", "message": "Creating index: aleph-entity-succession-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:50.909530", "message": "Creating index: aleph-entity-family-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:51.457384", "message": "Creating index: aleph-entity-assessment-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:52.282539", "message": "Creating index: aleph-entity-associate-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:52.814251", "message": "Creating index: aleph-entity-address-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:53.507110", "message": "Creating index: aleph-entity-courtcaseparty-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:54.216167", "message": "Creating index: aleph-entity-image-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:55.115904", "message": "Creating index: aleph-entity-cryptowallet-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:55.847871", "message": "Creating index: aleph-entity-message-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:56.614634", "message": "Creating index: aleph-entity-contractaward-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:57.324471", "message": "Creating index: aleph-entity-license-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:58.057576", "message": "Creating index: aleph-entity-call-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:58.804226", "message": "Creating index: aleph-entity-courtcase-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:38:59.491853", "message": "Creating index: aleph-entity-employment-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:39:00.192920", "message": "Creating index: aleph-entity-article-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:39:00.903883", "message": "Creating index: aleph-entity-video-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:39:01.469860", "message": "Creating index: aleph-entity-email-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:39:02.385226", "message": "Creating index: aleph-entity-document-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:39:03.013252", "message": "Creating index: aleph-entity-vehicle-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:39:03.755903", "message": "Creating index: aleph-entity-note-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:39:04.754657", "message": "Creating index: aleph-entity-audio-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:39:05.308807", "message": "Creating index: aleph-entity-debt-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:39:06.009476", "message": "Creating index: aleph-entity-contract-v1...", "severity": "INFO"}
{"logger": "aleph.index.util", "timestamp": "2022-02-25 18:39:06.729421", "message": "Creating index: aleph-xref-v1...", "severity": "INFO"}
```

When this command finishes running, load http://127.0.0.1:8080/ to see your Aleph server.

![Aleph server running](./exercise-5-4-aleph1.png)

## Start an Aleph Shell

```sh
docker-compose run --rm shell bash
```

Example:

```
micah@trapdoor aleph % docker-compose run --rm shell bash
[+] Running 6/0
 ⠿ Container exercise-5-4-redis-1             Running                      0.0s
 ⠿ Container exercise-5-4-convert-document-1  Running                      0.0s
 ⠿ Container exercise-5-4-postgres-1          Running                      0.0s
 ⠿ Container exercise-5-4-elasticsearch-1     Running                      0.0s
 ⠿ Container exercise-5-4-ingest-file-1       Running                      0.0s
 ⠿ Container exercise-5-4-worker-1            Running                      0.0s
root@39093f0cc006:/aleph# aleph --help
Usage: aleph [OPTIONS] COMMAND [ARGS]...

  Server-side command line for aleph.

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  cancel              Cancel all queued tasks for the dataset.
  cancel-user         Cancel all queued tasks not related to a dataset.
  cleanup-archive
  collections         List all collections.
  crawldir            Crawl the given directory.
  createuser          Create a user and show their API key.
  db                  Perform database migrations.
  delete              Delete a given collection.
  deleterole          Hard-delete a role (user, or group) from the database.
  dump-entities       Export FtM entities for the given collection.
  dump-profiles       Export profile entityset items for the given...
  evilshit            EVIL: Delete all data and recreate the database.
  flush               Flush all the contents for a given collection.
  flushdeleted        Remove soft-deleted database objects.
  load-entities       Load FtM entities from the specified iJSON file.
  publish             Make a collection visible to all users.
  reindex             Index all the aggregator contents for a collection.
  reindex-casefiles   Re-index all the casefile collections.
  reindex-full        Re-index all collections.
  reingest            Process documents and database entities and index...
  reingest-casefiles  Re-ingest all the casefile collections.
  resetcache          Clear the redis cache.
  resetindex          Re-create the ES index configuration, dropping all...
  retry-exports       Cancel all queued tasks not related to a dataset.
  routes              Show the routes for the app.
  run                 Run a development server.
  shell               Run a shell in the app context.
  status              Get the queue status (pending and finished tasks.)
  touch               Mark a collection as changed.
  update              Re-index all collections and clear some caches.
  upgrade             Create or upgrade the search index and database.
  worker              Run the queue-based worker service.
  xref                Cross-reference all entities and documents in a...
root@39093f0cc006:/aleph#
```

Run `exit` to quit the Aleph shell, and in your Docker Compose window press CTRL-C to close down all of the Aleph containers.
