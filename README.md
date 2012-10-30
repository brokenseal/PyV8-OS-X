PyV8-OS-X
=========
[![endorse](http://api.coderwall.com/brokenseal/endorsecount.png)](http://coderwall.com/brokenseal)

This is a binary distribution of [pyv8](http://code.google.com/p/pyv8/),
for use with Python >= 2.6.1 and OS X >= 10.6.4, packaged up for easy
installation. PyV8 allows Python to access the Google V8 Javascript engine.

The original source of `_PyV8.so` is from
[Martin Loewis at uni-potsdam](http://www.dcl.hpi.uni-potsdam.de/home/loewis/pyv8/).

```
$ otool -L _PyV8.so
_PyV8.so:
        /usr/lib/libstdc++.6.dylib (compatibility version 7.0.0, current version 7.9.0)
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 125.2.0)
```

Dr. Loewis used the following software to build it:
* pyv8 1.0-dev r282
* Boost 1.44.0
* V8 2.4.6
* Python 2.6.1
* Mac OS X 10.6.4


Installation
------------

A convenient way to install is using pip. You can install within a
[virtualenv](http://pypi.python.org/pypi/virtualenv/), if you'd like.

To install with pip directly from this git repo, use the command:
```
pip install -e git://github.com/brokenseal/PyV8-OS-X#egg=pyv8
```
(see the "Git Read-Only" URL above for the path).

You can then ``from pyv8 import PyV8`` in python and proceed with the examples
shown on the pyv8 website.
