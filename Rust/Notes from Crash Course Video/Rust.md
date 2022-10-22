# Rust
Rust is a low level language blending elements of other low level languages while still prioritizing usability. 
_______________________________________________________________________
___
## Types and Variables
Rust is a statically typed language, variable types must be known at compile time, however, the compiler can infer variable types based on the value and use of the variable.

- Primitive Types
	![[Pasted image 20220912160401.png]]
- Boolean (bool)
- Characters (char) 
- [[Tuples]]
- [[Arrays and Vectors]]
- [[Strings]] 

Example of infered and explicit typing, as well as finding the max of a type:![[Pasted image 20220912161119.png]]
_______________________________________________________________________
_______________________________________________________________________
## Conditionals in Rust
#### if/else
Rust if/else statements work much the same in Rust as in any other language. Example below
![[Pasted image 20220914103318.png]]
_______________________________________________________________________
_______________________________________________________________________
## Looping in Rust
### infinite loop
Rust has a built in infinite loop feature called `loop`. ![[Pasted image 20220914105148.png]]


### While loops
![[Pasted image 20220914105304.png]]

### For loops
![[Pasted image 20220914105516.png]]
___
_______________________________________________________________________
## Functions in Rust
![[Pasted image 20220914105736.png]]

Functions in rust take in arguments whose type has been declared in the function. You also must declare the return value. In the below argument `-> i32` is telling the compiler that this function will return a 32 bit integer. Also, in the argument below, the lack of a semicolon on `n1 + n2` tells the compiler that we will be returning `n1 + n2`. 

![[Pasted image 20220914105959.png]]
_______________________________________________________________________
_______________________________________________________________________
#### Closures 
#learnmore
_______________________________________________________________________
_______________________________________________________________________
## Pointers and References 
In Rust, it is important to know that, for non-primitive data types, if you assign another variable to a piece of data, the first variable will no longer hold that value. You'll need to use a reference (&) to point to the resource
For example, 
``let arr1 = [1,2,3]
`let arr2 = arr1`
will work, because arrays are Primitive. However, if we try to do this with a vector, then once we assign `arr2`, `arr1` will no longer hold data. 
_______________________________________________________________________
_______________________________________________________________________
## Structs and Impls
There are no classes in Rust, thus we recreate their functionality using structs and impls. 
#### Structs
![[Pasted image 20220914111742.png]]![[Pasted image 20220914111823.png]]

You can also make what are called tuple structs, which allow you to assign values to a struct without naming them, and then you simply access those attributes using dot syntax. 

```
struct Color(u8,u8,u8`
let example = mut Color(200, 0, 10)`
println!({} {} {}, color.0, color.1, color.2)
```

Will work as expected. 

#### Impls
We implement functions in impls
![[Pasted image 20220914112822.png]]
If we want to write functions that operate on the data contained in the struct itsself, we pass `&self` to the function, and then use dot syntax to access the variables. ![[Pasted image 20220914113149.png]]
_______________________________________________________________________
_______________________________________________________________________
## Enums
Enums are types which have a few definite values. 
```

```
}



# Modules in Rust
A module in rust is, in a rough sense, a named bunch of items. These can include functions, types, traits, other modules, etc,. It is similar to a directiory in the file system. 
![[Pasted image 20221003112457.png]]



## Defining a module in Rust
- Use the `mod` keyword
	- This is done directly in the source file ![[Pasted image 20221003112552.png]]
- Creating a file with a module name
	- ![[Pasted image 20221003112640.png]]
- Create a directory with a module name and mod.rs within
	- ![[Pasted image 20221003112834.png]]

## Visibility and Privacy
In Rust, almost everything is private by default. That means that items can only be accessed by the module where they are defined, or descendent modules. We need to use the `pub` keyword to make it accessible from anywhere their host module is accessible. 

## Accessing items from a module
- Use a full path eg `std::collections::HashMap::New();`
- Importing items with the use keyword 
	- eg `use std::collections::HashMap;`
	- Multiple import eg `use std::collections::{HashMap, LinkedList, BinaryHeap`
	- Renaming imports with `as` eg  `use std::collections::BinaryHeap as BH`
	- import everything with `*` though this is bad practice! eg `use std::collections::*;`
		- The exception to this being bad practice is when you are using a `prelude`. `prelude` is a Rust idiom which essentially means it is the 'prelude' to a library. A prelude includes everything you need to get started with a library quickly. 

# Slice
Slices let you reference a contiguous sequence of items in a collection without referencing the entire collection.
