There are two types of strings
- Primitive str = Immutable fixed-length string somewhere in memory
- String = Growable, heap allocated data structure - Use when you need to modify or own string data

Useful functions for strings:
- [[Functions#push_str string|push_str]] - Appends a string to the end of a mutable string
- [[Functions#push |push]] - Appends a character to the end of a mutable string
- [[Functions#len string|len]] - Returns the length of a given string
- [[Functions#Capacity string|capacity]] - Returns the number of characters the string can store
- [[Functions#is_empty (string)|is_empty]] - Returns a boolean telling if it is an empty string
- [[Functions#contains (string)|contains]] - Returns a boolean indicating if a given string is a substring of the string we are checking
- [[Functions#replace (string)|replace]] - Replaces a given substring with a given string (Any occurence of such substrings)
- [[Functions#split_whitespace string|split_whitespace]] - Creates an iterator with substrings from a given string separated by spaces
- 



