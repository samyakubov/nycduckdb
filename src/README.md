# NYCDB

**a tool for building a database of NYC housing data**

This is a Python library and cli tool for installing, updating and managing NYCDB, a postgres database of NYC Housing Data.

For more background information on this project and links to download copies of full database dump visit: https://github.com/nycdb/nycdb. We use the term **nycdb** to refer to both the python software and the running copy of the postgres database.

## Using the cli tool

You will need python 3.6+ and Postgres. The latest version can be installed from pypi with pip:  `python3 -m pip install nycdb`

If the installation is successful, you can view a summary of the tool's options by running `nycdb --help`

To print a list of datasets: ` nycdb --list-datasets`

`nycdb`'s main job is to download datasets and import them into postgres. It does not manage the database for you. You can use the flags `-U/--user`, `-D/--database`, `-P/--password`, and `-H/--host` to instruct nycdb to connect to the correct database. See `nycdb --help` for the defaults.

Example: downloading, loading, and verifying the dataset **hpd_violations**:

``` sh
nycdb --download hpd_violations
nycdb --load hpd_violations
nycdb --verify hpd_violations
```

To delete a previously imported dataset (for example, if you'd like to import an updated version of it), use the `--drop` option. For example, to delete the dataset **hpd_violations**: `nycdb --drop hpd_violations`.


By default the downloaded data files are is stored in `./data`. Use `--root-dir` to change the location of the data directory.

You can export a `.sql` file for any dataset by using the `--dump` command

## Development

There are two development workflows: one using python virtual environments and one using docker.

### Python3 virtual environments

If you have postgres installed separately, you can use this alternative method without docker:

Setup and active a virtual environment:

``` sh
python3 -m venv venv
source venv/bin/activate
```

Install nycdb: ` pip install -e ./src`

As long as the virtual environment is activated, you can use `nycdb` directly in your shell.