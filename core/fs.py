
import os

class File:
    def __init__(self, name):
        self._name = name
        self._is_dir = False

    @property
    def name(self):
        return self._name

    @property
    def is_dir(self):
        return self._is_dir

    def __eq__(self, other):
        return other and self.name == other.name

    def __repr__(self):
        return self.name

    def __cmp__(self, other):
        return self.name.__cmp__(other.name)

class RemoteFile(File):
    """
    Represents a remote file. A remote file is a list of urls to other files.
    """
    def __init__(self, name):
        super(RemoteFile, self).__init__(name)
        self.file_pieces = []


class Directory(File):
    def __init__(self, name):
        super(Directory, self).__init__(name)
        self._is_dir = True
        self._files = dict()


class FS:
    def __init__(self):
        self.root = Directory('/')

    def add_file(self, from_local_file_path, to_remote_dir_path):
        if os.path.exists(from_local_file_path):
            local_stat_info = os.stat(from_local_file_path)
            if local_stat_info.st_size > 0:
                directory = self.get_guaranteed_dir(to_remote_dir_path)
            else:
                raise IOError('Invalid local file size: ' + local_stat_info.st_size)
        else:
            raise FileNotFoundError(from_local_file_path)

    def get_guaranteed_dir(self,to_remote_dir_path):
        print(os.path.split(to_remote_dir_path))
        return Directory('')