import gnupg
import os


class GPG(gnupg.GPG):
    """
    A class that adds directory encryption and decryption to 
    gnupg.GPG
    """
    def __init__(
        self,
        recursive: bool = True,
        recipients: list = None,
        no_overwrite: bool = True   # when encrypting files, make a copy first. preserve directory structure
    ):
        super().__init__()
        self.recursive = recursive
        self.recipients = recipients

    def __str__(self):
        return self.__doc__.replace('  ', '').replace('\n', '')

    def _prepare_dir_operation(
        self,
        dir_name: str,
        recursive: bool = None,
    ) -> list:
        if recursive is None:
            recursive = self.recursive
        make_path = lambda i: os.path.join(dir_name, i)
        dir_contents = tuple(map(make_path, os.listdir(dir_name)))
        if not recursive or (recursive is None and not self.recursive):
            is_a_file = lambda i: os.path.isfile(i)
            dir_contents = tuple(filter(is_a_file, dir_contents))
        return dir_contents

    # change recipients type to str or iterable
    def _encrypt_file(
        self,
        path: str,
        recipients: str = None,
        within_recursive_call: bool = False,
        verbose: int = 1,
    ):
        # if within recursive call is true, don't raise error
        if within_recursive_call and os.path.isdir(path):
            return
        self._check_path_exists(path)
        try:
            with open(path, "rb") as f:
                an_encryption = self.encrypt_file(f, recipients=recipients, output=path)
                print(f.name, "Encrypted? ", an_encryption.ok)
        except IsADirectoryError:
            print("Cannot encrypt, %s is not a file" % path)

    def _check_path_exists(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError("Cannot find ", path)

    def _decrypt_file(
        self,
        path: str,
        passphrase: str,
        within_recursive_call: bool = False,
        verbose: int = 1,
    ):
        if within_recursive_call and os.path.isdir(path):
            return
        self._check_path_exists(path)
        try:
            with open(path, "rb") as f:
                a_decryption = self.decrypt_file(f, passphrase=passphrase, output=path)
                print(f.name, "Decrypted? ", a_decryption.ok)
        except IsADirectoryError:
            print("Cannot decrypt, %s is not a file" % path)

    def encrypt_dir(
        self,
        dir_name: str,
        recipients: list = None,
        recursive: bool = True,
        verbose: int = 1,
    ):
        """
        Encrypt all files in directory [dir_name], recursive set to
        True by default
        """
        if recipients is None:
            if self.recipients is None:
                e = "GPG.recipients is not set"
                raise TypeError(e)
            recipients = self.recipients
        dir_op_args = dict(dir_name=dir_name, recursive=recursive)
        dir_contents = self._prepare_dir_operation(**dir_op_args)
        for path in dir_contents:
            try:
                if os.path.isdir(path):
                    if not recursive:
                        message = (
                            "Cannot encrypt directory %s: \
                                recursive is set to False"
                            % path
                        )
                        raise IsADirectoryError(message)
                    self.encrypt_dir(
                        dir_name=path, recipients=recipients, recursive=recursive
                    )
                    print("Encrypted: ", path)
                encrypt_file_map = {
                    "path": path,
                    "recipients": recipients,
                    "within_recursive_call": recursive,
                }
                self._encrypt_file(**encrypt_file_map)
                if verbose == 1:
                    print("Encrypted: ", path)
            except KeyError:
                print("Could not encrypt directory: ", dir_name)

    def decrypt_dir(
        self,
        dir_name: str,
        passphrase: str,
        recursive: bool = None,
        verbose: bool = False,
    ):
        """
        Decrypt all files in directory [dir_name], recursive set to
        True by default
        """
        if recursive is None:
            recursive = self.recursive
        dir_op_args = dict(dir_name=dir_name, recursive=recursive)
        dir_contents = self._prepare_dir_operation(**dir_op_args)
        for path in dir_contents:
            try:
                if os.path.isdir(path):
                    if not recursive:
                        message = (
                            "Cannot decrypt directory %s: \
                                recursive is set to False"
                            % path
                        )
                        raise IsADirectoryError(message)
                    self.decrypt_dir(
                        dir_name=path, passphrase=passphrase, recursive=recursive
                    )
                    print("Decrypted: ", dir_name)
                decrypt_file_map = {
                    "path": path,
                    "passphrase": passphrase,
                    "within_recursive_call": recursive,
                }
                self._decrypt_file(**decrypt_file_map)
                if verbose == 1:
                    print("Decrypted: ", path)
            except KeyError:
                print("Could not decrypt directory: ", dir_name)

    def encrypt_dir_list(self, dirs_to_encrypt: list):
        """"""
        pass

    def decrypt_dir_list(self, dirs_to_decrypt: list):
        """"""
        pass


if __name__ == "__main__":
    GPG()
