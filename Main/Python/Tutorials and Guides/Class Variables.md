Class Variables are variables that are the same across every instance of the class. They can only be accessed through the class itself or an instance of a class. However, they do not exist as attributes of the instances, only as attributes of the class. They can be accessed through instances of the class only through inheritance, as explained below. 

For example
``` Python
class Employee:
	raise_amount = 1.04
	# The Following two methods will work
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		
	def apply_raise(self):
		self.pay = int(self.pay * Employee.raise_amount)
		
	# This method will NOT work
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


print(Employee.raise_amount) # yields 1.04
print(emp_1.raise_amount) # yields 1.04
print(emp_2.raise_amount) # yields 1.04
```

On the last few lines, it is important to understand that when you try to access an attribute on an instance, python will first check if that instance contains that attribute, if it doesnt, then python will check if the class, or any class that it inherits from contains that attribute. So at the end of the above example 
```Python
print(emp_1.raise_amount) 
```

`emp_1` doesnt actually have the attribute `raise_amount`, they are accessing the classes `raise_amount` attribute. 

An easy way to see what attributes an instance has is to use the `.__dict__` function. `.__dict__`  Will list all of the attributes available to the instance. 

You can set class variables by accessing them directly within code or through an instance
```Python 
#This will set the raise amount for the class and EVERY instance of the class to 1.05
Employee.raise_amount = 1.05
#This will set the raise amount for ONLY this instance to 1.06
emp_1.raise_amount = 1.06
```
In fact, the last line in the above example gives us an unexpected result. It actually creates the attribute `raise_amount` _within_ the instances [[namespace]], rather than changing the attribute it inherits from the class. This can be useful if for example you really want to change the value of an instance for one or some particular instance(s) of a class. 

Now, say that we want to have some class variable that will keep track of how many instances of the class there are, we can do something like:
```Python
class Employee:
	raise_amount = 1.04
	num_of_emps = 0
	# The Following two methods will work
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		
	def apply_raise(self):
		self.pay = int(self.pay * Employee.raise_amount)
		
	# This method will NOT work
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
```

We want this to change every time that we add an employee, so a natural place to put this will be in the `___init___` method, since it runs every time you instantiate an instance of a class
```Python
def __init__(self, first, last, pay):
	self.first = first
	self.last = last
	self.pay = pay
	self.email = first + '.'  + last + '@company.com'
	Employee.num_of_emps += 1 #Note that this is accessed through the CLASS not the instance
```

Next we will look at [[Methods - Class, Static, and Regular|Class Methods]]
