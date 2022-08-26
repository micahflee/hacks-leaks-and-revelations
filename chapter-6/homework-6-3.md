# Homework 6-3: Quickly Run a WordPress Site With Docker Compose

You can find the `docker-compose.yaml` file used in this homework [here](./homework-6-3/docker-compose.yaml).

If you're using Windows, use a PowerShell terminal.

## Make a `docker-compose.yaml` File

Make a new homework folder just for this assignment, and copy `docker-compose.yaml` into it.

## Start Your WordPress Site

Change to this folder and bring up the containers:

```sh
docker-compose up
```

Example:

```
micah@trapdoor homework-6-3 % docker-compose up     
Creating network "homework-6-3_default" with the default driver
Pulling db (mysql:5.7)...
5.7: Pulling from library/mysql
9815334b7810: Pull complete
f85cb6fccbfd: Pull complete
b63612353671: Pull complete
447901201612: Pull complete
9b6bc806cc29: Pull complete
24ec1f4b3b0d: Pull complete
207ed1eb2fd4: Pull complete
27cbde3edd97: Pull complete
0a5aa35cc154: Pull complete
e6c92bf6471b: Pull complete
07b80de0d1af: Pull complete
Digest: sha256:c1bda6ecdbc63d3b0d3a3a3ce195de3dd755c4a0658ed782a16a0682216b9a48
Status: Downloaded newer image for mysql:5.7
Pulling wordpress (wordpress:latest)...
latest: Pulling from library/wordpress
7a6db449b51b: Pull complete
ad2afdb99a9d: Pull complete
dbc5aa907229: Pull complete
82f252ab4ad1: Pull complete
bf5b34fc9894: Pull complete
6161651d3d95: Pull complete
cf2adf296ef1: Pull complete
d921da48d554: Pull complete
b18a4562cdb2: Pull complete
c2620408b8f1: Pull complete
7674ea7f8b64: Pull complete
d424de41e878: Pull complete
95dce5dc9f57: Pull complete
4a65afeeb0d9: Pull complete
e3f4c7b3ecca: Pull complete
0f855ed70a9b: Pull complete
8fd46befb58e: Pull complete
b10589319bdf: Pull complete
4df613d34dec: Pull complete
2bf61e4e04d6: Pull complete
268033097d9e: Pull complete
Digest: sha256:5f1873a461105cb1dc1a75731671125f1fb406b18e3fcf63210e8f7f84ce560b
Status: Downloaded newer image for wordpress:latest
Creating homework-6-3_db_1 ... done
Creating homework-6-3_wordpress_1 ... done
Attaching to homework-6-3_db_1, homework-6-3_wordpress_1
db_1         | 2022-08-26 22:39:40+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 5.7.39-1.el7 started.
wordpress_1  | No 'wp-config.php' found in /var/www/html, but 'WORDPRESS_...' variables supplied; copying '/usr/src/wordpress/wp-config-docker.php' (WORDPRESS_DB_HOST WORDPRESS_DB_NAME WORDPRESS_DB_PASSWORD WORDPRESS_DB_USER)
wordpress_1  | AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.20.0.3. Set the 'ServerName' directive globally to suppress this message
wordpress_1  | AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.20.0.3. Set the 'ServerName' directive globally to suppress this message
wordpress_1  | [Fri Aug 26 22:39:43.061940 2022] [mpm_prefork:notice] [pid 1] AH00163: Apache/2.4.54 (Debian) PHP/7.4.30 configured -- resuming normal operations
wordpress_1  | [Fri Aug 26 22:39:43.062049 2022] [core:notice] [pid 1] AH00094: Command line: 'apache2 -D FOREGROUND'
db_1         | 2022-08-26 22:39:43+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
db_1         | 2022-08-26 22:39:43+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 5.7.39-1.el7 started.
db_1         | '/var/lib/mysql/mysql.sock' -> '/var/run/mysqld/mysqld.sock'
db_1         | 2022-08-26T22:39:44.385188Z 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
db_1         | 2022-08-26T22:39:44.392002Z 0 [Note] mysqld (mysqld 5.7.39) starting as process 1 ...
db_1         | 2022-08-26T22:39:44.397524Z 0 [Warning] Setting lower_case_table_names=2 because file system for /var/lib/mysql/ is case insensitive
db_1         | 2022-08-26T22:39:44.399299Z 0 [Note] InnoDB: PUNCH HOLE support available
db_1         | 2022-08-26T22:39:44.399372Z 0 [Note] InnoDB: Mutexes and rw_locks use GCC atomic builtins
db_1         | 2022-08-26T22:39:44.399377Z 0 [Note] InnoDB: Uses event mutexes
db_1         | 2022-08-26T22:39:44.399380Z 0 [Note] InnoDB: GCC builtin __atomic_thread_fence() is used for memory barrier
db_1         | 2022-08-26T22:39:44.399382Z 0 [Note] InnoDB: Compressed tables use zlib 1.2.12
db_1         | 2022-08-26T22:39:44.399388Z 0 [Note] InnoDB: Using Linux native AIO
db_1         | 2022-08-26T22:39:44.399710Z 0 [Note] InnoDB: Number of pools: 1
db_1         | 2022-08-26T22:39:44.399978Z 0 [Note] InnoDB: Using CPU crc32 instructions
db_1         | 2022-08-26T22:39:44.401692Z 0 [Note] InnoDB: Initializing buffer pool, total size = 128M, instances = 1, chunk size = 128M
db_1         | 2022-08-26T22:39:44.410129Z 0 [Note] InnoDB: Completed initialization of buffer pool
db_1         | 2022-08-26T22:39:44.412116Z 0 [Note] InnoDB: If the mysqld execution user is authorized, page cleaner thread priority can be changed. See the man page of setpriority().
db_1         | 2022-08-26T22:39:44.458683Z 0 [Note] InnoDB: Highest supported file format is Barracuda.
db_1         | 2022-08-26T22:39:44.464696Z 0 [Note] InnoDB: Log scan progressed past the checkpoint lsn 12142046
db_1         | 2022-08-26T22:39:44.464755Z 0 [Note] InnoDB: Doing recovery: scanned up to log sequence number 12142055
db_1         | 2022-08-26T22:39:44.464766Z 0 [Note] InnoDB: Database was not shutdown normally!
db_1         | 2022-08-26T22:39:44.464770Z 0 [Note] InnoDB: Starting crash recovery.
db_1         | 2022-08-26T22:39:44.676520Z 0 [Note] InnoDB: Removed temporary tablespace data file: "ibtmp1"
db_1         | 2022-08-26T22:39:44.676568Z 0 [Note] InnoDB: Creating shared tablespace for temporary tables
db_1         | 2022-08-26T22:39:44.678984Z 0 [Note] InnoDB: Setting file './ibtmp1' size to 12 MB. Physically writing the file full; Please wait ...
db_1         | 2022-08-26T22:39:44.742644Z 0 [Note] InnoDB: File './ibtmp1' size is now 12 MB.
db_1         | 2022-08-26T22:39:44.748150Z 0 [Note] InnoDB: 96 redo rollback segment(s) found. 96 redo rollback segment(s) are active.
db_1         | 2022-08-26T22:39:44.748211Z 0 [Note] InnoDB: 32 non-redo rollback segment(s) are active.
db_1         | 2022-08-26T22:39:44.749582Z 0 [Note] InnoDB: 5.7.39 started; log sequence number 12142055
db_1         | 2022-08-26T22:39:44.749865Z 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
db_1         | 2022-08-26T22:39:44.750767Z 0 [Note] Plugin 'FEDERATED' is disabled.
db_1         | 2022-08-26T22:39:44.780819Z 0 [Note] Found ca.pem, server-cert.pem and server-key.pem in data directory. Trying to enable SSL support using them.
db_1         | 2022-08-26T22:39:44.780836Z 0 [Note] Skipping generation of SSL certificates as certificate files are present in data directory.
db_1         | 2022-08-26T22:39:44.780840Z 0 [Warning] A deprecated TLS version TLSv1 is enabled. Please use TLSv1.2 or higher.
db_1         | 2022-08-26T22:39:44.780841Z 0 [Warning] A deprecated TLS version TLSv1.1 is enabled. Please use TLSv1.2 or higher.
db_1         | 2022-08-26T22:39:44.795966Z 0 [Warning] CA certificate ca.pem is self signed.
db_1         | 2022-08-26T22:39:44.796235Z 0 [Note] Skipping generation of RSA key pair as key files are present in data directory.
db_1         | 2022-08-26T22:39:44.802098Z 0 [Note] Server hostname (bind-address): '*'; port: 3306
db_1         | 2022-08-26T22:39:44.802149Z 0 [Note] IPv6 is available.
db_1         | 2022-08-26T22:39:44.802163Z 0 [Note]   - '::' resolves to '::';
db_1         | 2022-08-26T22:39:44.802181Z 0 [Note] Server socket created on IP: '::'.
db_1         | 2022-08-26T22:39:44.804645Z 0 [Warning] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
db_1         | 2022-08-26T22:39:44.805946Z 0 [Note] InnoDB: Buffer pool(s) load completed at 220826 22:39:44
db_1         | 2022-08-26T22:39:45.037204Z 0 [Note] Event Scheduler: Loaded 0 events
db_1         | 2022-08-26T22:39:45.037483Z 0 [Note] mysqld: ready for connections.
db_1         | Version: '5.7.39'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server (GPL)
```

