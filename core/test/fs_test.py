__author__ = 'carlos'

import unittest
from core.fs import FS, Directory, File


class FsTestCase(unittest.TestCase):

    def test_initial_fs(self):
        filesystem = FS()
        print(filesystem.root)
        self.assertEqual(filesystem.root, Directory('/') )

    def test_fs_size(self):
        filesystem = FS()
        filesystem.add_file(from_local_file_path=__file__, to_remote_dir_path='/foo/bar/a/b/c')
        filesystem.size()


if __name__ == '__main__':
    unittest.main()
