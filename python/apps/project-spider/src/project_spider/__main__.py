# SPDX-FileCopyrightText: 2023-present Stuart Ellis <stuart@stuartellis.name>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from project_spider.cli import project_spider

    sys.exit(project_spider())
