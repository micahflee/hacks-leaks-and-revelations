# Homework 6-3: Quickly Run a WordPress Site With Docker Compose

You can find the `docker-compose.yaml` file used in this homework [here](./wordpress/docker-compose.yaml).

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
micah@trapdoor wordpress % docker-compose up
Creating network "wordpress_default" with the default driver
Creating volume "wordpress_db_data" with default driver
Creating volume "wordpress_wordpress_data" with default driver
Creating wordpress_db_1        ... done
Creating wordpress_wordpress_1 ... done
Attaching to wordpress_db_1, wordpress_wordpress_1
db_1         | 2022-08-28 18:07:33+00:00 [Note] [Entrypoint]: Entrypoint script for MariaDB Server 1:10.9.2+maria~ubu2204 started.
wordpress_1  | WordPress not found in /var/www/html - copying now...
db_1         | 2022-08-28 18:07:33+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
db_1         | 2022-08-28 18:07:33+00:00 [Note] [Entrypoint]: Entrypoint script for MariaDB Server 1:10.9.2+maria~ubu2204 started.
wordpress_1  | Complete! WordPress has been successfully copied to /var/www/html
wordpress_1  | No 'wp-config.php' found in /var/www/html, but 'WORDPRESS_...' variables supplied; copying 'wp-config-docker.php' (WORDPRESS_DB_HOST WORDPRESS_DB_NAME WORDPRESS_DB_PASSWORD WORDPRESS_DB_USER)
db_1         | 2022-08-28 18:07:34+00:00 [Note] [Entrypoint]: Initializing database files
db_1         | 2022-08-28 18:07:34 0 [Warning] mariadbd: io_uring_queue_init() failed with ENOMEM: try larger memory locked limit, ulimit -l, or https://mariadb.com/kb/en/systemd/#configuring-limitmemlock under systemd (262144 bytes required)
db_1         | 2022-08-28 18:07:34 0 [Warning] InnoDB: liburing disabled: falling back to innodb_use_native_aio=OFF
wordpress_1  | AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.23.0.3. Set the 'ServerName' directive globally to suppress this message
wordpress_1  | AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.23.0.3. Set the 'ServerName' directive globally to suppress this message
wordpress_1  | [Sun Aug 28 18:07:34.449415 2022] [mpm_prefork:notice] [pid 1] AH00163: Apache/2.4.54 (Debian) PHP/7.4.30 configured -- resuming normal operations
wordpress_1  | [Sun Aug 28 18:07:34.449484 2022] [core:notice] [pid 1] AH00094: Command line: 'apache2 -D FOREGROUND'
db_1         | 
db_1         | 
db_1         | PLEASE REMEMBER TO SET A PASSWORD FOR THE MariaDB root USER !
db_1         | To do so, start the server, then issue the following command:
db_1         | 
db_1         | '/usr/bin/mysql_secure_installation'
db_1         | 
db_1         | which will also give you the option of removing the test
db_1         | databases and anonymous user created by default.  This is
db_1         | strongly recommended for production servers.
db_1         | 
db_1         | See the MariaDB Knowledgebase at https://mariadb.com/kb
db_1         | 
db_1         | Please report any problems at https://mariadb.org/jira
db_1         | 
db_1         | The latest information about MariaDB is available at https://mariadb.org/.
db_1         | 
db_1         | Consider joining MariaDB's strong and vibrant community:
db_1         | https://mariadb.org/get-involved/
db_1         | 
db_1         | 2022-08-28 18:07:35+00:00 [Note] [Entrypoint]: Database files initialized
db_1         | 2022-08-28 18:07:35+00:00 [Note] [Entrypoint]: Starting temporary server
db_1         | 2022-08-28 18:07:35+00:00 [Note] [Entrypoint]: Waiting for server startup
db_1         | 2022-08-28 18:07:35 0 [Note] mariadbd (server 10.9.2-MariaDB-1:10.9.2+maria~ubu2204) starting as process 93 ...
db_1         | 2022-08-28 18:07:35 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
db_1         | 2022-08-28 18:07:35 0 [Note] InnoDB: Number of transaction pools: 1
db_1         | 2022-08-28 18:07:35 0 [Note] InnoDB: Using crc32 + pclmulqdq instructions
db_1         | 2022-08-28 18:07:35 0 [Note] mariadbd: O_TMPFILE is not supported on /tmp (disabling future attempts)
db_1         | 2022-08-28 18:07:35 0 [Warning] mariadbd: io_uring_queue_init() failed with ENOMEM: try larger memory locked limit, ulimit -l, or https://mariadb.com/kb/en/systemd/#configuring-limitmemlock under systemd (262144 bytes required)
db_1         | 2022-08-28 18:07:35 0 [Warning] InnoDB: liburing disabled: falling back to innodb_use_native_aio=OFF
db_1         | 2022-08-28 18:07:35 0 [Note] InnoDB: Initializing buffer pool, total size = 128.000MiB, chunk size = 2.000MiB
db_1         | 2022-08-28 18:07:35 0 [Note] InnoDB: Completed initialization of buffer pool
db_1         | 2022-08-28 18:07:35 0 [Note] InnoDB: File system buffers for log disabled (block size=4096 bytes)
db_1         | 2022-08-28 18:07:35 0 [Note] InnoDB: 128 rollback segments are active.
db_1         | 2022-08-28 18:07:35 0 [Note] InnoDB: Setting file './ibtmp1' size to 12.000MiB. Physically writing the file full; Please wait ...
db_1         | 2022-08-28 18:07:35 0 [Note] InnoDB: File './ibtmp1' size is now 12.000MiB.
db_1         | 2022-08-28 18:07:35 0 [Note] InnoDB: log sequence number 45479; transaction id 14
db_1         | 2022-08-28 18:07:35 0 [Note] Plugin 'FEEDBACK' is disabled.
db_1         | 2022-08-28 18:07:35 0 [Warning] 'user' entry 'root@0362065ce624' ignored in --skip-name-resolve mode.
db_1         | 2022-08-28 18:07:35 0 [Warning] 'proxies_priv' entry '@% root@0362065ce624' ignored in --skip-name-resolve mode.
db_1         | 2022-08-28 18:07:35 0 [Note] mariadbd: ready for connections.
db_1         | Version: '10.9.2-MariaDB-1:10.9.2+maria~ubu2204'  socket: '/run/mysqld/mysqld.sock'  port: 0  mariadb.org binary distribution
db_1         | 2022-08-28 18:07:36+00:00 [Note] [Entrypoint]: Temporary server started.
db_1         | 2022-08-28 18:07:38+00:00 [Note] [Entrypoint]: Securing system users (equivalent to running mysql_secure_installation)
db_1         | 2022-08-28 18:07:38+00:00 [Note] [Entrypoint]: Creating database wordpress
db_1         | 2022-08-28 18:07:38+00:00 [Note] [Entrypoint]: Creating user wordpress
db_1         | 2022-08-28 18:07:38+00:00 [Note] [Entrypoint]: Giving user wordpress access to schema wordpress
db_1         | 
db_1         | 2022-08-28 18:07:38+00:00 [Note] [Entrypoint]: Stopping temporary server
db_1         | 2022-08-28 18:07:38 0 [Note] mariadbd (initiated by: root[root] @ localhost []): Normal shutdown
db_1         | 2022-08-28 18:07:38 0 [Note] InnoDB: FTS optimize thread exiting.
db_1         | 2022-08-28 18:07:38 0 [Note] InnoDB: Starting shutdown...
db_1         | 2022-08-28 18:07:38 0 [Note] InnoDB: Dumping buffer pool(s) to /var/lib/mysql/ib_buffer_pool
db_1         | 2022-08-28 18:07:38 0 [Note] InnoDB: Buffer pool(s) dump completed at 220828 18:07:38
db_1         | 2022-08-28 18:07:38 0 [Note] InnoDB: Removed temporary tablespace data file: "./ibtmp1"
db_1         | 2022-08-28 18:07:38 0 [Note] InnoDB: Shutdown completed; log sequence number 46729; transaction id 15
db_1         | 2022-08-28 18:07:38 0 [Note] mariadbd: Shutdown complete
db_1         | 
db_1         | 2022-08-28 18:07:39+00:00 [Note] [Entrypoint]: Temporary server stopped
db_1         | 
db_1         | 2022-08-28 18:07:39+00:00 [Note] [Entrypoint]: MariaDB init process done. Ready for start up.
db_1         | 
db_1         | 2022-08-28 18:07:39 0 [Note] mariadbd (server 10.9.2-MariaDB-1:10.9.2+maria~ubu2204) starting as process 1 ...
db_1         | 2022-08-28 18:07:39 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
db_1         | 2022-08-28 18:07:39 0 [Note] InnoDB: Number of transaction pools: 1
db_1         | 2022-08-28 18:07:39 0 [Note] InnoDB: Using crc32 + pclmulqdq instructions
db_1         | 2022-08-28 18:07:39 0 [Note] mariadbd: O_TMPFILE is not supported on /tmp (disabling future attempts)
db_1         | 2022-08-28 18:07:39 0 [Warning] mariadbd: io_uring_queue_init() failed with ENOMEM: try larger memory locked limit, ulimit -l, or https://mariadb.com/kb/en/systemd/#configuring-limitmemlock under systemd (262144 bytes required)
db_1         | 2022-08-28 18:07:39 0 [Warning] InnoDB: liburing disabled: falling back to innodb_use_native_aio=OFF
db_1         | 2022-08-28 18:07:39 0 [Note] InnoDB: Initializing buffer pool, total size = 128.000MiB, chunk size = 2.000MiB
db_1         | 2022-08-28 18:07:39 0 [Note] InnoDB: Completed initialization of buffer pool
db_1         | 2022-08-28 18:07:39 0 [Note] InnoDB: File system buffers for log disabled (block size=4096 bytes)
db_1         | 2022-08-28 18:07:39 0 [Note] InnoDB: 128 rollback segments are active.
db_1         | 2022-08-28 18:07:39 0 [Note] InnoDB: Setting file './ibtmp1' size to 12.000MiB. Physically writing the file full; Please wait ...
db_1         | 2022-08-28 18:07:39 0 [Note] InnoDB: File './ibtmp1' size is now 12.000MiB.
db_1         | 2022-08-28 18:07:39 0 [Note] InnoDB: log sequence number 46729; transaction id 14
db_1         | 2022-08-28 18:07:39 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
db_1         | 2022-08-28 18:07:39 0 [Note] Plugin 'FEEDBACK' is disabled.
db_1         | 2022-08-28 18:07:39 0 [Warning] You need to use --log-bin to make --expire-logs-days or --binlog-expire-logs-seconds work.
db_1         | 2022-08-28 18:07:39 0 [Note] InnoDB: Buffer pool(s) load completed at 220828 18:07:39
db_1         | 2022-08-28 18:07:39 0 [Note] Server socket created on IP: '0.0.0.0'.
db_1         | 2022-08-28 18:07:39 0 [Note] Server socket created on IP: '::'.
db_1         | 2022-08-28 18:07:39 0 [Note] mariadbd: ready for connections.
db_1         | Version: '10.9.2-MariaDB-1:10.9.2+maria~ubu2204'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

