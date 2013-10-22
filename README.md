# python file system better assertion

An assertion lib for `the` to assert file system stuff.

# API
* `basename(dir)`. assert basename of a path.
* `dirname(dir)`. assert dirname of a path.
* `extname(file)`. assert file extension
* `path`. assert path exists
* `file`. assert it a file
* `dir`. assert it a dir
* `mount`. assert it a mount point
* `absolute_path`. assert it an absolute path
* `readable`. assert readable.
* `writable`. assert writable.
* `executable` assert executable

# Usage:
```python
from the import the
import thefs

the.use(thefs)

the("/a/b/c.md").should.have.basename("c.md")
the("/a/b/c.md").should.have.dirname("/a/b")
the("/a/b/c.md").should.have.extname("/a/b")

the("/a/b/c.md").should.be.a.path
the("/a/b/c.md").should.be.a.file
the("/a/b/c.md").should.be.a.dir
the("/a/b/c.md").should.be.a.link
the("/a/b/c.md").should.be.a.mount
the("/a/b/c.md").should.be.an.absolute_path

the("/a/b/c.md").should.be.readable
the("/a/b/c.md").should.be.writable
the("/a/b/c.md").should.be.executable
```