## Setup Your WordPress Site

Now go ahead and load http://127.0.0.1:8000 in your browser. You'll see some more output in your Docker Compose terminal, showing you exactly what requests your browser is making:

```
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:08 +0000] "GET / HTTP/1.1" 302 405 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:09 +0000] "GET /wp-admin/install.php HTTP/1.1" 200 4627 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:10 +0000] "GET /wp-includes/css/buttons.min.css?ver=5.9.1 HTTP/1.1" 200 1791 "http://127.0.0.1:8000/wp-admin/install.php" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:10 +0000] "GET /wp-admin/css/l10n.min.css?ver=5.9.1 HTTP/1.1" 200 1022 "http://127.0.0.1:8000/wp-admin/install.php" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:10 +0000] "GET /wp-admin/css/forms.min.css?ver=5.9.1 HTTP/1.1" 200 6549 "http://127.0.0.1:8000/wp-admin/install.php" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:10 +0000] "GET /wp-admin/css/install.min.css?ver=5.9.1 HTTP/1.1" 200 2125 "http://127.0.0.1:8000/wp-admin/install.php" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:10 +0000] "GET /wp-includes/css/dashicons.min.css?ver=5.9.1 HTTP/1.1" 200 36068 "http://127.0.0.1:8000/wp-admin/install.php" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:10 +0000] "GET /wp-admin/js/language-chooser.min.js?ver=5.9.1 HTTP/1.1" 200 622 "http://127.0.0.1:8000/wp-admin/install.php" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:10 +0000] "GET /wp-includes/js/jquery/jquery-migrate.min.js?ver=3.3.2 HTTP/1.1" 200 4520 "http://127.0.0.1:8000/wp-admin/install.php" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:10 +0000] "GET /wp-includes/js/jquery/jquery.min.js?ver=3.6.0 HTTP/1.1" 200 31262 "http://127.0.0.1:8000/wp-admin/install.php" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:10 +0000] "GET /wp-admin/images/wordpress-logo.svg?ver=20131107 HTTP/1.1" 200 1810 "http://127.0.0.1:8000/wp-admin/css/install.min.css?ver=5.9.1" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:10 +0000] "GET /wp-admin/images/spinner-2x.gif HTTP/1.1" 200 7822 "http://127.0.0.1:8000/wp-admin/css/install.min.css?ver=5.9.1" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 172.18.0.1 - - [25/Feb/2022:17:02:10 +0000] "GET /favicon.ico HTTP/1.1" 302 404 "http://127.0.0.1:8000/wp-admin/install.php" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
homework-6-3-wordpress-1  | 127.0.0.1 - - [25/Feb/2022:17:02:15 +0000] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.52 (Debian) PHP/7.4.28 (internal dummy connection)"
homework-6-3-wordpress-1  | 127.0.0.1 - - [25/Feb/2022:17:02:16 +0000] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.52 (Debian) PHP/7.4.28 (internal dummy connection)"
```

