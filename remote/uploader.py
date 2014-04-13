from abc import abstractclassmethod

__author__ = 'carlos'

import os

class Uploader:

    def __init__(self):
        self._listeners = dict()

    def upload(self, from_local_file, to_virtual_dir_path, listener):
        virtual_path = os.path.join(to_virtual_dir_path, os.path.basename(from_local_file))
        if virtual_path in self._listeners.keys():
            raise FileExistsError('Path %s already used' % (virtual_path, ))
        else:
            self._listeners[virtual_path] = listener
            self._upload(from_local_file, virtual_path)
        return virtual_path

    @abstractclassmethod
    def _upload(self, from_local_file, to_virtual_path):
        raise NotImplementedError('You must create an specific uploader that extends from this')

class UploaderManager:

    def get_free_uploader(self):
        return Uploader()