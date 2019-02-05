# -*- coding: utf-8 -*-

"""Console script for composer_scan."""
import sys
import click
import json
from .composer_scan import scanFile
import os

@click.command()
@click.option('-f', help="composer.lock file to scan, defaults to file in current directory", type=click.Path(exists=False), default="composer.lock")
@click.option('-v', help="Verbose output, show status of all plugins, if not set only outputs found vulnerabilities", is_flag=True)
@click.option('--no-fail', help="even if vulnerabilities are found, exit 0 (emergency option to not fail CI pipelines)", envvar="COMPOSER_SCAN_NO_FAIL", is_flag=True)
@click.option('--token', help="WPVulnDB api token or set as envrionment variable: WPVULNDB_API_TOKEN", envvar="WPVULNDB_API_TOKEN", required=True)
@click.pass_context
def main(ctx, f, v, no_fail, token):
    """Console script for composer_scan."""
    if 'CI' in os.environ:
        ctx.color = True

    if not os.path.exists(f):
        click.echo("{} does not exist, exiting scan".format(f))
        sys.exit(0)

    try:
        with open(f, 'r') as input:
            composer_obj = json.load(input)

    except Exception as e:
        click.echo("unable to open {}".format(f))
        click.echo(e)
        sys.exit(1)

    found = scanFile(composer_obj, v)

    if no_fail:
        click.secho("no-fail flag set, exiting 0...")
        sys.exit(0)
    sys.exit(found)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
