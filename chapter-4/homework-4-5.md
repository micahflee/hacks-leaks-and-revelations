# Homework 4-5: Exploring the Oath Keepers Dataset Remotely

## Use BitTorrent From the CLI

```sh
apt install transmission-cli
```

Example:

```
root@test-vps:~# apt install transmission-cli
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libevent-2.1-7 libminiupnpc17 libnatpmp1 transmission-common
Suggested packages:
  minissdpd natpmpc transmission-daemon transmission-gtk
The following NEW packages will be installed:
  libevent-2.1-7 libminiupnpc17 libnatpmp1 transmission-cli transmission-common
0 upgraded, 5 newly installed, 0 to remove and 2 not upgraded.
Need to get 711 kB of archives.
After this operation, 2297 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirrors.digitalocean.com/ubuntu jammy/main amd64 libevent-2.1-7 amd64 2.1.12-stable-1build3 [148 kB]
Get:2 http://mirrors.digitalocean.com/ubuntu jammy/main amd64 libminiupnpc17 amd64 2.2.3-1build1 [27.7 kB]
Get:3 http://mirrors.digitalocean.com/ubuntu jammy/main amd64 libnatpmp1 amd64 20150609-7.1build2 [7716 B]
Get:4 http://mirrors.digitalocean.com/ubuntu jammy/main amd64 transmission-common all 3.00-2ubuntu2 [206 kB]
--snip--
```

Create a folder for datasets:

```sh
mkdir ~/datasets
cd ~/datasets
```

Download the Oath Keepers dataset:

```sh
wget https://ddosecrets.com/images/0/02/Oath_Keepers.torrent
transmission-cli -w . Oath_Keepers.torrent
```

For example:

```
root@test-vps:~/datasets# wget https://ddosecrets.com/images/0/02/Oath_Keepers.torrent
--2022-08-13 00:27:41--  https://ddosecrets.com/images/0/02/Oath_Keepers.torrent
Resolving ddosecrets.com (ddosecrets.com)... 104.26.2.199, 104.26.3.199, 172.67.75.15, ...
Connecting to ddosecrets.com (ddosecrets.com)|104.26.2.199|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 45109 (44K) [application/x-bittorrent]
Saving to: ‘Oath_Keepers.torrent’

Oath_Keepers.torrent    100%[===========================================>]  44.05K  --.-KB/s    in 0s

2022-08-13 00:27:42 (180 MB/s) - ‘Oath_Keepers.torrent’ saved [45109/45109]

root@test-vps:~/datasets# transmission-cli -w . Oath_Keepers.torrent
transmission-cli 3.00 (bb6b5a062e)
[2022-08-13 00:27:46.525] Transmission 3.00 (bb6b5a062e) started
[2022-08-13 00:27:46.526] RPC Server: Adding address to whitelist: 127.0.0.1
[2022-08-13 00:27:46.526] RPC Server: Adding address to whitelist: ::1
--snip--
Progress: 4.5%, dl from 7 of 8 peers (7.44 MB/s), ul to 0 (0 kB/s) [0.00]      
```

Press CTRL-C when the download is finished.

## Explore the Dataset

```sh
# Change to the Oath Keepers folder
cd Oath\ Keepers/
# Measure disk space
du -sh --apparent-size .
# List files
ls -lh
# Change folder
cd Oath\ Keepers.sbd/
# List more files
ls -lh
```

Example:

