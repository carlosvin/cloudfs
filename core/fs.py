
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
    Represents a remote file.
    """
    def __init__(self, name, url):
        super(RemoteFile, self).__init__(name)
        self._url = url
        # TODO to manage piece of files self.file_pieces = [] A remote file is a list of urls to other files.

class Directory(File):
    def __init__(self, name):
        super(Directory, self).__init__(name)
        self._is_dir = True
        self._files = dict()

    def get_guaranteed_dir(self, split_path):
        sub_dir_name = split_path[0]
        if not sub_dir_name in self._files.keys():
            sub_dir = Directory(sub_dir_name)
            self._files[sub_dir_name] = Directory(sub_dir_name)
        else:
            sub_dir = self._files[sub_dir_name]

        if len(split_path) == 1:
            return sub_dir.get_guaranteed_dir(split_path[1:-1])
        else:
            return sub_dir

    def add_local_file(self,from_local_file_path):
        os.path.basename(from_local_file_path)

class FS:
    def __init__(self):
        self._size = 0
        self.root = Directory('/')

    def add_file(self, from_local_file_path, to_remote_dir_path):
        if os.path.exists(from_local_file_path):
            local_stat_info = os.stat(from_local_file_path)
            if local_stat_info.st_size > 0:
                directory = self.get_guaranteed_dir(to_remote_dir_path)
                directory.add_local_file(from_local_file_path)
                self._size += local_stat_info.st_size
            else:
                raise IOError('Invalid local file size: ' + local_stat_info.st_size)
        else:
            raise FileNotFoundError(from_local_file_path)

    def get_guaranteed_dir(self,to_remote_dir_path):
        tmp_path = os.path.normpath(to_remote_dir_path)
        return self.root.get_guaranteed_dir(tmp_path.split(os.path.sep))

    @property
    def size(self):
        return self._size
