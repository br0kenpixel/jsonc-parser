# jsonc-parser
Simple JSONC parser written in Python.

It's written in pure Python, requiring only one dependency: the json module (built into Python).
The module provides loads() and load() functions, much like the original json module.
Comments are first removed, then the "comment-less" JSON string is passed to json.loads()

This module also works with MicroPython, just make sure your build has the ujson module enabled.

Warning:
The code is absolutely NOT perfect, it may contain bugs and there's probably a better way to implement it.
My code is just a quick-and-dirty implementation that I needed for a project.
