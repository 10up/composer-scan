#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `composer_scan` package."""

import pytest

from click.testing import CliRunner

from composer_scan import composer_scan
from composer_scan import cli
from lock_tests import lock_tests


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output



def test_plugins():
    runner = CliRunner()
    for lock_test in lock_tests:
        with runner.isolated_filesystem():
            with open("composer.lock", "w") as lockfile:
                lockfile.write(lock_test["file_contents"])

            result = runner.invoke(cli.main, lock_test["args"])
            assert lock_test["return_code"] == result.exit_code
            assert lock_test["text_search"] in result.output
            assert lock_test["vuln_url"] in result.output

