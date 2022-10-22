The following are notes from [The Rust Programminghttps://doc.rust-lang.org/book/foreword.html Language](https://doc.rust-lang.org/book/foreword.html), a guide freely available from the designers of Rust. For more detail, one should obviously refer to the source. Here will be a distillation of the most important parts, in my opinion. 

# Common Programming Concepts
---
# Variables and Mutability
---
**Mutability**
- by default, variables are immutable. 
- Prefacing a variable declaration with `mut` sets the variable to be mutable. 

**Constants**: 
- can never be mutable. 
- declared with the `const` keyword. 
- type *must* be annotated at declaration
- can be declared in any scope
- can *only* be set to a constant expression, *not* the result of a value that could only be computed at runtime.

**Shadowing**
One can declare a new variable with the same name as a previously declared variable. This is called *shadowing*. The second variable is what the compiler sees until that second variable is either shadowed again or until the scope ends. 
```rust
fn main() {
	let x = 5; 
	{ 
		let x = x * 2; 
		println!("The value of x in the inner scope is: {x}"); 
	}
	println!("The value of x is: {x}");
	}
```
This is particularly valuable in the case in which we wish to change the type of a variable, which is not otherwise possible. 

# Data Types
---
Reminder: Rust is a *statically typed* language -> it must know the types of all variables at compile time. While the compiler is very good at inferring type when it needs to, invariably there will be times in which there are multiple *possible* types, in which case one must add a type annotation. 

## **Scalar Types**
A scalar type represents a single value. Rust supports integers, floating point, Booleans, and characters.

**Integer Types**

| length  | Signed | Unsigned | Example    |     | Number literals |
| ------- | ------ | -------- |:---------- | --- | --------------- |
| 8-bit   | i8     | u8       | 98_222     |     | Decimal         |
| 16-bit  | i16    | u16      | 0xff       |     | Hex             |
| 32-bit  | i32    | u32      | 0o77       |     | Octal           |
| 64-bit  | i64    | u64      | 0b111_0000 |     | Binary          |
| 128-bit | i128   | u128     | b'A'       |     | Byte (u8 only)  |
| arch    | isize  | usize    |            |     |                 |

When choosing between various integer types, the main concern is avoiding integer overflow.

**Floating Point Types**
Rust has two primitive types for floating point numbers, f32 and f64, the latter of which is the default. 

**Numeric Operations**
Rust supports ``+-/*%``. Other mathematical operations are in crates. 

**The Boolean Type**
`let t: bool = true`
Booleans work the same in rust as in most languages

**The Character Type**
`char` is Rusts most primitive alphabetic type. Character literals are specified with single quotes, as opposed to string literals which are specified with double quotes


## Compound Types
Compound types can group multiple values into one type. In Rust there are two primitive compound types: tuples and arrays. 

### Tuple
A [[Tuple]] groups together a number of values with a variety of types into one compound type.
- Fixed Length, once declared, one cannot grow or shrink in size.
- Elements do not have to share a type `let tup: (i32, f64, u8) = (500, 6.3, 1)` is a valid declaration. 
- Accessed using the dot ` . ` operator ex `tup.1` or by destructuring it as follows
```rust
fn main() { 
let tup = (500, 6.4, 1); 
let (x, y, z) = tup; 
println!("The value of y is: {y}"); 
}
```
- The tuple without any values has a special name, *unit*, written `()` and represent and empty value **or** empty return type
### Array
An [[Array]] is another collection of values
- Fixed Length, once declared, one cannot grow or shrink in size.
- Elements **must** share the same type
- Data is allocated on the *stack* not the *heap*
- Elements are accessed by indexing `[i]`
- Invalid indices are **not accessible**. Rust will panic and throw a runtime error. 

# Functions
---
- Rust code uses snake case as the conventional style for function and variable names. 
- It does *not* matter where you define your functions, as long as they are defined in a scope that is visible to the caller
## Parameters and Return Values
- Type must be declared in definition
- If a function returns a value, we declare the type with `->`
- 
## Statements and Expressions
- Function bodies are made a series of statements optionally ending in an expression.
- Expressions evaluate to a value
- Statements are instructions that perform an action and do not return a value
- Expressions do not include ending semicolons

# Control Flow
---
While control flow in Rust works much as you would expect it to in any other language, there are a few things we can do with it that are worth mentioning

### Using `if` in a `let` Statement
Because `if` is an expression that, we can use it on the right side of a `let` statement to assign the outcome to a variable. 
```rust 
fn main() { 
let condition = true; 
let number = if condition { 5 } else { 6 }; 
println!("The value of number is: {number}"); }
```
One can easily see the use case in this scenario for assigning variables based on state. Important to note, that the type on each [[Definitions|arm]] must be the same so that the compiler can infer what sort of variable it is allocating data for.

## Loops
Rust has three kinds of loops: `loop`, `while`, `for`. 
- `break` tells Rust to stop whatever it is doing and **end** the looping it is currently doing. 
- `continue` tells Rust to stop the *current* iteration of the loop and continue with the loops next iteration. For example, `continue` in `for x in (0..10)` when x = 3 will just start the loop block with x = 4

## loop
`loop` tells Rust to just continue executing a block of code repeatedly until you tell it explicitly to stop. 

### Returning Values from Loops
One use of a loop is to retry an operation you know might fail. You might also need to pass the result of that operation out of the loop to the rest of your code. To do this you can add the value you want returned after the `break` expression you use to stop the loop. 
`break counter * 2;`

### Loop Labels to Disambiguate Between Multiple Loops

If you have loops within loops, `break` and `continue` apply to the innermost loop at that point. You can optionally specify a _loop label_ on a loop that we can then use with `break` or `continue` to specify that those keywords apply to the labeled loop instead of the innermost loop. Loop labels must begin with a single quote. Here’s an example with two nested loops:
```rust
fn main() { 
	let mut count = 0;
		'counting_up: loop { 
			println!("count = {count}"); 
			let mut remaining = 10; 
			loop { println!("remaining = {remaining}");
				if remaining == 9 { 
				
				break; 
				} 
				if count == 2 { 
				break 'counting_up; 
				} 
				remaining -= 1; 
		} 
		count += 1;
} 
println!("End count = {count}"); }

```
## For and While
One safely assumes that for and while loops work much the same as any other language
- While repeats according to a conditional
- for loops over elements in a collection

# Understanding Ownership
---
## The Stack and the Heap

The stack stores values in the order it gets that and removes the values in the opposite order (First in Last Out). Adding new data is called  *pushing onto the stack* and removing data is called *popping off the stack*. All data on the stack must have a known, fixed size.

Data with an *unknown* size at compile time or a size that might change must be stored on the heap instead. 

Pushing to the stack is faster than allocating on the heap because the allocator never has to search for a place to store new data; that location is always at the top of the stack. 

## Ownership Rules
- Each value in Rust has an owner
- There can be only one owner of a value at a time
- When the owner foes out of scope, the value will be dropped
- Assigning a value to another variable moves it.

## References and Borrowing
If we wish to pass a value to a function without giving away ownership, or without giving away and then getting ownership back, we pass a reference to that value instead. 

### Mutable References
If we wish for a function to modify a value without giving away ownership, we:
1. first must declare that value as mutable.
2. Pass in a mutable reference to that value into our function. 
```rust
fn main(){
	let mut s = String::from("Hello");
	change(&mut s);
}

fn change(some_string: &mut String){
	some_string.push_str(",  World");
}
```
Note that a reference to a mutable value is **NOT** mutable, we must explicitly create a *mutable* reference to that mutable value. 

**Restriction:** A value which has a mutable reference cant have any other references to it. This means both mutable and immutable. This prevents data races at compile time.  There are a few caveats to this rule, however. 
- If immutable references are declared **and** used for the last time *before* a mutable reference is declared, that is ok, because the immutable references have reach the end of their [[The Rust Programming Language Book#Generic Types, Traits, and Lifetimes|lifetimes]]. 

## The Slice Type
Slices let you reference a contiguous sequence of elements in a collection rather than the whole collection. A slice is a kind of reference so it does not have ownership. 
### String Slices
A String slice is a reference to part of a `String`. In this way we can use part or all of a string without directly accessing it. 
Notes:
- String Literals are Slices
- A function that can take a string slice as an argument can also take a String reference through dereference coercion 

# Using Structs to Structure Related Data
---
## Defining an Instantiating Structs
A struct is similar to a tuple, in that both hold multiple related values. Like tuples, a struct can hold values of different types. Unlike tuples, in a struct one names each piece of data so its clear what the values mean. 

Example of Struct definition:
```rust 
struct User {
	active: bool,
	username: String,
	email: String,
	sign_in_count: u64,
	}
}
```

To use a struct after we've defined it, we create an instance of that struct by specifying concrete values for each of the fields. We create an instance by stating the name of the struct and then add curly brackets containing `key:value` pairs. To access a specific value from a struct we use dot notation. `user1.email`, for example. 

Example of Struct instantiation:
```rust
let user1 = User { 
	email: String::from("someone@example.com"), 
	username: String::from("someusername123"), 
	active: true, 
	sign_in_count: 1, 
	};
```

It is important to note that if we want to be able to mutate any value of a struct the entire instance of the struct must be declared as mutable. Rust does not allow you to choose some fields to be mutable and others to not be. 

#### Creating an struct builder
While this does not introduce new functionality, it is worth noting that to save yourself trouble and time, it is useful to create a function to build new instances of a struct. 

Example of Struct Builder
```rust 
fn build_user(email: String, username: String) -> User { 
User { 
	email: email, 
	username: username, 
	active: true, 
	sign_in_count: 1, 
	} // Note that since this does not end in a semicolon, we are returning User
}
```


## Method Syntax
Methods are similar to function in that we declare them with the `fn` keyword and a name. They can have parameters and a return value, and they contain some code that's run when the method is called from somewhere else. Unlike functions, methods are defined within the context of a struct (or enum or a trait object). Their first parameter is always `self`, which represents the instance of the struct the method is being called on. 

### Defining Methods

Methods are defined within an implement block that is associated with a struct. For example, if our struct is called Rectangle, we can define methods on that struct as follows:
```rust
impl Rectangle {
	fn area(&self) ->u32 {
	self.width * self.height
	}
}
```

Notes:
1. We use `&self` because we do not want to take ownership
2. If we wanted to change the fields of the instance we would use `&mut self`
3. Using `self` on its own is rare, and usually is only done when the instance is being transformed into something else and shouldn't be used again. (One can imagine if we had a struct for caterpillar, and it had a method to metamorphose into a butterfly struct, we wouldn't want to still have a caterpillar struct lying around)

# Enums and Pattern Matching
---
## Defining an Enum
Where structs give you a way of grouping together related fields and data, like a Rectangle with its width and height, enums give you a way of saying a value is one of a possible set of values. For example, we may want to say that rectangle is one of a set of possible shapes that also includes Circle and Triangle. To do this, Rust allows us to encode these possibilities as an enum. 

Here is an example of an enum that has two variants, where one variant will have an associated string, and the other will have four associated integers
```rust
enum IpAddr { 
	V4(u8, u8, u8, u8), 
	V6(String), 
	} 
	let home = IpAddr::V4(127, 0, 0, 1); 
	let loopback = IpAddr::V6(String::from("::1"));
```

Here's another example of a struct that takes a variety of different types in its variants:
```rust
enum Message { 
	Quit, 
	Move { x: i32, y: i32 }, 
	Write(String), 
	ChangeColor(i32, i32, i32), 
	}
```

Like structs, we can implement methods on enums the same way. 
```rust
impl Message {
	fn call(&self) {
		// method body would be defined here
	}
}
```

## The Option Enum and Its Advantages Over Null Values
The option Enum encodes a very common scenario: A value could be something or it could be nothing. Rust doesn't have the null feature that many other languages have. Instead, Rust has an Enum called Option\<T>, and it is defined as follows: 
```rust
enum Option<T> {
    None,
    Some(T),
}
```