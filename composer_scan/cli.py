# -*- coding: utf-8 -*-

"""Console script for composer_scan."""
import sys
import click
import json
from .composer_scan import scanFile


@click.option('-f', help="composer.lock file to scan, defaults to file in current directory", type=click.Path(exists=True), default="composer.lock")
@click.command()
def main(f):
    """Console script for composer_scan."""
    try:
        with open(f, 'r') as input:
            composer_obj = json.load(input)

    except Exception as e:
        click.echo("unable to open {}".format(f))
        click.echo(e)
        sys.exit(1)

    found = scanFile(composer_obj)
    sys.exit(found)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
