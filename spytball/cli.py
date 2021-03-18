"""
Usage:
    spytball [OPTIONS] [FILE1, FILE2, ...]
    spytball (d | decrypt-dir) [-v | --verbose] [$directory_name]
    spytball (e | encrypt-dir) [-o $output_name] [-n --no-recurse] [$directory_name]
    spytball examples 
    spytball (config | configure)
    spytball (-h | --help)
    spytball (c | --help)


Options:
    -h  --help           Show this help message and exit
    -v  --verbose        Print files to stdout as they're processed
    -n  --no-recurse     Don't recurse into subdirectories.
    -S  --source-dirs    List of directories to add to tarball.
    -o  --outfile        Save resulting tarball as name.
    -d  --dry-run        Trial run.
    -x  --exclude        Skip files when making tarball.
    -ov --overwrite      Encrypt original files: don't make a copy to encrypt (default False).
    -r  --recipients     Recipients of encryption.
    -p  --passphrase     Decrypt using passphrase. No option to save it.

Commands:
    e, encrypt-dir       Encrypt directory. 
    d, decrypt-dir       Decrypt directory.
    config, configure    Change configuration.
    examples             Show examples.
    test                 Trial run on simulated files.

Arguments:
    <filename>

Examples:
    ----
"""

# fix examples
# --help output should fit in a shell with no need for $ less
# make configuration 

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

    args = docopt(__doc__, version=f"spytball v%s" % VERSION)
    print(VERSION)

    if args.get(""):






