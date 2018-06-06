import contextlib
import os

with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')

# This is equivalent to:

try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass