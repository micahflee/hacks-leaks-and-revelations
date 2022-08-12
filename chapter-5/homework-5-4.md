# Homework 5-4: Play With a VPS

You can use whatever cloud provider you'd like. In this example I'm using [DigitalOcean](https://www.digitalocean.com/).

I've created an SSH key on my computer and uploaded the public key to my DigitalOcean account. Logging into the DigitalOcean console, I created a new VPS with these settings:

- Operating system: Ubuntu
- Plan: 1GB memory, 1 Intel CPU, 25GB disk space, 1000GB bandwidth ($6/month)
- Data center: Singapore
- Authentication: I chose the SSH key for my computer
- Hostname: `hacksleaksrev-example`

When DigitalOcean is done provisioning my VPS, it tells me the IP address is `159.223.86.215`.

## SSH into the server

Because I'm using DigitalOcean, I will SSH using the root user like this:

```sh
ssh root@159.223.86.215
```

Example:

```
micah@rogue:~$ ssh root@159.223.86.215
The authenticity of host '159.223.86.215 (159.223.86.215)' can't be established.
ECDSA key fingerprint is SHA256:i8pKXiZKoy8O1/GKVa5H05SIQ4sSGPWo6IDAJ6pIEmI.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '159.223.86.215' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-97-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Feb 24 21:36:30 UTC 2022

  System load:  0.53              Users logged in:       0
  Usage of /:   6.1% of 24.06GB   IPv4 address for eth0: 159.223.86.215
  Memory usage: 19%               IPv4 address for eth0: 10.15.0.5
  Swap usage:   0%                IPv4 address for eth1: 10.104.0.2
  Processes:    108

1 update can be applied immediately.
To see these additional updates run: apt list --upgradable



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@hacksleaksrev-example:~# 
```

## Start a Byobu session

```sh
byobu
```

Example:

![Screenshot of Byoby session](./homework-5-5-vps-byobu.png)

## Install updates

I don't need to use `sudo` because I'm logged in directly as the root user.

```sh
apt update
apt upgrade
```

Example:

```
root@hacksleaksrev-example:~# apt update
Hit:1 http://mirrors.digitalocean.com/ubuntu focal InRelease
Hit:2 https://repos-droplet.digitalocean.com/apt/droplet-agent main InRelease                    
Get:3 http://mirrors.digitalocean.com/ubuntu focal-updates InRelease [114 kB]                    
Get:4 http://mirrors.digitalocean.com/ubuntu focal-backports InRelease [108 kB]       
Get:5 http://mirrors.digitalocean.com/ubuntu focal-updates/main amd64 Packages [1600 kB]
Get:6 http://mirrors.digitalocean.com/ubuntu focal-updates/main Translation-en [306 kB]
Get:7 http://mirrors.digitalocean.com/ubuntu focal-updates/main amd64 c-n-f Metadata [14.8 kB]
Get:8 http://mirrors.digitalocean.com/ubuntu focal-updates/restricted amd64 Packages [818 kB]
Get:9 http://mirrors.digitalocean.com/ubuntu focal-updates/restricted Translation-en [116 kB]
Get:10 http://security.ubuntu.com/ubuntu focal-security InRelease [114 kB]
Get:11 http://mirrors.digitalocean.com/ubuntu focal-updates/restricted amd64 c-n-f Metadata [500 B]
Get:12 http://mirrors.digitalocean.com/ubuntu focal-updates/universe amd64 Packages [905 kB]
Get:13 http://mirrors.digitalocean.com/ubuntu focal-updates/universe Translation-en [201 kB]
Get:14 http://mirrors.digitalocean.com/ubuntu focal-updates/universe amd64 c-n-f Metadata [20.1 kB]
Get:15 http://mirrors.digitalocean.com/ubuntu focal-updates/multiverse amd64 Packages [23.7 kB]
Get:16 http://mirrors.digitalocean.com/ubuntu focal-updates/multiverse Translation-en [7312 B]
Get:17 http://mirrors.digitalocean.com/ubuntu focal-updates/multiverse amd64 c-n-f Metadata [580 B]
Get:18 http://mirrors.digitalocean.com/ubuntu focal-backports/universe amd64 Packages [22.0 kB]
Get:19 http://mirrors.digitalocean.com/ubuntu focal-backports/universe Translation-en [15.2 kB]
Get:20 http://mirrors.digitalocean.com/ubuntu focal-backports/universe amd64 c-n-f Metadata [728 B]
Get:21 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [1265 kB]
Get:22 http://security.ubuntu.com/ubuntu focal-security/main Translation-en [221 kB]
Get:23 http://security.ubuntu.com/ubuntu focal-security/main amd64 c-n-f Metadata [9624 B]
Get:24 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [764 kB]
Get:25 http://security.ubuntu.com/ubuntu focal-security/restricted Translation-en [109 kB]
Get:26 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 c-n-f Metadata [504 B]
Get:27 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [679 kB]
Get:28 http://security.ubuntu.com/ubuntu focal-security/universe Translation-en [116 kB]
Get:29 http://security.ubuntu.com/ubuntu focal-security/universe amd64 c-n-f Metadata [13.1 kB]
Get:30 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 Packages [20.7 kB]
Get:31 http://security.ubuntu.com/ubuntu focal-security/multiverse Translation-en [5196 B]
Get:32 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 c-n-f Metadata [500 B]
Fetched 7592 kB in 3s (2641 kB/s)                
Reading package lists... Done
Building dependency tree       
Reading state information... Done
46 packages can be upgraded. Run 'apt list --upgradable' to see them.
root@hacksleaksrev-example:~# apt upgrade
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
The following NEW packages will be installed:
  linux-headers-5.4.0-100 linux-headers-5.4.0-100-generic linux-image-5.4.0-100-generic linux-modules-5.4.0-100-generic
The following packages will be upgraded:
  base-files bsdutils cryptsetup cryptsetup-bin cryptsetup-initramfs cryptsetup-run fdisk initramfs-tools initramfs-tools-bin initramfs-tools-core libarchive13
  libblkid1 libcryptsetup12 libdrm-common libdrm2 libexpat1 libfdisk1 libmount1 libsasl2-2 libsasl2-modules libsasl2-modules-db libsmartcols1 libuuid1
  linux-headers-generic linux-headers-virtual linux-image-virtual linux-virtual motd-news-config mount open-vm-tools python-apt-common python3-apt python3-distupgrade
  python3-update-manager snapd sosreport ubuntu-advantage-tools ubuntu-release-upgrader-core update-manager-core util-linux uuid-runtime vim vim-common vim-runtime
  vim-tiny xxd
46 upgraded, 4 newly installed, 0 to remove and 0 not upgraded.
30 standard security updates
Need to get 85.1 MB of archives.
After this operation, 192 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirrors.digitalocean.com/ubuntu focal-updates/main amd64 motd-news-config all 11ubuntu5.5 [4472 B]                     
Get:2 http://mirrors.digitalocean.com/ubuntu focal-updates/main amd64 base-files amd64 11ubuntu5.5 [60.5 kB]                      
Get:3 http://mirrors.digitalocean.com/ubuntu focal-updates/main amd64 bsdutils amd64 1:2.34-0.1ubuntu9.3 [63.0 kB]
Get:4 http://mirrors.digitalocean.com/ubuntu focal-updates/main amd64 libblkid1 amd64 2.34-0.1ubuntu9.3 [136 kB]       
Get:5 http://mirrors.digitalocean.com/ubuntu focal-updates/main amd64 libuuid1 amd64 2.34-0.1ubuntu9.3 [19.9 kB]         
--snip--
```

## Practice

Check what my IP address is using curl:

```sh
curl https://ifconfig.co
```

Example:

```
root@hacksleaksrev-example:~# curl https://ifconfig.co
159.223.86.215
```

Look at what files are in the root directory:

```sh
ls -l /
```

Example:

```
root@hacksleaksrev-example:~# ls -l /
total 64
lrwxrwxrwx   1 root root     7 Jan 31 22:26 bin -> usr/bin
drwxr-xr-x   4 root root  4096 Feb 24 21:41 boot
drwxr-xr-x  17 root root  3800 Feb 24 21:35 dev
drwxr-xr-x  94 root root  4096 Feb 24 21:40 etc
drwxr-xr-x   2 root root  4096 Apr 15  2020 home
lrwxrwxrwx   1 root root     7 Jan 31 22:26 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Jan 31 22:26 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 Jan 31 22:26 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 Jan 31 22:26 libx32 -> usr/libx32
drwx------   2 root root 16384 Jan 31 22:29 lost+found
drwxr-xr-x   2 root root  4096 Jan 31 22:26 media
drwxr-xr-x   2 root root  4096 Jan 31 22:26 mnt
drwxr-xr-x   3 root root  4096 Feb 24 21:35 opt
dr-xr-xr-x 158 root root     0 Feb 24 21:35 proc
drwx------   6 root root  4096 Feb 24 21:37 root
drwxr-xr-x  27 root root   860 Feb 24 21:41 run
lrwxrwxrwx   1 root root     8 Jan 31 22:26 sbin -> usr/sbin
drwxr-xr-x   6 root root  4096 Jan 31 22:28 snap
drwxr-xr-x   2 root root  4096 Jan 31 22:26 srv
dr-xr-xr-x  13 root root     0 Feb 24 21:35 sys
drwxrwxrwt  12 root root  4096 Feb 24 21:41 tmp
drwxr-xr-x  14 root root  4096 Feb 24 21:40 usr
drwxr-xr-x  13 root root  4096 Jan 31 22:28 var
```

Install `transmission-cli`:

```sh
root@hacksleaksrev-example:~# apt search transmission-cli
Sorting... Done
Full Text Search... Done
libtransmission-client-perl/focal 0.0806-1 all
  Perl interface to Transmission

transmission-cli/focal 2.94-2ubuntu3 amd64
  lightweight BitTorrent client (command line programs)

transmission-daemon/focal 2.94-2ubuntu3 amd64
  lightweight BitTorrent client (daemon)

root@hacksleaksrev-example:~# apt install transmission-cli
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libminiupnpc17 libnatpmp1 transmission-common
Suggested packages:
  minissdpd natpmpc transmission-daemon transmission-gtk
The following NEW packages will be installed:
  libminiupnpc17 libnatpmp1 transmission-cli transmission-common
0 upgraded, 4 newly installed, 0 to remove and 0 not upgraded.
Need to get 679 kB of archives.
After this operation, 3683 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirrors.digitalocean.com/ubuntu focal/main amd64 libminiupnpc17 amd64 2.1.20190824-0ubuntu2 [25.8 kB]
Get:2 http://mirrors.digitalocean.com/ubuntu focal/main amd64 libnatpmp1 amd64 20150609-7build1 [7724 B]
Get:3 http://mirrors.digitalocean.com/ubuntu focal/main amd64 transmission-common all 2.94-2ubuntu3 [237 kB]
Get:4 http://mirrors.digitalocean.com/ubuntu focal/universe amd64 transmission-cli amd64 2.94-2ubuntu3 [408 kB]
Fetched 679 kB in 0s (8782 kB/s)      
Selecting previously unselected package libminiupnpc17:amd64.
(Reading database ... 94675 files and directories currently installed.)
Preparing to unpack .../libminiupnpc17_2.1.20190824-0ubuntu2_amd64.deb ...
Unpacking libminiupnpc17:amd64 (2.1.20190824-0ubuntu2) ...
Selecting previously unselected package libnatpmp1:amd64.
Preparing to unpack .../libnatpmp1_20150609-7build1_amd64.deb ...
Unpacking libnatpmp1:amd64 (20150609-7build1) ...
Selecting previously unselected package transmission-common.
Preparing to unpack .../transmission-common_2.94-2ubuntu3_all.deb ...
Unpacking transmission-common (2.94-2ubuntu3) ...
Selecting previously unselected package transmission-cli.
Preparing to unpack .../transmission-cli_2.94-2ubuntu3_amd64.deb ...
Unpacking transmission-cli (2.94-2ubuntu3) ...
Setting up libnatpmp1:amd64 (20150609-7build1) ...
Setting up libminiupnpc17:amd64 (2.1.20190824-0ubuntu2) ...
Setting up transmission-common (2.94-2ubuntu3) ...
Setting up transmission-cli (2.94-2ubuntu3) ...
Processing triggers for man-db (2.9.1-1) ...
Processing triggers for libc-bin (2.31-0ubuntu9.2) ...
root@hacksleaksrev-example:~# 
```

## Download the public OathKeepers dataset

Check out the [Oath Keepers dataset](https://ddosecrets.com/wiki/Oath_Keepers) on the DDoSecrets website. Part of this dataset is private, but part of it is available to the public. Anyone can download 5 gigabyte torrent of emails and chat logs.

See how to use `transmission-cli`:

```sh
transmission-cli --help
```

Example:

```
root@hacksleaksrev-example:~# transmission-cli --help
transmission-cli 2.94 (d8e60ee44f)
A fast and easy BitTorrent client

Usage: transmission-cli [options] <file|url|magnet>

Options:
 -h  --help                          Display this help page and exit
 -b  --blocklist                     Enable peer blocklists
 -B  --no-blocklist                  Disable peer blocklists
 -d  --downlimit            <speed>  Set max download speed in kB/s
 -D  --no-downlimit                  Don't limit the download speed
 -er --encryption-required           Encrypt all peer connections
 -ep --encryption-preferred          Prefer encrypted peer connections
 -et --encryption-tolerated          Prefer unencrypted peer connections
 -f  --finish               <script> Run a script when the torrent finishes
 -g  --config-dir           <path>   Where to find configuration files
 -m  --portmap                       Enable portmapping via NAT-PMP or UPnP
 -M  --no-portmap                    Disable portmapping
 -p  --port                 <port>   Port for incoming peers (Default: 51413)
 -t  --tos                  <tos>    Peer socket TOS (0 to 255,
                                     default=default)
 -u  --uplimit              <speed>  Set max upload speed in kB/s
 -U  --no-uplimit                    Don't limit the upload speed
 -v  --verify                        Verify the specified torrent
 -V  --version                       Show version number and exit
 -w  --download-dir         <path>   Where to save downloaded data
```

Download the torrent file:

```sh
wget https://ddosecrets.com/images/0/02/Oath_Keepers.torrent
```

Example:

```
root@hacksleaksrev-example:~# wget https://ddosecrets.com/images/0/02/Oath_Keepers.torrent
--2022-02-24 21:57:23--  https://ddosecrets.com/images/0/02/Oath_Keepers.torrent
Resolving ddosecrets.com (ddosecrets.com)... 104.26.3.199, 104.26.2.199, 172.67.75.15, ...
Connecting to ddosecrets.com (ddosecrets.com)|104.26.3.199|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 45109 (44K) [application/x-bittorrent]
Saving to: ‘Oath_Keepers.torrent’

Oath_Keepers.torrent                      100%[=====================================================================================>]  44.05K  --.-KB/s    in 0s      

2022-02-24 21:57:24 (148 MB/s) - ‘Oath_Keepers.torrent’ saved [45109/45109]
```

Make sure it's downloaded with `ls`:

```sh
ls -lh
```

Example:

```
root@hacksleaksrev-example:~# ls -lh
total 52K
-rw-r--r-- 1 root root  45K Sep 26 20:00 Oath_Keepers.torrent
drwx------ 3 root root 4.0K Feb 24 21:35 snap
root@hacksleaksrev-example:~# 
```

Download the torrent to the current folder:

```sh
transmission-cli --download-dir . Oath_Keepers.torrent
```

Example:

![Downloading the Oath Keepers dataset](./homework-5-5-transmission.png)

When it's done, you can press CTRL-C to stop seeding.

Now check out the files:

```sh
ls -lh
```

Example:

```
root@hacksleaksrev-example:~# ls -lh
total 56K
drwxr-xr-x 3 root root 4.0K Feb 24 22:03 'Oath Keepers'
-rw-r--r-- 1 root root  45K Sep 26 20:00  Oath_Keepers.torrent
drwx------ 3 root root 4.0K Feb 24 21:35  snap
```

## Explore the Oath Keepers dataset

```sh
cd Oath\ Keepers/
ls -l
cd Oath\ Keepers.sbd/
ls -l
```

Example:

```
root@hacksleaksrev-example:~# cd Oath\ Keepers/
root@hacksleaksrev-example:~/Oath Keepers# ls -l
total 13196
drwxr-xr-x 2 root root     4096 Feb 24 22:03 'Oath Keepers.sbd'
-rw-r--r-- 1 root root 12109624 Feb 24 22:03  messages.json
-rw-r--r-- 1 root root  1393296 Feb 24 22:00  messages_old.json
root@hacksleaksrev-example:~/Oath Keepers# cd Oath\ Keepers.sbd/
root@hacksleaksrev-example:~/Oath Keepers/Oath Keepers.sbd# ls -l
total 4007288
-rw-r--r-- 1 root root    2288916 Feb 24 22:00  Archive
-rw-r--r-- 1 root root      23192 Feb 24 22:00 'Saved Correspondence'
-rw-r--r-- 1 root root      25382 Feb 24 22:00  Systems
-rw-r--r-- 1 root root    2921276 Feb 24 22:00  ak
-rw-r--r-- 1 root root   41772536 Feb 24 22:03  al
-rw-r--r-- 1 root root     289734 Feb 24 22:00  alb
-rw-r--r-- 1 root root   14085257 Feb 24 22:03  ar
-rw-r--r-- 1 root root   32170455 Feb 24 22:03  az
-rw-r--r-- 1 root root   24744491 Feb 24 22:03  ca
-rw-r--r-- 1 root root      13843 Feb 24 22:00  carter
-rw-r--r-- 1 root root  115954560 Feb 24 22:03  co
-rw-r--r-- 1 root root  623043702 Feb 24 22:03  contact
-rw-r--r-- 1 root root      73792 Feb 24 22:00  copyright-claims
-rw-r--r-- 1 root root   38752256 Feb 24 22:03  ct
-rw-r--r-- 1 root root    8491030 Feb 24 22:03  de
-rw-r--r-- 1 root root        205 Feb 24 22:00  dead.letter
-rw-r--r-- 1 root root        183 Feb 24 22:00  dead.letter335
-rw-r--r-- 1 root root   37377548 Feb 24 22:03  disaster-volunteers
-rw-r--r-- 1 root root      21384 Feb 24 22:00  disgruntled
-rw-r--r-- 1 root root      36175 Feb 24 22:00  drafts
-rw-r--r-- 1 root root      10414 Feb 24 22:00  drafts52
-rw-r--r-- 1 root root   40379291 Feb 24 22:03  fl
-rw-r--r-- 1 root root    2311439 Feb 24 22:01  ga
-rw-r--r-- 1 root root   11659879 Feb 24 22:03  hi
-rw-r--r-- 1 root root   16957793 Feb 24 22:03  ia
-rw-r--r-- 1 root root   14816645 Feb 24 22:03  id
-rw-r--r-- 1 root root   15011418 Feb 24 22:03  il
-rw-r--r-- 1 root root   14396497 Feb 24 22:03  in
-rw-r--r-- 1 root root   50026543 Feb 24 22:03  info
-rw-r--r-- 1 root root    4411665 Feb 24 22:03  jeo
-rw-r--r-- 1 root root       4549 Feb 24 22:00  josey-fold
-rw-r--r-- 1 root root  103773969 Feb 24 22:03  jpj
-rw-r--r-- 1 root root   14964856 Feb 24 22:03  ks
-rw-r--r-- 1 root root   18960528 Feb 24 22:03  ky
-rw-r--r-- 1 root root   29680448 Feb 24 22:03  la
-rw-r--r-- 1 root root       4146 Feb 24 22:00  leo
-rw-r--r-- 1 root root   36757744 Feb 24 22:03  ma
-rw-r--r-- 1 root root    8023610 Feb 24 22:03  mail
-rw-r--r-- 1 root root      24171 Feb 24 22:01  mbox
-rw-r--r-- 1 root root   18217954 Feb 24 22:03  md
-rw-r--r-- 1 root root   15951044 Feb 24 22:03  me
-rw-r--r-- 1 root root   82673679 Feb 24 22:03  media
-rw-r--r-- 1 root root     103319 Feb 24 22:00  membership
-rw-r--r-- 1 root root  106632496 Feb 24 22:03  mi
-rw-r--r-- 1 root root   12642968 Feb 24 22:02  mn
-rw-r--r-- 1 root root    3281433 Feb 24 22:03  mo
-rw-r--r-- 1 root root   13102162 Feb 24 22:02  ms
-rw-r--r-- 1 root root   14178472 Feb 24 22:03  mt
-rw-r--r-- 1 root root   22228676 Feb 24 22:03  nc
-rw-r--r-- 1 root root   17401414 Feb 24 22:03  nd
-rw-r--r-- 1 root root    4942433 Feb 24 22:03  ne
-rw-r--r-- 1 root root   14647692 Feb 24 22:03  nh
-rw-r--r-- 1 root root  105287358 Feb 24 22:03  nj
-rw-r--r-- 1 root root   10978031 Feb 24 22:02  nm
-rw-r--r-- 1 root root    3723754 Feb 24 22:02  nv
-rw-r--r-- 1 root root  106080393 Feb 24 22:03  ny
-rw-r--r-- 1 root root    9730438 Feb 24 22:03  oh
-rw-r--r-- 1 root root  115396725 Feb 24 22:03  ok
-rw-r--r-- 1 root root 1415118552 Feb 24 22:03  oksupport
-rw-r--r-- 1 root root  101908002 Feb 24 22:03  or
-rw-r--r-- 1 root root   16482905 Feb 24 22:03  pa
-rw-r--r-- 1 root root     268699 Feb 24 22:01  picrights.com
-rw-r--r-- 1 root root    2586635 Feb 24 22:01  press
-rw-r--r-- 1 root root    2981244 Feb 24 22:00  rallypay
-rw-r--r-- 1 root root      22118 Feb 24 22:00 'read and returned'
-rw-r--r-- 1 root root      11956 Feb 24 22:00  refund
-rw-r--r-- 1 root root   16212454 Feb 24 22:03  ri
-rw-r--r-- 1 root root   66766724 Feb 24 22:03  root
-rw-r--r-- 1 root root    9377453 Feb 24 22:02  sc
-rw-r--r-- 1 root root   12827808 Feb 24 22:03  sd
-rw-r--r-- 1 root root       3084 Feb 24 22:00  sent
-rw-r--r-- 1 root root       3008 Feb 24 22:00  sent858
-rw-r--r-- 1 root root       1137 Feb 24 22:00  sentmail
-rw-r--r-- 1 root root      13024 Feb 24 22:00  sentmail197
-rw-r--r-- 1 root root   19648783 Feb 24 22:03  sentmail34
-rw-r--r-- 1 root root       8541 Feb 24 22:00  sentmail458
-rw-r--r-- 1 root root    3299530 Feb 24 22:00  sentmail490
-rw-r--r-- 1 root root      24557 Feb 24 22:00  sentmail497
-rw-r--r-- 1 root root        634 Feb 24 22:00  sentmail587
-rw-r--r-- 1 root root    2340634 Feb 24 22:03  sentmail648
-rw-r--r-- 1 root root     148897 Feb 24 22:00  sentmail651
-rw-r--r-- 1 root root       2878 Feb 24 22:00  sentmail654
-rw-r--r-- 1 root root       5017 Feb 24 22:00  sentmail687
-rw-r--r-- 1 root root        830 Feb 24 22:00  sentmail738
-rw-r--r-- 1 root root       7234 Feb 24 22:00  sentmail833
-rw-r--r-- 1 root root   18238836 Feb 24 22:03  sentmail881
-rw-r--r-- 1 root root       3878 Feb 24 22:00  sentmail936
-rw-r--r-- 1 root root       9254 Feb 24 22:00  sentmail95
-rw-r--r-- 1 root root    3397050 Feb 24 22:01  stewart.rhodes
-rw-r--r-- 1 root root   13490089 Feb 24 22:03  tn
-rw-r--r-- 1 root root  256892355 Feb 24 22:03  trash961
-rw-r--r-- 1 root root   13959440 Feb 24 22:03  tx
-rw-r--r-- 1 root root    3842408 Feb 24 22:00  ut
-rw-r--r-- 1 root root    2407419 Feb 24 22:03  va
-rw-r--r-- 1 root root    1755509 Feb 24 22:00  volunteers
-rw-r--r-- 1 root root   42023374 Feb 24 22:03  vt
-rw-r--r-- 1 root root   44739864 Feb 24 22:03  wa
-rw-r--r-- 1 root root   12250886 Feb 24 22:02  wi
-rw-r--r-- 1 root root   13201098 Feb 24 22:03  wv
-rw-r--r-- 1 root root    5481775 Feb 24 22:03  wy
root@hacksleaksrev-example:~/Oath Keepers/Oath Keepers.sbd# 
```

## Delete the VPS

When you're done using it, remember to delete your VPS so you won't be charged more for it.
