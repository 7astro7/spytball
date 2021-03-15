import getpass

try:
    USER = getpass.getuser()
except KeyError:
    pass

try:
    CONFIG_DIR = os.path.join(os.path.expanduser("~%s" % USER), ".spytball")
except KeyError:
    pass

SOURCE_DIR_LIST = [
    "bash",
]
VERSION = 0.01

GPG_CONFIG_DIR = None
LAST_BACKUP_DIR = None
