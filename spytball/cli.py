"""
A simple Python utility that uses GPG to: 
    encrypt directories.
    decrypt directories.
    encrypt files.
    decrypt files.
    make tarballs wherein each file is encrypted.

Usage:
    spytball (d | decrypt) [-v | --verbose] <directory-name>
    spytball (e | encrypt) [-o $output_name] [-n | --no-recurse] <directory-name>
    spytball examples 
    spytball (config | configure)
    spytball (-h | --help)
    spytball test

Arguments:
    <directory_name>
    <file_name>

Options:
    -h  --help           Show this help message and exit
    -v  --verbose        Print files to stdout as they're processed
    -n  --no-recurse     Don't recurse into subdirectories
    -S  --source-dirs    List of directories to add to tarball
    -o                   Specify output file
    -d  --dry-run        Trial run
    -x  --exclude        Skip files when making tarball
    --overwrite          Encrypt original files: don't make a copy to encrypt (default False)
    -r  --recipients     Recipients of encrypted files

Commands:
    e, encrypt           Encrypt directory. 
    d, decrypt           Decrypt directory.
    config, configure    Change configuration.
    remember             Remember recipient.
    examples             Show examples.
    test                 Trial run on simulated files.
    version              Show version and exit.
"""

# fix examples
# --help output should fit in a shell with no need for $ less
# make configuration 
# check gpg to see if it's ever okay to save passwords 
# *reference pass for password retrieval if non-privileged user*
# show gpg help message?
# allow for environment variables as parameters

from .spyt import GPG
from .ball import Archive
from docopt import docopt
from .constants import VERSION
import configparser
import sys
import os
from .utils import get_directory_name, simulate_a_spytball


default_encrypt_params = {
    "recipients": [], # populate with config values
    "recursive": True,
    "overwrite": False
}

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
    Make an encrypted backup, a spytball
    """

    args = docopt(__doc__, version=f"Spytball v%s" % VERSION)

    if args.get("version") or args.get("--version"):
        print("Spytball version %s" % VERSION)

    if args.get("e") or args.get("encrypt"):
        params = {
            "verbose": 0,
            "recursive": True,
            "recipients": None,
            "dir_name": None
        }
#       if not(args.get("recipients") or no recipient set in config
        if not args.get("recipients"):
            # IF NO RECIPIENTS SET IN CONFIG
            print("No recipients chosen")
            sys.exit(1)
        params["dir_name"] = get_directory_name(args.get("directory_name")) # may have to check first, then assign
        if args.get("--overwrite"):
            params["overwrite"] = True
        params["verbose"] = get_verbose(args)
        GPG().encrypt_dir(**params)
        sys.exit(0)
        
    if args.get("d") or args.get("decrypt"):
        params = {
            "verbose": 0,
            "recursive": True,
            # passphrase
            "dir_name": None
        }
        if args.get("-n") or args.get("--no-recurse"):
            default_options["recursive"] = False 
        params["verbose"] = get_verbose(args)
        GPG().decrypt_dir(**params)
        sys.exit(0)
    
    elif args.get("test"):
        simulate_a_spytball()

    elif args.get("examples"):
        # last
        pass

    if args.get("config") or args.get("configure"):
        pass

def get_verbose(args) -> int:
    """
    """
    if args.get("-v") or args.get("--verbose"):
        a, b = args.get("-v"), args.get("--verbose")
        verbose = int(a if a else b)
        if params["verbose"] < 1:
            return 0
        elif params["verbose"] > 1:
            return 2
    return 1

def examples():
    """
    Show example commands
    """
    pass

def print_usage():
    pass
