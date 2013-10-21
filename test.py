import unittest
import thefs
from the import *
the.use(thefs)


class TestTheFs(unittest.TestCase):
    def setUp(self):
        self.r = self.assertRaises
        self.true = self.assertTrue

    def test_basename(self):
        self.true(expect("/a/b/c.md").to.have.basename("c.md"))
        with self.r(AssertionError):
            self.true(expect("/a/b/c.md").to.have.basename("what"))

    def test_dirname(self):
        self.true(expect("/a/b/c.md").to.have.dirname("/a/b"))
        with self.r(AssertionError):
            self.true(expect("/a/b/c.md").to.have.dirname("/a/b/"))

    def test_extname(self):
        self.true(expect("/a/b/c.md").to.have.extname(".md"))
        with self.r(AssertionError):
            self.true(expect("/a/b/c.md").to.have.extname("md"))

    def test_path(self):
        self.true(expect(".").to.be.path)
        with self.r(AssertionError):
            expect(".....s...soooooooooooooo").to.be.path

    def test_file(self):
        self.true(expect("./test.py").to.be.a.file)
        with self.r(AssertionError):
            expect(".").to.be.a.file

    def test_dir(self):
        self.true(expect(".").to.be.a.dir)
        with self.r(AssertionError):
            expect("./readme.md").to.be.a.dir

    def test_absolute_path(self):
        self.true(expect("/tmp/readme.md").to.be.an.absolute_path)
        with self.r(AssertionError):
            expect("./readme.md").to.be.an.absolute_path

    def test_readable(self):
        self.true(expect("./test.py").to.be.readable)
        with self.r(AssertionError):
            expect("/a/b/c.md").to.be.readable

    def test_mount(self): pass

    def test_writable(self): pass

    def test_executable(self): pass


if __name__ == '__main__':
    unittest.main()
