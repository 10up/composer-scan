# -*- coding: utf-8 -*-

"""Console script for composer_scan."""
import sys
import click
import json
from .composer_scan import scanFile


@click.option('-f', help="composer.lock file to scan, defaults to file in current directory", type=click.Path(exists=True), default="composer.lock")
@click.option('-v', help="Verbose output, show status of all plugins, if not set only outputs found vulnerabilities", is_flag=True)
@click.command()
def main(f, v):
    """Console script for composer_scan."""
    if 'CI' in os.environ:
        ctx.color = True
    try:
        with open(f, 'r') as input:
            composer_obj = json.load(input)

    except Exception as e:
        click.echo("unable to open {}".format(f))
        click.echo(e)
        sys.exit(1)

    found = scanFile(composer_obj, v)
    sys.exit(found)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