![Screenshot of Wordpress](./chapter-6-3-wordpress.png)

## Open a Shell in a Running Container

Open a separate terminal and run:

```sh
docker-compose ps
```

Example:

```
micah@trapdoor homework-6-3 % docker-compose ps
          Name                        Command               State          Ports        
----------------------------------------------------------------------------------------
homework-6-3_db_1          docker-entrypoint.sh mysqld      Up      3306/tcp, 33060/tcp 
homework-6-3_wordpress_1   docker-entrypoint.sh apach ...   Up      0.0.0.0:8000->80/tcp
```

Open a bash shell in the WordPress container:

```sh
docker-compose exec wordpress bash
```

Example:

```
micah@trapdoor homework-6-3 % docker-compose exec wordpress bash
root@4fe8833c3fe6:/var/www/html# 
```

Check out the files in the WordPress container.

```sh
ls -lh
```

Example:

```
root@4fe8833c3fe6:/var/www/html# ls -lh
total 232K
-rw-r--r--  1 www-data www-data  405 Feb  6  2020 index.php
-rw-r--r--  1 www-data www-data  20K Jan  1 00:15 license.txt
-rw-r--r--  1 www-data www-data 7.3K Dec 28 17:38 readme.html
-rw-r--r--  1 www-data www-data 7.0K Jan 21  2021 wp-activate.php
drwxr-xr-x  9 www-data www-data 4.0K Feb 22 15:19 wp-admin
-rw-r--r--  1 www-data www-data  351 Feb  6  2020 wp-blog-header.php
-rw-r--r--  1 www-data www-data 2.3K Nov  9 23:07 wp-comments-post.php
-rw-rw-r--  1 www-data www-data 5.4K Feb 24 01:03 wp-config-docker.php
-rw-r--r--  1 www-data www-data 3.0K Dec 14 08:44 wp-config-sample.php
-rw-r--r--  1 www-data www-data 5.5K Feb 25 16:59 wp-config.php
drwxr-xr-x  5 www-data www-data 4.0K Feb 25 17:02 wp-content
-rw-r--r--  1 www-data www-data 3.9K Aug  3  2021 wp-cron.php
drwxr-xr-x 26 www-data www-data  16K Feb 22 15:19 wp-includes
-rw-r--r--  1 www-data www-data 2.5K Feb  6  2020 wp-links-opml.php
-rw-r--r--  1 www-data www-data 3.9K May 15  2021 wp-load.php
-rw-r--r--  1 www-data www-data  47K Jan  4 08:30 wp-login.php
-rw-r--r--  1 www-data www-data 8.4K Sep 22 21:01 wp-mail.php
-rw-r--r--  1 www-data www-data  23K Nov 30 17:32 wp-settings.php
-rw-r--r--  1 www-data www-data  32K Oct 25 00:23 wp-signup.php
-rw-r--r--  1 www-data www-data 4.7K Oct  8  2020 wp-trackback.php
-rw-r--r--  1 www-data www-data 3.2K Jun  8  2020 xmlrpc.php
```

