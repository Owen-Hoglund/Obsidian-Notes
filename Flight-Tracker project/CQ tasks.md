4 May 22:
Input Validation
--------------------------------------------------
take an instance of the flightGroupClass
 pass that class as an argument to an input_validator function
Check each attribute of the class to ensure that it meets standards for input format
If it passes return True if it Fails return False and give some reason why/allow for correction?
Airport CSV Cleaning 
--------------------------------------------------
use SQLite to Query airport.csv
SELECT Airports 
FROM airport.csv
WHERE iata_code NOT Null
AND type == Large Airport (? use your judgement on this one, might not be necessary to filter)

4 May 22 (further detail):
# Notes on input/argument validation

Here are the guidelines on the validation requirements. They are not ordered in the order that you should accomplish them as some of the validations require other attributes to be validated in order to validate themselves.
I recommend you tackle them in this order:

email -> stayRange -> dateLowerBound -> dateUpperBound -> destination -> groupOrigins

I think this order will be not only easiest to hardest, but you will develop some methods that will prove themselves reusable in the ensuing work.
I am realizing that this is turning out to be quite a lot more work than I expected it to be, so I will for sure be helping out on this and, as always, don't feel obligated to do any work at all. 


## flightGroup
Within the flightGroup class, there are 6 arguments that get passed in during initialization that need to be validated before they get used anywhere else in the program in order to maintain a clean program:
  
1. destination 
	- The destination where all travelers within the group are going
	- [ ] Must be a valid string
		- [ ] No more than 3 letters
		- [ ] Must not include anything but letters
		- [ ] Must be in all caps
			- [ ] if letters are not capitalized convert them then proceed with the rest of the validation
	- [ ] Must be included in our csv file containing all the airports we are going to work with
	- [ ] Must not appear in the groupOrigins list (remember that that list is a tuple so it wont be as simple as just saying X not in Y, where X is destination and Y is the list of origins). I can give you more information on this later if you dont pick up what I'm laying down
2. Upper and lower bound of travel dates
	- This is the range people are interested in travelling during. So for instance, a group might be interested in travelling between august and december
	- Look into the library datetime, I used it in exampleGroupGenerator.py to generate random dates but its full of functionality. I used it to generate a random date within the next year and then I made my own function to convert it from the datetime class to a string, you can look at that for inspiration but I dont think you can reverse engineer it to go backwards. 

	- dateLowerBound
		- The beginning of the range of dates the group is interested in travelling
		- [ ] Must be a string in the format YYYY-MM-DD
		- [ ] Must be at least one day in the future (current date + one day)
		- [ ] Must be within a year of the current date
		- [ ] MM must be a valid entry
			- [ ] Not greater than 12
			- [ ] Not less than 1
			- [ ] Months 1-9 must be formatted with a prefixed zero (sept = 09, sept != 9)
		- [ ] DD Must be a valid entry
			- [ ] Not greater than the number of days in the associated month
			- [ ] Not less than zero
			- [ ] Same prefix zero rule as months (01, 02, etc,.)

	- dateUpperBound
		- The end of the range of dates the group is interested in travelling
		- [ ] Must be a string in the format YYYY-MM-DD
		- [ ] Must be at least dateLowerBound + the upper bound of the stayRange
		- [ ] MM must be a valid entry
			- [ ] Not greater than 12
			- [ ] Not less than 1
			- [ ] Months 1-9 must be formatted with a prefixed zero (sept = 09, sept != 9)
		- [ ] DD Must be a valid entry
			- [ ] Not greater than the number of days in the associated month
			- [ ] Not less than zero
			- [ ] Same prefix zero rule as months (01, 02, etc,.)
3. stayRange
	- This is the length of trip the group is interested in. For example, 7-14 days
	- [ ] Must be a tuple of integers
		- [ ] The first index (\[0\])  must be the lesser of the two integers
		- [ ] The second index (\[1\]) must be the greater of the two integers

4. email
	- Obviously this must be an email address
	- [ ] format "example@domain.com"
		- I am confident that you can copy paste someone elses work to ensure that an email address is valid, surely someone has done this and posted it
5. groupOrigins
	- This is by far the most complex attribute in the class. It is a list of tuples. 
	- The tuples are in the format (String, Int) where the string is an iata airport code, and the int represents the number of people travelling from that airport.
		- for example, if part of a group has three people travelling from Minneapolis, the tuple will be ('MSP', 3)
		- In practice the list will look like this
			- \[ ('MSP' , 3) , ('YYZ' , 4) , ......... (BOS , 3)\]
	- [ ] Must be of type list
	- [ ] There must be at least 2 elements in the list
	- [ ] each element must be of type tuple
		- [ ] each tuple must contain exactly 2 elements
		- [ ] those two elements must be a string and an int, in that order