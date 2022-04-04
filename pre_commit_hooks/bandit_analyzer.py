from __future__ import print_function
import sys
import bandit
from bandit.cli.main import main as bandit_cli_main


def main():
    print(f"Bandit version: {bandit.__version__}")
    print("Calling", " ".join(sys.argv))
    try:
        bandit_cli_main()
        return 0
    except SystemExit as error:
        return error.code


if __name__ == '__main__':
    sys.exit(main())
