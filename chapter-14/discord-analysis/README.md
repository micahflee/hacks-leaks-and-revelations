# Discord JSON Search

A tool to search Discord JSON files for keywords, and showing you specific messages that include those keywords, as well as the channels they're in.

Note: This tool was developed in 2017 for a specific journalism project that's featured in Chapter 14 of [Hacks, Leaks, and Revelations](https://github.com/micahflee/hacks-leaks-and-revelations). It's no longer under development.

## Getting started

Install dependencies:

```sh
$ python3 -m venv venv
$ . venv/bin/activate
(env) $ pip3 install -r requirements.txt
```

Initialize the database:

```sh
(venv) $ ./admin.py create-db
(venv) $ ./admin.py import-json [filename.json] # do this for each JSON file
```

To start the app:

```sh
(venv) $ ./app.py
```

## Simple command line tool

You can also use `discord-json-search` to search an individual JSON file for keywords.