![Screenshot of Wordpress](./chapter-6-3-wordpress.png)

## Open a Shell in a Running Container

Open a separate terminal and run:

```sh
docker-compose ps
```

Example:

```
micah@trapdoor wordpress % docker-compose ps
        Name                       Command               State          Ports        
-------------------------------------------------------------------------------------
wordpress_db_1          docker-entrypoint.sh mariadbd    Up      3306/tcp            
wordpress_wordpress_1   docker-entrypoint.sh apach ...   Up      0.0.0.0:8000->80/tcp```

Open a bash shell in the WordPress container:

```sh
docker-compose exec wordpress bash
```

Example:

```
micah@trapdoor wordpress % docker-compose exec wordpress bash
root@1ba135713d6d:/var/www/html# 
```

Check out the files in the WordPress container.

```sh
ls -lh
```

Example:

```
root@1ba135713d6d:/var/www/html# ls -lh
total 232K
-rw-r--r--  1 www-data www-data  405 Feb  6  2020 index.php
-rw-r--r--  1 www-data www-data  20K Jan  1  2022 license.txt
-rw-r--r--  1 www-data www-data 7.3K Mar 22 21:11 readme.html
-rw-r--r--  1 www-data www-data 7.0K Jan 21  2021 wp-activate.php
drwxr-xr-x  9 www-data www-data 4.0K Jul 12 16:16 wp-admin
-rw-r--r--  1 www-data www-data  351 Feb  6  2020 wp-blog-header.php
-rw-r--r--  1 www-data www-data 2.3K Nov  9  2021 wp-comments-post.php
-rw-rw-r--  1 www-data www-data 5.4K Aug 23 23:37 wp-config-docker.php
-rw-r--r--  1 www-data www-data 3.0K Dec 14  2021 wp-config-sample.php
-rw-r--r--  1 www-data www-data 5.5K Aug 28 18:07 wp-config.php
drwxr-xr-x  5 www-data www-data 4.0K Jul 12 16:16 wp-content
-rw-r--r--  1 www-data www-data 3.9K Apr 28 09:49 wp-cron.php
drwxr-xr-x 26 www-data www-data  16K Jul 12 16:16 wp-includes
-rw-r--r--  1 www-data www-data 2.5K Mar 19 20:31 wp-links-opml.php
-rw-r--r--  1 www-data www-data 3.9K Apr 12 01:47 wp-load.php
-rw-r--r--  1 www-data www-data  48K Apr 29 14:36 wp-login.php
-rw-r--r--  1 www-data www-data 8.4K Mar 22 16:25 wp-mail.php
-rw-r--r--  1 www-data www-data  24K Apr 12 09:26 wp-settings.php
-rw-r--r--  1 www-data www-data  32K Apr 11 11:42 wp-signup.php
-rw-r--r--  1 www-data www-data 4.7K Apr 11 11:42 wp-trackback.php
-rw-r--r--  1 www-data www-data 3.2K Jun  8  2020 xmlrpc.php
```

