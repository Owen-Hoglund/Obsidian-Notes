```Python
class Employee:
	num_of_emps  = 0
	raise_amount = 1.04
	#-------------------------------------------------------------
	# This method initializes an instance of the class
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.'  + last + '@company.com'
		Employee.num_of_emps += 1 
	#-------------------------------------------------------------
	# This method gives an alternative method of intantiating the
	# class with a string, rather than inline input as normal such
	# as something like emp = Employee(john, hamm, 100000). Class
	# methods can be used without an instance of the class because
	# they call upon the class itself, not attributes of an 
	# instance of the class
	
	@classmethod
	def from_string(cls, emp_str)
		#The line below takes a string of employee info, parses it
		first, last, pay = emp_str.split('-')
		# The line below creates an instance of the
		# class employee, and returns it
		return cls(first, last, pay)
	#-------------------------------------------------------------
	# This method sets the raise rate
	@classmethod 
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount
	#-------------------------------------------------------------
	# This method tells you if a given day was a work day
	@staticmethod
	def is_work_day(day):
		if day.weekday() == 5 or f day.weekday() == 6:
			return False
		return True
	#note that this function relies upon another library, but it
	# is not important to the content of this reference

	#-------------------------------------------------------------
	# This method gives an employee a raise according to the raise
	# amount
	def apply_raise(self):
		self.pay = int(self.pay * Employee.raise_amount)
#-----------------------------------------------------------------
	# This Class is a subclass of Employee
class Developer(Employee):
	raise_amt = 1.10
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang
#-----------------------------------------------------------------
	# This Class is a subclass of Employee
class Manager(employee):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees
	#-------------------------------------------------------------
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)
	#-------------------------------------------------------------
	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
	#-------------------------------------------------------------
	def print(self):
		for emp in self.employees:
			print('--->', emp.fullname())
```