```
root@test-vps:~/datasets# cd Oath\ Keepers/
root@test-vps:~/datasets/Oath Keepers# du -sh --apparent-size .
3.9G	.
root@test-vps:~/datasets/Oath Keepers# ls -lh
total 13M
drwxr-xr-x 2 root root 4.0K Aug 13 00:31 'Oath Keepers.sbd'
-rw-r--r-- 1 root root  12M Aug 13 00:31  messages.json
-rw-r--r-- 1 root root 1.4M Aug 13 00:28  messages_old.json
root@test-vps:~/datasets/Oath Keepers# cd Oath\ Keepers.sbd/
root@test-vps:~/datasets/Oath Keepers/Oath Keepers.sbd# ls -lh
total 3.9G
-rw-r--r-- 1 root root 2.2M Aug 13 00:28  Archive
-rw-r--r-- 1 root root  23K Aug 13 00:28 'Saved Correspondence'
-rw-r--r-- 1 root root  25K Aug 13 00:28  Systems
-rw-r--r-- 1 root root 2.8M Aug 13 00:28  ak
-rw-r--r-- 1 root root  40M Aug 13 00:31  al
-rw-r--r-- 1 root root 283K Aug 13 00:28  alb
-rw-r--r-- 1 root root  14M Aug 13 00:31  ar
-rw-r--r-- 1 root root  31M Aug 13 00:31  az
-rw-r--r-- 1 root root  24M Aug 13 00:31  ca
-rw-r--r-- 1 root root  14K Aug 13 00:28  carter
-rw-r--r-- 1 root root 111M Aug 13 00:31  co
-rw-r--r-- 1 root root 595M Aug 13 00:31  contact
-rw-r--r-- 1 root root  73K Aug 13 00:28  copyright-claims
-rw-r--r-- 1 root root  37M Aug 13 00:31  ct
-rw-r--r-- 1 root root 8.1M Aug 13 00:30  de
-rw-r--r-- 1 root root  205 Aug 13 00:28  dead.letter
-rw-r--r-- 1 root root  183 Aug 13 00:28  dead.letter335
-rw-r--r-- 1 root root  36M Aug 13 00:31  disaster-volunteers
-rw-r--r-- 1 root root  21K Aug 13 00:28  disgruntled
-rw-r--r-- 1 root root  36K Aug 13 00:28  drafts
-rw-r--r-- 1 root root  11K Aug 13 00:28  drafts52
-rw-r--r-- 1 root root  39M Aug 13 00:31  fl
-rw-r--r-- 1 root root 2.3M Aug 13 00:28  ga
-rw-r--r-- 1 root root  12M Aug 13 00:31  hi
-rw-r--r-- 1 root root  17M Aug 13 00:31  ia
-rw-r--r-- 1 root root  15M Aug 13 00:31  id
-rw-r--r-- 1 root root  15M Aug 13 00:31  il
-rw-r--r-- 1 root root  14M Aug 13 00:31  in
-rw-r--r-- 1 root root  48M Aug 13 00:31  info
-rw-r--r-- 1 root root 4.3M Aug 13 00:30  jeo
-rw-r--r-- 1 root root 4.5K Aug 13 00:28  josey-fold
-rw-r--r-- 1 root root  99M Aug 13 00:31  jpj
-rw-r--r-- 1 root root  15M Aug 13 00:31  ks
-rw-r--r-- 1 root root  19M Aug 13 00:31  ky
-rw-r--r-- 1 root root  29M Aug 13 00:31  la
-rw-r--r-- 1 root root 4.1K Aug 13 00:28  leo
-rw-r--r-- 1 root root  36M Aug 13 00:31  ma
-rw-r--r-- 1 root root 7.7M Aug 13 00:30  mail
-rw-r--r-- 1 root root  24K Aug 13 00:28  mbox
-rw-r--r-- 1 root root  18M Aug 13 00:31  md
-rw-r--r-- 1 root root  16M Aug 13 00:31  me
-rw-r--r-- 1 root root  79M Aug 13 00:31  media
-rw-r--r-- 1 root root 101K Aug 13 00:28  membership
-rw-r--r-- 1 root root 102M Aug 13 00:31  mi
-rw-r--r-- 1 root root  13M Aug 13 00:31  mn
-rw-r--r-- 1 root root 3.2M Aug 13 00:29  mo
-rw-r--r-- 1 root root  13M Aug 13 00:31  ms
-rw-r--r-- 1 root root  14M Aug 13 00:31  mt
-rw-r--r-- 1 root root  22M Aug 13 00:31  nc
-rw-r--r-- 1 root root  17M Aug 13 00:30  nd
-rw-r--r-- 1 root root 4.8M Aug 13 00:31  ne
-rw-r--r-- 1 root root  14M Aug 13 00:30  nh
-rw-r--r-- 1 root root 101M Aug 13 00:31  nj
-rw-r--r-- 1 root root  11M Aug 13 00:31  nm
-rw-r--r-- 1 root root 3.6M Aug 13 00:29  nv
-rw-r--r-- 1 root root 102M Aug 13 00:31  ny
-rw-r--r-- 1 root root 9.3M Aug 13 00:31  oh
-rw-r--r-- 1 root root 111M Aug 13 00:31  ok
-rw-r--r-- 1 root root 1.4G Aug 13 00:31  oksupport
-rw-r--r-- 1 root root  98M Aug 13 00:31  or
-rw-r--r-- 1 root root  16M Aug 13 00:31  pa
-rw-r--r-- 1 root root 263K Aug 13 00:28  picrights.com
-rw-r--r-- 1 root root 2.5M Aug 13 00:28  press
-rw-r--r-- 1 root root 2.9M Aug 13 00:28  rallypay
-rw-r--r-- 1 root root  22K Aug 13 00:28 'read and returned'
-rw-r--r-- 1 root root  12K Aug 13 00:28  refund
-rw-r--r-- 1 root root  16M Aug 13 00:30  ri
-rw-r--r-- 1 root root  64M Aug 13 00:31  root
-rw-r--r-- 1 root root 9.0M Aug 13 00:30  sc
-rw-r--r-- 1 root root  13M Aug 13 00:31  sd
-rw-r--r-- 1 root root 3.1K Aug 13 00:28  sent
-rw-r--r-- 1 root root 3.0K Aug 13 00:28  sent858
-rw-r--r-- 1 root root 1.2K Aug 13 00:28  sentmail
-rw-r--r-- 1 root root  13K Aug 13 00:28  sentmail197
-rw-r--r-- 1 root root  19M Aug 13 00:31  sentmail34
-rw-r--r-- 1 root root 8.4K Aug 13 00:28  sentmail458
-rw-r--r-- 1 root root 3.2M Aug 13 00:28  sentmail490
-rw-r--r-- 1 root root  24K Aug 13 00:28  sentmail497
-rw-r--r-- 1 root root  634 Aug 13 00:28  sentmail587
-rw-r--r-- 1 root root 2.3M Aug 13 00:30  sentmail648
-rw-r--r-- 1 root root 146K Aug 13 00:28  sentmail651
-rw-r--r-- 1 root root 2.9K Aug 13 00:28  sentmail654
-rw-r--r-- 1 root root 4.9K Aug 13 00:28  sentmail687
-rw-r--r-- 1 root root  830 Aug 13 00:28  sentmail738
-rw-r--r-- 1 root root 7.1K Aug 13 00:28  sentmail833
-rw-r--r-- 1 root root  18M Aug 13 00:31  sentmail881
-rw-r--r-- 1 root root 3.8K Aug 13 00:28  sentmail936
-rw-r--r-- 1 root root 9.1K Aug 13 00:28  sentmail95
-rw-r--r-- 1 root root 3.3M Aug 13 00:30  stewart.rhodes
-rw-r--r-- 1 root root  13M Aug 13 00:30  tn
-rw-r--r-- 1 root root 245M Aug 13 00:31  trash961
-rw-r--r-- 1 root root  14M Aug 13 00:31  tx
-rw-r--r-- 1 root root 3.7M Aug 13 00:28  ut
-rw-r--r-- 1 root root 2.3M Aug 13 00:31  va
-rw-r--r-- 1 root root 1.7M Aug 13 00:28  volunteers
-rw-r--r-- 1 root root  41M Aug 13 00:31  vt
-rw-r--r-- 1 root root  43M Aug 13 00:31  wa
-rw-r--r-- 1 root root  12M Aug 13 00:30  wi
-rw-r--r-- 1 root root  13M Aug 13 00:30  wv
-rw-r--r-- 1 root root 5.3M Aug 13 00:30  wy
root@test-vps:~/datasets/Oath Keepers/Oath Keepers.sbd# 
```

