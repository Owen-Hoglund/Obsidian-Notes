declared like: 
```python
class Employee:
	def __init__ (self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
```
instantiated as object like:
```python
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Cory', 'Quirk', 75000)
```
you can also set attributes of a class like this, but it's more lines:
```python
emp_1.first = 'Corey'
#etc
```

```python
class Employee:
	#...
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

```
the first argument (here, `self`) is the class itself. this type of method can only be called with an instance of the class.

with the `@classmethod` attribute, [[Methods - Class, Static, and Regular#Class Methods]] allow you to define some action(s) related to a class. the convention for the first arguments of these methods is `cls` as opposed to `self`. these methods can be called *without* an instance of the class, as with `@staticmethod`
	
(note: `@` denotes a **decorator** in Python, as with JavaScript. in Java, `@` denotes an **annotation** - similar, but know the difference)
