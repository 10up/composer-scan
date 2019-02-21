
# WordPress Composer Scan

Scan composer.lock file to find vulnerable WordPress plugins/themes using https://wpvulndb.com/ api"

## Requirements

Supports most major python versions since 2.7, see `tox.ini` for tested versions

Required python packages (will automatically be installed by setup.py)

```:text
requests
click
```

Also requires an API key from [WPVulnDB](https://wpvulndb.com/)

## Install

Clone this repo and install with pip

```:bash
git clone git@gitlab.10up.com:10up-systems/ci-tools/composer-scan.git composer-scan
cd composer-scan
pip install .   ## installs the python package in the currnet directory
```

## Usage

```:bash
> composer-scan --help
Usage: composer-scan [OPTIONS]

  Console script for composer_scan.

Options:
  -f PATH       composer.lock file to scan, defaults to file in current
                directory
  -v            Verbose output, show status of all plugins, if not set only
                outputs found vulnerabilities
  --no-fail     even if vulnerabilities are found, exit 0 (emergency option to
                not fail CI pipelines)
  --token TEXT  WPVulnDB api token or set as envrionment variable:
                WPVULNDB_API_TOKEN  [required]
  --help        Show this message and exit.
```

The WPVulnDB API key can be specified on the command line in an envrionment variable `WPVULNDB_API_TOKEN`. `-f` can be used to specify the file to scan, if not used `composer.lock` in the currnet directory will be used

```:bash
> export WPVULNDB_API_TOKEN="api_token"
> composer-scan -f ~/wp-local-docker-sites/mysite/wordpress/wp-content/composer.lock
```
