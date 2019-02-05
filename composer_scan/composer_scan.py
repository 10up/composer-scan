# -*- coding: utf-8 -*-

"""Main module."""

import json
import re
import requests
from distutils.version import LooseVersion
import click


def scanFile(composer_obj, verbose, token):

    headers = {
        "Authorization": "Token token={}".format(token)
    }

    globalFound = 0

    for package in composer_obj['packages']:
        if re.match("wordpress-[plugin|theme]", package["type"]):
            _type = package["type"].split("-")[-1]
            name = package["name"].split("/")[-1]
            version = package['version']

            try:
                r = requests.get("https://wpvulndb.com/api/v3/{}/{}".format(
                    _type+"s",
                    name
                ), headers=headers)
                r.raise_for_status()
            except Exception:
                if r.status_code == 404:
                    if verbose:
                        click.secho("{} not found on WPVulnDB".format(name), fg="yellow")
                        click.echo()
                    continue
                else:
                    click.secho("API request for {} failed".format(name), fg="yellow")
                    click.echo(r.status_code)
                    click.echo()
                    continue

            if len(json.loads(r.text)[name]['vulnerabilities']) > 0:
                found = 0
                titlePrint = False
                for v in json.loads(r.text)[name]['vulnerabilities']:
                    if not LooseVersion(version) >= LooseVersion(v["fixed_in"]):
                        if not titlePrint:
                            click.echo("{} - {} - {}".format(name, version, _type))
                            titlePrint = True
                        click.secho("VULNERABILITY FOUND!!!", fg="red")
                        click.echo("{}".format(v["title"]))
                        click.echo("https://wpvulndb.com/vulnerabilities/{}".format(v["id"]))
                        # set found to 1 so we can exit
                        found = 1
                if not found:
                    if verbose:
                        click.echo("{} - {} - {}".format(name, version, _type))
                        click.secho("{} {} has reported vulnerabilities, but they are all fixed in version {}".format(_type, name, version), fg="green")
                        click.echo()
                else:
                    globalFound = 1
                    click.echo()

            else:
                if verbose:
                    click.echo("{} - {} - {}".format(name, version, _type))
                    click.secho("No vulnerabilities found for {} {}".format(_type, name), fg="green")
                    click.echo()

    return globalFound
