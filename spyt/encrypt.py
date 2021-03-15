
import gnupg
import os

class GPG(gnupg.GPG):

    def __init__(self, gnupghome: str = None, recursive: bool = True):
        super().__init__()
        self.recursive = recursive
        if gnupghome is not None:
            self.gnupghome = gnupghome

    def _prepare_dir_operation(self, dir_name: str, recursive: bool = None):
        make_path = lambda i: os.path.join(dir_name, i)
        dir_contents = tuple(map(make_path, os.listdir(dir_name)))
        if not recursive or (recursive is None and not self.recursive):
            file_not_dir = lambda i: os.path.isfile(i)
            dir_contents = tuple(filter(file_not_dir, dir_contents))
        return dir_contents

    def _encrypt_file(self, path: str, recipients: str):
        self._check_path_exists(path)
        try:
            with open(path, "rb") as f:
                an_encryption = self.encrypt_file(
                        f,
                        recipients = recipients,
                        output = path
                        )
                print(f.name, "OK? ", an_encryption.ok)
        except IsADirectoryError:
            print('Cannot encrypt, %s is not a file' % path)

    def _check_path_exists(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError('Cannot find ', path)


    def _decrypt_file(self, path: str, passphrase: str):
        self._check_path_exists(path)
        try:
            with open(path, "rb") as f:
                a_decryption = self.decrypt_file(
                        f,
                        passphrase = passphrase,
                        output = path
                        )
                print(f.name, "OK? ", an_encryption.ok)
        except IsADirectoryError:
            print('Cannot encrypt, %s is not a file' % path)

    def encrypt_dir(self, dir_name: str, recipients: list, 
            recursive: bool = True):
        """
        """
        if recursive is None:
            recursive = self.recursive
        dir_op_args  = dict(dir_name, recursive)
        dir_contents = self._prepare_dir_operation(** dir_op_args)
#        make_path = lambda i: os.path.join(dir_name, i)
#        dir_contents = tuple(map(make_path, os.listdir(dir_name)))
#        if not recursive:
#            file_not_dir = lambda i: os.path.isfile(i)
#            dir_contents = tuple(filter(file_not_dir, dir_contents))
        for path in dir_contents:
            try:
                if os.path.isdir(path):
                    if not recursive:
                        message = "Cannot encrypt directory %s: \
                                recursive is set to False" % path
                        raise IsAdirectoryError(message)
                    self.encrypt_dir(dir_name = path, recipients = recipients)
                self._encrypt_file(path = path, recipients = recipients)
            except KeyError:
                print("Could not encrypt directory: ", dir_name)

    def decrypt_dir(self, dir_name: str, recursive: bool = None):
        """
        """
        if recursive is None:
            recursive = self.recursive
        dir_op_args  = dict(dir_name, recursive)
        dir_contents = self._prepare_dir_operation(** dir_op_args)
        for path in dir_contents:
            try:
                if os.path.isdir(path):
                    if not recursive:
                        message = "Cannot decrypt directory %s: \
                                recursive is set to False" % path
                        raise IsAdirectoryError(message)
                    self.encrypt_dir(dir_name = path, recipients = recipients)
                self._encrypt_file(path = path, recipients = recipients)
            except KeyError:
                print("Could not decrypt directory: ", dir_name)

    def encrypt_dir_list(self, dirs_to_encrypt: list):
        """
        """
        pass

if __name__ == "__main__":
    GPG()
