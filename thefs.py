"""
An assertion lib for `the` to assert file system stuff.

usage:

from the import the
import thefs

the.use(thefs)

the("/Users/wenjun.yan").should.be.a.path
the("/tmp/test.rb").should.be.executable
"""

import os


def basename(self, other):
    return self._check(os.path.basename(self.obj) == other,
                       "Basename of {} is {}.".format(self.obj, other),
                       "Basename of {} is not {}.".format(self.obj, other))


def dirname(self, other):
    return self._check(os.path.dirname(self.obj) == other,
                       "Dirname of {} is {}.".format(self.obj, other),
                       "Dirname of {} is not {}.".format(self.obj, other))


def extname(self, other):
    return self._check(os.path.splitext(self.obj)[1] == other,
                       "Extname of {} is {}.".format(self.obj, other),
                       "Extname of {} is not {}.".format(self.obj, other))


def path(self):
    return self._check(os.path.exists(self.obj),
                       self.obj + " exist.",
                       self.obj + " do not exist.", )


def file(self):
    return self._check(os.path.isfile(self.obj),
                       self.obj + " is a file",
                       self.obj + " is a not file")


def dir(self):
    return self._check(os.path.isdir(self.obj),
                       self.obj + " is a directory",
                       self.obj + " is not a directory")


def link(self):
    return self._check(os.path.islink(self.obj),
                       self.obj + " is a link",
                       self.obj + " is not a link")


def mount(self):
    return self._check(os.path.ismount(self.obj),
                       self.obj + " is a mount point",
                       self.obj + " is not a mount point")


def absolute_path(self):
    return self._check(os.path.isabs(self.obj),
                       self.obj + " is an absolute path",
                       self.obj + " is not an absolute path")


def readable(self):
    return self._check(os.access(self.obj, os.R_OK),
                       self.obj + " is readable",
                       self.obj + " is not readable")


def writable(self):
    return self._check(os.access(self.obj, os.W_OK),
                       self.obj + " is writable",
                       self.obj + " is not writable")


def executable(self):
    return self._check(os.access(self.obj, os.X_OK),
                       self.obj + " is executable",
                       self.obj + " is not executable")


API = [basename, dirname, extname, path, file, dir,
       link, mount, absolute_path, readable, writable, executable]
