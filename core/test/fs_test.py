__author__ = 'carlos'

import unittest
from core.fs import FS, Directory, File
import os

class FsTestCase(unittest.TestCase):

    def test_initial_fs(self):
        filesystem = FS()
        self.assertEqual(filesystem.root, Directory('/') )

    def test_fs_size(self):
        filesystem = FS()
        dir_path = os.path.dirname(__file__)
        init_file = os.path.join(dir_path, '__init__.py')
        this_file = __file__

        init_file_size = os.stat(init_file).st_size
        this_file_size = os.stat(this_file).st_size

        filesystem.add_file(from_local_file_path=init_file, to_remote_dir_path=dir_path)
        self.assertEquals(init_file_size, filesystem.size)

        filesystem.add_file(from_local_file_path=this_file, to_remote_dir_path=dir_path)
        self.assertEquals(init_file_size + this_file_size, filesystem.size)


if __name__ == '__main__':
    unittest.main()
