To use the unittest module we need to first create a new file for our unit testing class. The naming convention is that for a file "exampleFile" the new file will be titled "test_exampleFile". 

- import unittest
- create new class that inherits from unittest.TestCase
	-  `class TestCalc(unittest.testcase)`
- to run test
	- run 'python -m unittest test_exampleFile.py'
	- or, more easily, at the end of the test file write
		- `if __name__ == '__main__: \n unittest.main()'`
		- You can now run `python test_exampleFile.py`
- All test method names must start with test_
- 