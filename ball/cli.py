
"""
Usage:
    spytball [OPTIONS] [FILE1, FILE2, ...]



Options:
    -h --help           Show this help message and exit
    -v --verbose        Print files to stdout as they're processed
    -S --source-dirs    List of directories to add to tarball
    -o --outfile        Save resulting tarball as name
    -d --dry-run        Trial run
    -x --exclude        Skip files when making tarball

Commands:
    configure
    examples

Arguments:
    <filename>
"""

from make_tarball import Backup
from docopt import docopt
from constants import VERSION
import sys

def main():
    """
    Main method
    """
    try:
        cli()
    except KeyboardInterrupt:
        print("Exiting")
        sys.exit(1)

def cli():
    """
    Make an encrypted backup, a spytball. Remote sync not
    integrated yet.
    """

    args = docopt(__doc__, version = f"spytball v%s" % VERSION)
    print(VERSION)


if __name__ == "__main__":
    main()