Let's see what's in `wp-config.php`:

```sh
cat wp-config.php
```

Example:

```
root@1ba135713d6d:/var/www/html# cat wp-config.php
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
define( 'AUTH_KEY',         getenv_docker('WORDPRESS_AUTH_KEY',         '46edecbb34e8de68911318ccf8df68fe61908830') );
define( 'SECURE_AUTH_KEY',  getenv_docker('WORDPRESS_SECURE_AUTH_KEY',  '697b9513ce1c9864f6611c732ee13ade7bdae9e8') );
define( 'LOGGED_IN_KEY',    getenv_docker('WORDPRESS_LOGGED_IN_KEY',    '64104bef0443b4ea26401d89ad66a7b95cc4c993') );
define( 'NONCE_KEY',        getenv_docker('WORDPRESS_NONCE_KEY',        '25c86eaf78f2760183eab6348049481390613059') );
define( 'AUTH_SALT',        getenv_docker('WORDPRESS_AUTH_SALT',        '7799a3619c478e747853e0dff993700cb8deb8ea') );
define( 'SECURE_AUTH_SALT', getenv_docker('WORDPRESS_SECURE_AUTH_SALT', '87e3bfe026c4674588e40285c304157d7c66a527') );
define( 'LOGGED_IN_SALT',   getenv_docker('WORDPRESS_LOGGED_IN_SALT',   '436cfc5d65cd47ae084a0b702620bbed05f9dab0') );
define( 'NONCE_SALT',       getenv_docker('WORDPRESS_NONCE_SALT',       'd154627689453325c946d67ce0599c7be6ad192e') );
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