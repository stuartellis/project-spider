# SPDX-FileCopyrightText: 2023-present Stuart Ellis <stuart@stuartellis.name>
#
# SPDX-License-Identifier: MIT
import sys
import click

import project_spider.request_utils as r

from project_spider.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="Project Spider")
def project_spider():
    pass

@project_spider.command()
def info():
    print(f"Platform: {sys.version}")
    r.canary()


if getattr(sys, 'frozen', False):
    project_spider(sys.argv[1:])