## Copy Files From Your VPS

Open a terminal on your computer (not SSHed to the remote computer), and install rsync if you don't have it.

Copy the Oath Keepers dataset to your datasets USB disk, like this:

```sh
rsync -av --progress root@178.128.22.151:"~/datasets/Oath\ Keepers" /media/micah/datasets/
```

But change the IP address to be the IP of your VPS, and change the destrination path to be the path of your datasets USB disk.

For example:

```sh
micah@rogue:~$ rsync -av --progress root@178.128.22.151:"~/datasets/Oath\ Keepers" /media/micah/datasets/
receiving incremental file list
Oath Keepers/
Oath Keepers/messages.json
     12,109,624 100%    1.89MB/s    0:00:06 (xfr#1, to-chk=102/104)
Oath Keepers/messages_old.json
      1,393,296 100%    1.65MB/s    0:00:00 (xfr#2, to-chk=101/104)
Oath Keepers/Oath Keepers.sbd/
Oath Keepers/Oath Keepers.sbd/Archive
      2,288,916 100%    1.81MB/s    0:00:01 (xfr#3, to-chk=99/104)
Oath Keepers/Oath Keepers.sbd/Saved Correspondence
         23,192 100%  111.02kB/s    0:00:00 (xfr#4, to-chk=98/104)
Oath Keepers/Oath Keepers.sbd/Systems
         25,382 100%  121.51kB/s    0:00:00 (xfr#5, to-chk=97/104)
Oath Keepers/Oath Keepers.sbd/ak
      2,921,276 100%    4.33MB/s    0:00:00 (xfr#6, to-chk=96/104)
Oath Keepers/Oath Keepers.sbd/al
     41,772,536 100%    6.57MB/s    0:00:06 (xfr#7, to-chk=95/104)
--snip--
```

## Delete Your VPS

When you're done using it, remember to delete your VPS from DigitalOcean so you won't be charged more for it.
