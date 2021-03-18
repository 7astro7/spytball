import tarfile
import os
from datetime import datetime
from .constants import (
    SOURCE_DIR_LIST,
)

# verify integrity of tarball


class Archive:
    """Make a tarball. Archive isn't encrypted yet."""

    def __init__(
        self,
        ext: str = "xz",
        source_dirs=SOURCE_DIR_LIST,
    ):
        self.yolo = True
        self.source_dirs = source_dirs
        self.ext = ext

    def make_tarball(
        self,
        tarball_name: str = None,
        ext: str = None,
        source_dirs: list = None,
        verbose=True,
    ):
        if ext is None:
            ext = self.ext
        if source_dirs is None:
            source_dirs = self.source_dirs
        if not isinstance(source_dirs, list):
            if not isinstance(source_dirs, tuple):
                raise TypeError(
                    "source_dirs",
                    source_dirs,
                    "is not a list or tuple",
                )
        if tarball_name is None:
            now = datetime.now().strftime("%d_%b_%Y_%H_%M_%S")
            tarball_name = f"backup_on_%s.tar.%s" % (now, ext)
        is_path = lambda directory: os.path.exists(directory)
        source_dirs = tuple(filter(is_path, source_dirs))
        if not len(source_dirs):
            raise FileNotFoundError(
                "source_dirs includes 0 \
                    existent paths"
            )
        i = 0
        try:
            with tarfile.open(tarball_name, f"w:%s" % ext) as tar:
                while True:
                    if i >= len(source_dirs):
                        break
                    tar.add(source_dirs[i], arcname=os.path.basename(source_dirs[i]))
                    if verbose:
                        print("Added: %s to tarball" % source_dirs[i])
                    i += 1
        except:
            raise FileNotFoundError("tarball not made")

    def decompress_last_backup(self):
        pass


if __name__ == "__main__":
    Backup()
