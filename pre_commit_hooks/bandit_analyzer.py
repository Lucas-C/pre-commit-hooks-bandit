from __future__ import print_function
import sys
from bandit.cli.main import main as bandit_cli_main


def main():
    try:
        bandit_cli_main()
    except SystemExit as error:
        if error.code == 0:
            return 0
        return 1


if __name__ == '__main__':
    sys.exit(main())