Let's see what's in `wp-config.php`:

```sh
cat wp-config.php
```

Example:

```
root@7a313b222cd4:/var/www/html# cat wp-config.php 
<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * This has been slightly modified (to read environment variables) for use in Docker.
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// IMPORTANT: this file needs to stay in-sync with https://github.com/WordPress/WordPress/blob/master/wp-config-sample.php
// (it gets parsed by the upstream wizard in https://github.com/WordPress/WordPress/blob/f27cb65e1ef25d11b535695a660e7282b98eb742/wp-admin/setup-config.php#L356-L392)

// a helper function to lookup "env_FILE", "env", then fallback
if (!function_exists('getenv_docker')) {
	// https://github.com/docker-library/wordpress/issues/588 (WP-CLI will load this file 2x)
	function getenv_docker($env, $default) {
		if ($fileEnv = getenv($env . '_FILE')) {
			return rtrim(file_get_contents($fileEnv), "\r\n");
		}
		else if (($val = getenv($env)) !== false) {
			return $val;
		}
		else {
			return $default;
		}
	}
}

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', getenv_docker('WORDPRESS_DB_NAME', 'wordpress') );

/** Database username */
define( 'DB_USER', getenv_docker('WORDPRESS_DB_USER', 'example username') );

/** Database password */
define( 'DB_PASSWORD', getenv_docker('WORDPRESS_DB_PASSWORD', 'example password') );

/**
 * Docker image fallback values above are sourced from the official WordPress installation wizard:
 * https://github.com/WordPress/WordPress/blob/f9cc35ebad82753e9c86de322ea5c76a9001c7e2/wp-admin/setup-config.php#L216-L230
 * (However, using "example username" and "example password" in your database is strongly discouraged.  Please use strong, random credentials!)
 */

/** Database hostname */
define( 'DB_HOST', getenv_docker('WORDPRESS_DB_HOST', 'mysql') );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', getenv_docker('WORDPRESS_DB_CHARSET', 'utf8') );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', getenv_docker('WORDPRESS_DB_COLLATE', '') );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         getenv_docker('WORDPRESS_AUTH_KEY',         'b6bd1c5789f8a5adb7eed40cf57ec78a63460828') );
define( 'SECURE_AUTH_KEY',  getenv_docker('WORDPRESS_SECURE_AUTH_KEY',  'd1cedea61277f84ae2dc11491f7130152ce50587') );
define( 'LOGGED_IN_KEY',    getenv_docker('WORDPRESS_LOGGED_IN_KEY',    'feddc62a06c08514dea6a7ef70bc5516f9d47435') );
define( 'NONCE_KEY',        getenv_docker('WORDPRESS_NONCE_KEY',        '97a5847ebf26a45d8bf25b547d29ee432acbf6e2') );
define( 'AUTH_SALT',        getenv_docker('WORDPRESS_AUTH_SALT',        'e7da1a994cab84b1675a704c272ec8bfdb3ad8cc') );
define( 'SECURE_AUTH_SALT', getenv_docker('WORDPRESS_SECURE_AUTH_SALT', '50e58188282825066bbd93feb09bdbd07a18d9cb') );
define( 'LOGGED_IN_SALT',   getenv_docker('WORDPRESS_LOGGED_IN_SALT',   '7688a09f1bfc298198bfcaf75917d5b61a5b38c5') );
define( 'NONCE_SALT',       getenv_docker('WORDPRESS_NONCE_SALT',       'b4b2fc2760f3f496f1a9f4c6e13ce095b197cdef') );
// (See also https://wordpress.stackexchange.com/a/152905/199287)

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = getenv_docker('WORDPRESS_TABLE_PREFIX', 'wp_');

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', !!getenv_docker('WORDPRESS_DEBUG', '') );

/* Add any custom values between this line and the "stop editing" line. */

// If we're behind a proxy server and using HTTPS, we need to alert WordPress of that fact
// see also https://wordpress.org/support/article/administration-over-ssl/#using-a-reverse-proxy
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && strpos($_SERVER['HTTP_X_FORWARDED_PROTO'], 'https') !== false) {
	$_SERVER['HTTPS'] = 'on';
}
// (we include this by default because reverse proxying is extremely common in container environments)

if ($configExtra = getenv_docker('WORDPRESS_CONFIG_EXTRA', '')) {
	eval($configExtra);
}

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
```

## Stop Docker Compose

In your first terminal, press CTRL-C to stop the containers.