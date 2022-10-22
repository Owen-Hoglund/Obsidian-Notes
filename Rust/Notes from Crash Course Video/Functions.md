# Assert
## assert_eq
Asserts Equality of two elements by VALUE 
![[Pasted image 20220912172551.png]]
Yields:
![[Pasted image 20220912172627.png]]


# String Functions
In most of the functions below the string being modified is "Hello World", in cases where it is not, it is obvious or marked. 

## push_str (string)
Appends a string to a mutable string
![[Pasted image 20220912164351.png]]
![[Pasted image 20220912163928.png]]

## push (char)
Appends a character to the end of a mutable string


## len (string)
Returns the length of the string
![[Pasted image 20220912164241.png]]

## capacity (string)
Returns the number of characters the string can store
![[Pasted image 20220912164835.png]]

## is_empty (string)
checks if empty string
![[Pasted image 20220912165144.png]]

## contains (string)
checks if a string contains a given string as a substring
In example below the string is "Hello World"
![[Pasted image 20220912165757.png]]\
![[Pasted image 20220912165816.png]]

## replace (string)
 Replaces a given substring with a given string (Any occurence of such substrings)
![[Pasted image 20220912170534.png]]

## split_whitespace (string)
creates an iterator of substrings from a given string seperated by spaces
![[Pasted image 20220912170816.png]]

## with_capacity (string)
creates a string with a given character capacity![[Pasted image 20220912172215.png]]

# Array Functions
## slice (array)
returns a slice of an array. 
![[Pasted image 20220914102202.png]]

## len (array)
example.len() returns the number of elements in the array

# Vector Functions

# Misc Functions
## size_of_val 
size_of_val takes a pointer to a variable and returns the number of bytes that variable occupies in memory



