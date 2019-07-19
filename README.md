# WordPress Composer Scan

> Scans your composer.lock file to find vulnerable WordPress plugins and themes using the [WPScan Vulnerability Database](https://wpvulndb.com) API

[![Support Level](https://img.shields.io/badge/support-active-green.svg)](#support-level) [![MIT License](https://img.shields.io/github/license/10up/composer-scan.svg)](https://github.com/10up/composer-scan/blob/master/LICENSE.md)

## Requirements

- API key from the [WPScan Vulnerability Database](https://wpvulndb.com)
- Supports most major Python versions since 2.7, see [`tox.ini`](https://github.com/10up/composer-scan/blob/update/docs/tox.ini) for tested versions
- Required Python packages (will automatically be installed by setup.py):

```:text
requests
click
```

## Installation

Clone this repo and install with pip:

```:bash
git clone https://github.com/10up/composer-scan.git composer-scan
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
  --token TEXT  WPVulnDB API token or set as envrionment variable:
                WPVULNDB_API_TOKEN  [required]
  --help        Show this message and exit.
```

The WPScan Vulnerability Database API key can be specified on the command line in an envrionment variable `WPVULNDB_API_TOKEN`. `-f` can be used to specify the file to scan, if not used `composer.lock` in the currnet directory will be used.

```:bash
> export WPVULNDB_API_TOKEN="api_token"
> composer-scan -f ~/wp-local-docker-sites/mysite/wordpress/wp-content/composer.lock
```

## Support Level

**Active:** 10up is actively working on this, and we expect to continue work for the foreseeable future including keeping tested up to the most recent version of WordPress.  Bug reports, feature requests, questions, and pull requests are welcome.

## Contributing

Please read [CODE_OF_CONDUCT.md](https://github.com/10up/classifai/blob/develop/CODE_OF_CONDUCT.md) for details on our code of conduct and [CONTRIBUTING.md](https://github.com/10up/classifai/blob/develop/CONTRIBUTING.md) for details on the process for submitting pull requests to us.

## Like what you see?

<a href="http://10up.com/contact/"><img src="https://10updotcom-wpengine.s3.amazonaws.com/uploads/2016/10/10up-Github-Banner.png" width="850" alt="Work with us at 10up"></a>
