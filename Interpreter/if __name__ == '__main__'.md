`__name__` is a variable set by the Python interpreter when a file runs.

When the interpreter runs a module, the `__name__` variable will be set as `__main__` if that module being run is the main program.

If the code is importing another module, then `__name__` will be set to *that* module's name.

```python
# Python file one module

print("File one __name__ is set to: {}" .format(__name__))
```

### resources:
- [freecodecamp](https://www.freecodecamp.org/news/if-name-main-python-example/) 
- [Corey Schafer tutorial](https://youtu.be/sugvnHA7ElY)
