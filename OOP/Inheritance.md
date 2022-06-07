---
aliases: [Subclasses]
---
# Inheritance and Subclasses
Class inheritance is useful because we can create subclasses adn inherit all the functionality of the parent class. In this section we will be continuing to use our [[Method Code Reference Full Code|EmployeeClass]] as an example.

In this example we will be creating the subclasses `manager` and `developer`. 

Example
```Python
class Developer(Employee):
	pass
```
In the example above, we can now use the class Developer _exactly_ the same as we could with the class `Employee`.
for example

``` Python
Dev1 = Developer("john", "Waters", 100000)
```

Will work despite `Developer` not having any \_\_init\_\_ function because python will _attempt_ to find it, fail to find it, and then it will try to go "up the chain of inheritance" to determine if there is a constructor function which is inherited by `Developer`, and it will find that YES, Developer inherits its constructor from `Employee`, and it will happily instantiate as `Employee` does. 


There is a really helpful function to help visualize inheritance.
```Python
print(help((Developer))
```
This will print out a lot of useful information, the first being the *Method Resolution Order* which tells you how the language will search for methods when called upon. In our case, it will be 
```
Method Resolution Order
	Developer
	Employee
	builtins.object
```
Where the last bit is a something every python class inherits from - object. It will then list all the methods it inherits from `Employee` as well as other data descriptors and attributes

Now lets customize the subclass a little bit. For example, lets change the `Raise_amount` for the `Developers` subclass:
```Python
class Developer(Employee):
	raise_amt = 1.10

dev1.apply_raise()
```
In the code above there are two important things to note
	1. The Developer class is inheriting the `apply_raise` method from `Employee`
	2. Despite inheriting that method, it uses the `raise_amt` that we assigned as a class variable in `Developer`, *not* the one from `Employee` 

Sometimes we want to initiate our subclasses with more information than our parent class can handle. For example, if we wanted to pass in a programming language that a developer knows, we are going to need a new init method for the subclass. We want it to be similar to the method we inherit, however it needs one more argument. Before we begin though, we want to make sure that we do this in the cleanest way, and that means not repeating logic that we have already coded, so we are going to let the init method from Employee handle the first three arguments and then let Developer handle the last method
```Python
def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

Dev1 = Developer("john", "Waters", 100000, "java")

```
Where `super().__init__(self, first last, pay)` passes first, last, pay, to the parent class's init method, and then we handle `prog_lang` ourselves. 


Lets go ahead and create another subclass `Manager`

```Python
class Manager(employee):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)
	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
	def print(self):
		for emp in self.employees:
			print('--->', emp.fullname())
```
#review (default arguments, passing mutable data types as arguments)

**Useful tools:**
- print(isinstance(instance, class)) will tell you if an intance is an instance of a class
- print(issubclass(Class, Class)) will tell you if a given class is a subclass of another class

In the next Section we will discuss [[Special Methods]]





---------------------------------------------------------
```Python
class Developer(Employee):
	raise_amt = 1.10
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(employee):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)
	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
	def print(self):
		for emp in self.employees:
			print('--->', emp.fullname())

```