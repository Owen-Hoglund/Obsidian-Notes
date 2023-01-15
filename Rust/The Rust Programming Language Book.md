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
The option Enum encodes a very common scenario: A value could be something or it could be nothing. Rust doesn't have the null feature that many other languages have. Instead, Rust has an Enum called `Option<T>`, and it is defined as follows: 
```rust
enum Option<T> {
    None,
    Some(T),
}
```

- `<T>` is a generic Type Parameter.
- `Some<T>` variant can hold one piece of data of any type

Here are some examples of using `Option` values to hold types and string types:
```rust
let some_number = Some(5);
let some_char = Some('e');
let absent_number: Option<i32> = None;
```

- Type of `some_number` is `Option<i32>` 
- Type of `some_char` is `Option<char>`
- Type  of `absent_number` is `Option<i32>`
	- Rust requires us to annotate the overall `Option` type: the compiler can’t infer the type that the corresponding `Some` variant will hold by looking only at a `None` value.
- When we have a `Some` value, we know that a value is present and the value is held within the `Some`
- When we have a `None` value, it means we do not have a valid value

Why is this better? For one thing, the compiler will not allow us to use an `Option<T>` value as if it were definitely a valid value. For example, this code  wont compile because its trying to add an i8 to an `Option<i8>` 
```rust
    let x: i8 = 5;
    let y: Option<i8> = Some(5);
    let sum = x + y;
```

This solves one of the most common issues with Null - Assuming that something isn't null when it actually is.

## The match Control Flow Construct
`Match` is an extremely powerful control flow construct that allows you to compare a value against a series of patterns and then execute code based on which pattern matches. Patterns can be made up of literal values, variable names, wildcards, and many other things. 
### Patterns that bind to values
Another useful feature of match arms is that they can bind to the parts of the values that match the pattern. This is how we can extract values out of enum variants.

```rust
#[derive(Debug)]
enum UsState {
    Alabama,
    Alaska,
    // --snip--
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }
    }
}

fn main() {
    value_in_cents(Coin::Quarter(UsState::Alaska));
}

```

### Matching with Option

Say we have an option type that we want to get the T value out of, if it exists. We can handle `Option<T>` using `Match`. 

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
	match x {
		None => None,
		Some(i) => Some(i + 1),
	}
}
```

Note that all possibilities must be exhausted by the match arms or the code wont compile. There are a few ways to do this:
- you can name the **last** arm of a match function, which will handle all unspecified patterns, and bind the value to the name. 
-  `_` - this works the same way as the other option but is for values that we don't want to use.

## Concise Control Flow with if let
The `if let` syntax lets you combine `if` and `let` into a less verbose way to handle values that match one pattern while ignoring the rest.

The two following code blocks are equivalent:

	If config_max contains some value, bind that value to max, and execute the some(max) arm. Otherwise do nothing.
```rust
let config_max = Some(3u8);
match config_max {
	Some(max) => println!("The maximum is configured to be {}", max),
	_ => (),
}
```

	If config max has value execute code arm with max bound to value
```rust
let config_max = Some(3u8);
if let Some(max) = config_max {
	println!("The maximum is configured to be {}", max);
}
```


# Managing and Growing Projects with Packages, Crates, and Modules
---
Rust has a number of features that allow you to manage your code’s organization, including which details are exposed, which details are private, and what names are in each scope in your programs. These features, sometimes collectively referred to as the _module system_, include:

-   **Packages:** A Cargo feature that lets you build, test, and share crates
-   **Crates:** A tree of modules that produces a library or executable
-   **Modules** and **use:** Let you control the organization, scope, and privacy of paths
-   **Paths:** A way of naming an item, such as a struct, function, or module

## Packages and Crates
A _crate_ is the smallest amount of code that the Rust compiler considers at a time. Crates can contain modules, and the modules may be defined in other files that get compiled with the crate.

A crate can come in two forms:
- Binary Crate: programs you can compile to an executable that you can run, such as a command-line program or a server. Each must have a function called main that defines what happens when the executable runs. All the crates we've created so far have been binary  crates. 
- Library Crate: do not have a main function and they don't compile to an executable. Instead, they define functionality intended to be shared with multiple projects. Most of the time when Rustaceans say "crate" they mean a library crate and then use "crate" interchangeably with the general programming concept of a library. 

The *Crate Root* -  is a source file that the rust compiler starts from and makes up the root module of your crate. 

A *Package* - is a bundle of one or more crates that provides a set of functionality. A package contains a cargo.toml file that describes how to build those crates. Cargo is actually a package that contains the binary crate for the command-line tool you've been using to build your code. A package can contain as many binary crates as you like, but at most only one library crate. A package must contain at least one crate, whether that's a library or binary crate. 

## Defining Modules to Control Scope and Privacy

This section is already a boiled down cheat sheet version of larger topic, to condense it further would not do it justice, so I am going to copy it verbatim 

# Common Collections
---
## Storing Lists of Values with Vectors
I am already very familiar with vectors so this section will be sparse, if someone feels up to the task of condensing the topic even further than the rust language book does, feel free. I will note only things that seem important.

### Accessing Values via index vs .get()
One can directly access the values in a vector like `vec_example[i]`  or by `vec_example.get(i)`,
the difference being that `.get()` yields an `Option<&T>` which we can then use with `match`. Very useful if you don't know if there will be a value in that index!

### Mutating elements in a vector with a loop
Example given (note that we must let our iterator be a mutable reference  to the vector we wish to change, then for each element in the iterator we must **dereference it** in order to change the value):
```rust
fn main() {
    let mut v = vec![100, 32, 57];
    for i in &mut v {
        *i += 50;
    }
}
```

### Using an Enum to Store Multiple Types
One way to get around a vectors inability to store multiple types is to have a vector that contains enums. Because all variants of an enum are defined under the same enum type, we can store them all in a vector.

	Example:
```rust
enum SpreadsheetCell {
	Int(i32),
	Float(f64),
	Text(String),
}

let row = vec![
	SpreadsheetCell::Int(3),
	SpreadsheetCell::Text(String::from("blue")),
	SpreadsheetCell::Float(10.12),
];
```

## Storing Keys with Associated Values in Hash Maps
The type `HashMap<K,V>` stores a mapping of keys of type k to values of type v using a hashing function, which determines how it places these keys and values into memory.

### Adding a Key and Value Only if a key isn't present 

Hash maps have a special API for this called `entry` that takes the key you want to check as a parameter. The return value of the entry method is an enum called Entry that represents a value that might or might not exist. 
Then, the Enum Entry has a method on it called or_insert which returns a mutable reference to the value for the corresponding Entry key if that key exists, and if not, inserts the parameter as the new value for the key and returns a mutable reference to the new value. 
	example:
```rust
fn main() {
    use std::collections::HashMap;

    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);

	// insert entry if key doesnt exist otherwise returns mutable reference to the value
    scores.entry(String::from("Yellow")).or_insert(50);
    scores.entry(String::from("Blue")).or_insert(50);
    
    // Remove entry with key k
	scores.remove(&k);

    println!("{:?}", scores);
}
```

# Error Handling
---
Most languages do not differentiate between recoverable and irrecoverable errors, Rust does. In Rust, we have the type `Result<T, E>` for recoverable errors and the `panic!` macro that stops execution when the program encounters an unrecoverable error. 

## Unrecoverable Errors with Panic!

### Using a panic! backtrace
If a panic! call comes from a library because of a bug in our code instead of from our code calling the macro directly, we can set the `RUST_BACKTRACE` environment variable to get a backtrace of exactly what happened to cause the error. 
	in the console
```
$ RUST_BACKTRACE=1 cargo run
```

## Recoverable Errors with Result

Recall that the `Result` enum is defined as having two variants, `Ok`, and `Err`:
```rust
enum Result<T,E> {
	Ok(T),
	Err(E),
}
```
Where T and E are generic Type Parameters. 
- T represents the type of value that will be returned in a success case within the `Ok` variant
- E represents the type of error that will be returned in a failure case within the `Err` variant
- Because Result has generic type parameters, we can use the Result type and its defined functions in many situations

Example of a function that returns a `Result` type because the function could fail:
```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");
}
```

This may fail because the file doesn't exist in scope or because we don't have permission to open it, etc,. If we want to be able to take different actions depending on whether an error occurs we can use the `match` expression
```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the file: {:?}", error),
    };
}

```
In the above code, if the file is opened successfully, we assign `greeting_file` to the `file` contained within the `Ok(file)` variant of the enum Result.

### Matching on Different Errors
We can also match depending on the specific error that is returned by the `Result` 
```rust 
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => {
                panic!("Problem opening the file: {:?}", other_error);
            }
        },
    };
}

```

The above code does the following:
1. Assigns `greeting_file_result` to the result returned by passing "hello.txt" to the method `File::open()` which returns a `Result`
2. Matches the *variant* of `greeting_file_result` to two branch arms, `Ok(file)`, and `Err(error)`
	1. if `greeting_file_result` is the `Ok` variant, we assign the successfully opened `file` in `Ok(file)` to the variable `greeting_file`
	2. if `greeting_file_result` is the `Err` variant, we *match* the `error` in `Err(error)` to one of two branch arms `ErrorKind::NotFound`, or `other_error`
		1. `error == ErrorKind::NotFound` we *Create* the file specified, again *matching* the result of `File::Create` to `Ok` or `Err`, if there is no error we assign `greeting_file` to the newly created file, if not we panic and say 'Problem Creating the file: ', with the error contained in the err variant
		2. if the error is not a 'Not Found' error, we panic and print 'Problem Opening File' with the error contained in the error variant

The same logic can be equivalently coded below:
```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap_or_else(|error| {
        if error.kind() == ErrorKind::NotFound {
            File::create("hello.txt").unwrap_or_else(|error| {
                panic!("Problem creating the file: {:?}", error);
            })
        } else {
            panic!("Problem opening the file: {:?}", error);
        }
    });
}

```

For now, we ignore this as it relies upon #learnmore unwrap_or_else as well as closures, which are as yet uncovered

### Shortcuts for Panic on Error: unwrap and expect
Using match works well but is verbose and doesn't always communicate intent well. The `Result<T, E>` type has many helper methods to do specific tasks. 

#### unwrap
The unwrap method is a shortcut implemented just like the match expressions we used before. If `Result` value is the `Ok` variant, unwrap returns the value inside Ok, otherwise unwrap will call the error macro for us. 
```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap();
}

```

result if no such file exists
```
thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os {
code: 2, kind: NotFound, message: "No such file or directory" }',
src/main.rs:4:49

```

#### expect
Expect works identically to unwrap, with the only difference being that you can insert your own error message `.expect("Error Message goes here")`. 

### Propagating Errors

When a function's implementation calls something that might fail, instead of handling the error within the function itself, you can return the error to the calling code, where there might be more information or logic that dictates how the error should be handled than what you have available in the context of your code. This is called propagating errors. 

Below is an example of a function that reads a username from a file. if the file cant be read/doesn't exist, the function will return the errors to the code that called the function. 
```rust
#![allow(unused)]
fn main() {
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let username_file_result = File::open("hello.txt");

    let mut username_file = match username_file_result {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut username = String::new();

    match username_file.read_to_string(&mut username) {
        Ok(_) => Ok(username),
        Err(e) => Err(e),
    }
}
}

```
For a detailed explanation of this code see the original documentation. A very condensed version is below:
function attempts to open file
-> if fail return error code
-> if success attempt to read file contents to string username
-> if fail return error code
-> if success return string username


### A Shortcut for Propagating Errors: the ? Operator

The following code shows an implementation of the function with the same functionality but using the ? operator:
```rust
#![allow(unused)]
fn main() {
use std::fs::File;
use std::io;
use std::io::Read;

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?;
    let mut username = String::new();
    username_file.read_to_string(&mut username)?;
    Ok(username)
}
}
```

The `?` placed after a result is defined to work in almost the same way as the `match` expressions we defined to handle the `Result` values in the code [[The Rust Programming Language Book#Propagating Errors|above]]. There are some subtle differences that should be learned at some point but are not important and mostly revolve around the `from` function #learnmore .

The key takeaway is that the ? operator reduces boilerplate. We could even condense this further by chaining method calls immediately after the ?, as shown below:
```rust
#![allow(unused)]
fn main() {
use std::fs::File;
use std::io;
use std::io::Read;

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();

    File::open("hello.txt")?.read_to_string(&mut username)?;

    Ok(username)
}
}
```

This is all just to illustrate how we can use the ? operator to handle error propagation, however, it should be noted that there is an even more brief way of writing this function, as shown below, it simply does not give us the opportunity to explain what is going on behind the scenes
```rust
#![allow(unused)]
fn main() {
	use std::fs;
	use std::io;
	
	fn read_username_from_file() -> Result<String, io::Error> {
	    fs::read_to_string("hello.txt")
	}
}

```

This is because reading from a file to a string is a common enough operation that the standard library already implements it. Should it fail it will return the error type, if it succeeds it will return the Ok(string). 


#### Where the can ? be used

The ? operator can only be used in functions whose return type is compatible with the value the ? is used on. This is because the ? operator is defined to perform an early return of ta value out of the function, the same way we did with the `match` operator. 
Here's an example of the ? operator being used successfully, the code returns the last character of the first line of a string slice:
```rust
fn last_char_of_first_line(text: &str) -> Option<char> {
    text.lines().next()?.chars().last()
}

fn main() {
    assert_eq!(
        last_char_of_first_line("Hello, world\nHow are you today?"),
        Some('d')
    );

    assert_eq!(last_char_of_first_line(""), None);
    assert_eq!(last_char_of_first_line("\nhi"), None);
}
```
In short, we are returning an `Option<char>` because there might be a character there, but there may also not be. We read the first line of the string slice (IE we are splitting on \n, might be a valuable function to remember), now, this is all well and good, but if there are no lines in the slice, then we have a problem. If the slice has no lines, then the call to next() will return None, in which case we use ? to stop and return None from the function. If text is Not empty, next returns a Some value containing a string slice of the first line in text. Then the ? returns the string slice and we can call chars on that string slice to get an iterator of its characters. Its possible however that the first line is an empty string, so when we call last() it is an Option because we DO NOT KNOW if there are any characters in the line.

Note:
- You can use the ? Operator on a `Result` in a function that returns a `Result`
- You can use the ? Operator on an `Option` in a function that returns an `Option`
- You cannot use the ? Operator on a `Result` in a function that returns an `Option`
- You cannot use the ? Operator on an `Option` in a function that returns a `Result`
- In other words, you cannot mix and match

## To panic! or Not to panic!

Remember:
- When a code panics, there is **NO** way to recover
- When you return an `Err`, you can choose whether to attempt to recover or to panic

**Guidelines for Error Handling**
- You should panic when its possible that your code is in a *bad* state - something unexpected, as opposed to expected errors (bad user input, etc)
- Your code after this point relies upon not being in this bad state

# Generic Types, Traits, and Lifetimes
---
Every language has tools for effectively handling the duplication of concepts. In Rust, we have generics.

*Generics*: Abstract stand-ins for concrete types or other properties. 

We can express the behavior of generics or how they relate to other generics without knowing what will be in their place when compiling and running the code. 

## Removing Duplication by Extracting a Function

Generics allow us to replace specific types with a placeholder that represents multiple types to remove code duplication.

# Generic Data Types
We use generics to create definitions for items like function signatures or structs, which we can then use with many different concrete data types. Lets first look at how to define function , structs, enums, and methods using generics, then well discuss how generics affect code performance. \

## In Function Definitions

When defining a function that uses generics, we place the generics in the signature of the function where we would usually specify the data types of the parameters and return value. Doing so makes our code more flexible and provides more functionality to callers of our function while preventing code duplication.
If we have two functions that are identical in all form aside from the type of arguments, we can instead define the function with a generic `T`

Example of generic argument **NOTE: THIS CODE WILL NOT COMPILE UNLESS IT IMPLEMENTS PARTIALORD**
```rust
fn largest<T>(list: &[T]) -> &T {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {}", result);

    let char_list = vec!['y', 'm', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {}", result);
}
```


## In Struct Definitions

We can also define structs to use a generic type parameter in one or more fields using the <> syntax. 
```rust
struct Point<T> {
    x: T,
    y: T,
}

fn main() {
    let integer = Point { x: 5, y: 10 };
    let float = Point { x: 1.0, y: 4.0 };
}

```

Note that since we have only specified one generic type to define `Point<T>`, this definition says that the `Point<T>` struct is generic over some type T, and the fields x and y are *both* that type. If we wanted to have a struct with multiple generic types we would simply specify that by aliasing another generic as follows: `struct Point<T, U>` where `x: T, y: U`

## In Enum Definitions

As we did with structs, we can define enums to hold generic data types in their variants. Let's take another look at the `Option<T>` enum that the standard library provides:
```
enum Option<T>{
	Some(T),
	None,
}
```
As we now see more clearly, the `Option<T>` enum is generic over type T and has two variants, Some, which holds a value of type T and None, a variant that holds no value. 
Similarly, Result holds generics as well, a generic Ok(T) which represents some successful operation and its value, and Err(E) which represents a failed operation and its associated error 'value'.

## In Method Definitions 

We can also implement methods on structs and enums and use generic types in their definitions as well. 

> Generic method on a generic struct that returns a reference to the x value
```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

fn main() {
    let p = Point { x: 5, y: 10 };

    println!("p.x = {}", p.x());
}

```


One can also define implementations with a specified type on enums and structs that have generic types, in this way, only instances of the struct or enum with the given type taking the place of the generic have such methods defined on them.
For example
```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}

fn main() {
    let p = Point { x: 5, y: 10 };

    println!("p.x = {}", p.x());
}

```

only points with type f32 will have the method `distance_from_origin` implemented for them. 

Generic type parameters in a struct definition aren’t always the same as those you use in that same struct’s method signatures. Listing 10-11 uses the generic types `X1` and `Y1` for the `Point` struct and `X2` `Y2` for the `mixup` method signature to make the example clearer. The method creates a new `Point` instance with the `x` value from the `self` `Point` (of type `X1`) and the `y` value from the passed-in `Point` (of type `Y2`).

```rust
struct Point<X1, Y1> {
    x: X1,
    y: Y1,
}

impl<X1, Y1> Point<X1, Y1> {
    fn mixup<X2, Y2>(self, other: Point<X2, Y2>) -> Point<X1, Y2> {
        Point {
            x: self.x,
            y: other.y,
        }
    }
}

fn main() {
    let p1 = Point { x: 5, y: 10.4 };
    let p2 = Point { x: "Hello", y: 'c' };

    let p3 = p1.mixup(p2);

    println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
}

```

In `main`, we’ve defined a `Point` that has an `i32` for `x` (with value `5`) and an `f64` for `y` (with value `10.4`). The `p2` variable is a `Point` struct that has a string slice for `x` (with value `"Hello"`) and a `char` for `y` (with value `c`). Calling `mixup` on `p1` with the argument `p2` gives us `p3`, which will have an `i32` for `x`, because `x` came from `p1`. The `p3` variable will have a `char` for `y`, because `y` came from `p2`. The `println!` macro call will print `p3.x = 5, p3.y = c`.

The purpose of this example is to demonstrate a situation in which some generic parameters are declared with `impl` and some are declared with the method definition. Here, the generic parameters `X1` and `Y1` are declared after `impl` because they go with the struct definition. The generic parameters `X2` and `Y2` are declared after `fn mixup`, because they’re only relevant to the method.

# Traits: Defining Shared Behavior
A *trait* defines functionality a particular type has and can share with other types. We can use traits to define shared behavior in an abstract way. We can use *trait bounds* to specify that a generic type can be any type that has certain behavior. 

## Defining a trait

To define a trait, we use the `trait` keyword and then the traits name. We also set the trait to be either public or private, so that crates depending on this crate can or can not make use of the trait as well. Inside the curly brackets, we declare the method signatures that describe the behaviors of the types that implement this trait. 
Example:
```rust
pub trait Summary {
    fn summarize(&self) -> String;
}
```
In this example, the trait is called Summary, and summarize returns a string. Its arguments are just a reference to self, as that is all that we require for the example. Note that we do not include a definition of summarize, we only include its signature. This is because we will define the function individually for each type that implements this trait. 

## Implementing a Trait on a Type

Now that we have defined the signatures of a traits methods, it is time to implement those methods on a type. 
Say we want to implement summary on two structs, Tweet and NewsArticle, we can do it like this.
```rust
pub trait Summary {
    fn summarize(&self) -> String;
}

pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}

```

Now that summary has been implemented for tweet and NewsArticle, users can call the trait methods on instances of those types in the same way we call regular methods. The only difference is that the user must bring the trait into scope as well as the types. 

## Default Implementations

Sometimes it is useful to have default behavior for some or all of the methods in a trait instead of requiring implementations for all methods on every type. Then, as we implement the trait on a particular type, we can keep or override each methods default behavior. 
Here is an example of a default trait method definition:
```rust
pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}
impl Summary for NewsArticle {}
```
Now NewsArticle can use summarize and it will default to returning the string "Read more...".
Importantly, we do not have to change anything about our implementations of summarize anywhere else, for example with our implementation of summarize on Tweet. The reason is that the syntax for overriding a default implementation is the same as the syntax for implementing a trait method that doesn't have a default implementation. 

Default implementations can call other methods in the same trait, even if those other methods *don't* have a default implementation. In this way, a trait can provide a lot of useful functionality and only require implementers to specify a small part of it. 

For example, we could define summary trait to have a `summarize_author` method whose implementation is required, and then define a summarize method that has a default implementation that calls the `summarize_author` method
```rust
pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!("(Read more from {}...)", self.summarize_author())
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}

```

Now, if we call summarize on a tweet, it will print "(Read more from \[username\]...)".
Note that it is not possible to call the default implementation from an overriding implementation of the same method. 

## Traits as Parameters

Now we begin to see some really new functionality with traits that we don't get from normal methods or functions, we can use traits as parameters in function. In this way we can write functions that take all kinds of different types, so long as the type implements a given trait.
Example:
```rust
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```
Instead of a concrete type, we specify the `impl` keyword and the trait name. This parameter will accept any type that implements the specified trait. In the body we can call any methods on the the argument that come from the specified trait. 

## Trait Bound Syntax

The `impl trait` syntax shown in the code directly above works well for certain straightforward cases but is [[Definitions#Syntax Sugar|syntax sugar]] for a longer form known as a *trait bound*. It looks like this:
```rust
pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```
Again, this is equivalent to the code in the [[The Rust Programming Language Book#Traits as Parameters|Traits as Parameters]] section directly above. We place trait bounds with the declaration of the generic type parameter after a colon and inside angle brackets `<T: Summary>`, and then the actual argument that will be used in the definition inside the parentheses as we did before `(item: &T)`. 
- `impl trait` is more convenient and more concise in simple straightforward cases
- trait bound syntax can express more complexity in other cases

For example, we can have two parameters that implement `summary`. If Doing so with the `impl trait` syntax looks like this.
```rust
pub fn notify(item1: &impl Summary, item2: &impl Summary) {
```
using `impl trait` makes sense if we want to allow this function to have different types (as long as both implement `summary`). If we want to force both parameters to have the same type however, we must use the trait bound, as follows.
```rust
pub fn notify<T:Summary>(item1: &T, item2: &T){...}
```

## Specifying Multiple Trait Bounds with the + Syntax

WE can also specify more than one trait bound. Say we wanted notify to use display formatting as well as `summarize` on `item`: we specify in the `notify` definition that `item` must implement both `display` and `summary`. We can do this using the + syntax:
```rust
pub fn notify(item: &(impl Summary + Display)) {...}
```

Now the same using trait bounds on generic types:
```rust
pub fn notify<T: Summary + Display>(item: &T){...}
```

## Clearer Trait Bounds with where Clauses

using too many generic trait bounds has downsides: Each generic has its own trait bounds, so functions with multiple generic type parameters can contain lots of trait bound information between the functions name and its parameter list, making the function signature hard to read. For this reason, Rust has alternate syntax for speficying trait bounds inside a `where` clause after the function signature. So instead of writing this:
```rust
fn some_function<T: Display + Clone, U: Clone + Debug>(t:&T, u: &U) -> i32 {
...
}
```

we can use a `where` clause, like this:
```rust
fn som_function<T,U>(t: &T, u: &U) -> i32
where
	T: Display + Clone,
	U: Clone + Debug,
{
...
}
```
This is another example of [[Definitions#Syntax Sugar|syntax sugar]], it is functionally identical but easier to read. 

## Returning Types that implement Traits

We can also use the `impl trait` syntax in the return position to return a value of some type that implements a trait, as shown here:
```rust
fn returns_summarizable() -> impl Summary {
    Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    }
}
```
By using `impl Summary` in the return type, we specify that the `returns_summarizable` function returns some type that implements the `Summary` trait without naming the concrete type. In this case, `returns_summarizable` returns a tweet, but the code calling the function doesn't need to know that. 
**Note:** You can only use `impl Trait` if you're returning a single type. For example, this code **WILL NOT RUN**:
```rust
fn returns_summarizable(switch: bool) -> impl Summary {
    if switch {
        NewsArticle {
            headline: String::from(
                "Penguins win the Stanley Cup Championship!",
            ),
            location: String::from("Pittsburgh, PA, USA"),
            author: String::from("Iceburgh"),
            content: String::from(
                "The Pittsburgh Penguins once again are the best \
                 hockey team in the NHL.",
            ),
        }
    } else {
        Tweet {
            username: String::from("horse_ebooks"),
            content: String::from(
                "of course, as you probably already know, people",
            ),
            reply: false,
            retweet: false,
        }
    }
}
```
This is because the function could possibly be returning one of two types. 

## Using Trait Bounds to Conditionally Implement Methods

By using a train bound with an `impl` block that uses generic parameters, we can implement methods conditionally for types that implement the specified traits. For example, the type `Pair<T>` below always implements the `new` function to return a new instance of `Pair<T>`, But in the next `impl` block, `Pair<T>` only implements the `cmp_display` method if its inner type T implements the `PartialOrd` trait that enables comparison *and* the `Display` trait that enables printing. 

```rust
use std::fmt::Display;

struct Pair<T> {
    x: T,
    y: T,
}

impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

impl<T: Display + PartialOrd> Pair<T> {
    fn cmp_display(&self) {
        if self.x >= self.y {
            println!("The largest member is x = {}", self.x);
        } else {
            println!("The largest member is y = {}", self.y);
        }
    }
}
```

We can also conditionally implement a trait for any type that implements another trait. Implementations of a trait on any type that satisfies the trait bounds are called *Blanket Implementations* and are extensively used in the Rust standard library. For example, the standard library implements the `ToString` trait on any type that implements the `Display` trait. The `impl` block in the standard library look similar to this code:
```rust
impl<T: Display> ToString for T {
    // --snip--
}
```

## Summary
Traits and trait bounds let us write code that uses generic type parameters to reduce duplication but also specify to the compiler that we want the generic type to have particular behavior. The compiler can then use the trait bound information to check that all the concrete types used with our code provide the correct behavior. In dynamically typed languages, we would get an error at runtime if we called a method on a type which didn’t define the method. But Rust moves these errors to compile time so we’re forced to fix the problems before our code is even able to run. Additionally, we don’t have to write code that checks for behavior at runtime because we’ve already checked at compile time. Doing so improves performance without having to give up the flexibility of generics.


# Validating References with Lifetimes
---
Lifetimes are another kind of generic that we've already been using. Rather that ensuring that a type has the behavior we want, lifetimes ensure that references are valid as long as we need them to be.


## Preventing Dangling References with Lifetimes
The main aim of lifetimes is to prevent *dangling references*, which cause a program to reference data other than the data it's intended to reference. Consider the following code that **DOES NOT WORK**

```rust
fn main() {
    let r;

    {
        let x = 5;
        r = &x;
    }

    println!("r: {}", r); // Doesnt work
}
```
This doesn't work because we assigned r to be a reference to x, but x goes out of scope at the end of the block. In other words, the variable x "doesn't live long enough." But r is still valid outside of the scope, so if rust allowed this code to work, r would reference data that is no longer bound to a variable, unsafe! How does rest determine that this code is invalid? The Borrow Checker. 

## The Borrow Checker

The Rust compiler has a tool called the borrow checker that compares scopes to determine whether all borrows are valid. 
Example **DOES NOT WORK**:
```rust
fn main() {
    let r;                // ---------+-- 'a
                          //          |
    {                     //          |
        let x = 5;        // -+-- 'b  |
        r = &x;           //  |       |
    }                     // -+       |
                          //          |
    println!("r: {}", r); //          |
}                         // ---------+
```

Example **DOES WORK**:
```rust
fn main() {
    let x = 5;            // ----------+-- 'b
                          //           |
    let r = &x;           // --+-- 'a  |
                          //   |       |
    println!("r: {}", r); //   |       |
                          // --+       |
}                         // ----------+
```

## Generic Lifetimes in Functions
We'll write a function that returns the longer of two string slices. This function will take two slices and return a single slice. The following is an attempt to do so where the function returns a string slice (&str) which if one recalls is a reference to a str. 
Example **DOES NOT COMPILE**:
```
fn main() {
    let string1 = String::from("abcd");
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("The longest string is {}", result);
}

fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```
Output:
```
$ cargo run
   Compiling chapter10 v0.1.0 (file:///projects/chapter10)
error[E0106]: missing lifetime specifier
 --> src/main.rs:9:33
  |
9 | fn longest(x: &str, y: &str) -> &str {
  |               ----     ----     ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value, but the signature does not say whether it is borrowed from `x` or `y`
help: consider introducing a named lifetime parameter
  |
9 | fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
  |           ++++     ++          ++          ++

For more information about this error, try `rustc --explain E0106`.
error: could not compile `chapter10` due to previous error

```

The error text says that the return type needs a *generic lifetime parameter* on it because Rust can't tell whether the reference being returned refers to x or y. Unfortunately, we *cant* know, because we don't know what string slices are going to be passed in. 

## Lifetime Annotation Syntax
Lifetime annotations don’t change how long any of the references live. Rather, they describe the relationships of the lifetimes of multiple references to each other without affecting the lifetimes. Just as functions can accept any type when the signature specifies a generic type parameter, functions can accept references with any lifetime by specifying a generic lifetime parameter.

Lifetime annotations have a slightly unusual syntax: the names of lifetime parameters must start with an apostrophe (`'`) and are usually all lowercase and very short, like generic types. Most people use the name `'a` for the first lifetime annotation. We place lifetime parameter annotations after the `&` of a reference, using a space to separate the annotation from the reference's type.  

Examples:
```rust
&i32        // a reference
&'a i32     // a reference with an explicit lifetime
&'a mut i32 // a mutable reference with an explicit lifetime
```
 
One lifetime annotation by itself doesn't have much meaning, because the annotations are meant to tell Rust how generic lifetime parameters of multiple references relate to each other. let's examine how the lifetime annotations relate to each other in the context of the `longest` function. 

## Lifetime Annotations in Function Signatures
To use lifetime annotations in function signatures, we need to declare the generic _lifetime_ parameters inside angle brackets between the function name and the parameter list, just as we did with generic _type_ parameters.
We want the signature to express the following constraint: the returned reference will be valid as long as both the parameters are valid. This is the relationship between lifetimes of the parameters and the return value. We’ll name the lifetime `'a` and then add it to each reference.
```rust
//        ^lifetime parameters 
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

The function signature above tells the compiler that
> for some lifetime 'a, the function takes two parameters, *both* of which are string slices that live *at least* as long as lifetime 'a. 

Remember: The lifetime annotation **does not** affect the lifetimes of any values passed in or returned. Rather, we are specifying that the borrow checker should reject any values that don't adhere to these constraints. 

> When we pass concrete references to a function which uses lifetime annotations, the *concrete lifetime* that is substituted for `'a` is the part of the scope of x that overlaps with the scope of y. In other words, the generic lifetime `'a` will get the concrete lifetime that is equal to the smaller of the lifetimes of `x` and `y`. Because we’ve annotated the returned reference with the same lifetime parameter `'a`, the returned reference will also be valid for the length of the smaller of the lifetimes of `x` and `y`.

#finish 
# Writing Automated Tests
---
#finish
# An I/O Project
---
#finish 
# Function Language Features: Iterators and Closures
---

In this section we explore some of Rusts design that is influenced by *functional programming*. 
- *Closures* - A function-like construct you can store in a variable
- *Iterators* - A way of processing a series of elements
- how to use closures and iterators to improve the I/O project [[The Rust Programming Language Book#An I/O Project|here]]. 
- The performance of closures and iterators

## Closures: Anonymous Functions that Capture Their Environment
Rust’s closures are anonymous functions you can save in a variable or pass as arguments to other functions. You can create the closure in one place and then call the closure elsewhere to evaluate it in a different context. Unlike functions, closures can capture values from the scope in which they’re defined. We’ll demonstrate how these closure features allow for code reuse and behavior customization.


### Capturing the Environment with Closures
For the full context of the problem, see the full project [here](https://doc.rust-lang.org/book/ch13-01-closures.html#capturing-the-environment-with-closures).

Boiled Down: 
- Company gives away shirts sometimes to users
- If user profile has specified favorite color, they get the shirt in that color
- If user has NOT specified favorite color, they get the shirt that is most in stock

Our setup is shown below:
```rust
#[derive(Debug, PartialEq, Copy, Clone)]
enum ShirtColor {
    Red,
    Blue,
}

struct Inventory {
    shirts: Vec<ShirtColor>,
}

impl Inventory {
    fn giveaway(&self, user_preference: Option<ShirtColor>) -> ShirtColor {
        user_preference.unwrap_or_else(|| self.most_stocked())
    }

    fn most_stocked(&self) -> ShirtColor {
        let mut num_red = 0;
        let mut num_blue = 0;

        for color in &self.shirts {
            match color {
                ShirtColor::Red => num_red += 1,
                ShirtColor::Blue => num_blue += 1,
            }
        }
        if num_red > num_blue {
            ShirtColor::Red
        } else {
            ShirtColor::Blue
        }
    }
}

fn main() {
    let store = Inventory {
        shirts: vec![ShirtColor::Blue, ShirtColor::Red, ShirtColor::Blue],
    };

    let user_pref1 = Some(ShirtColor::Red);
    let giveaway1 = store.giveaway(user_pref1);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref1, giveaway1
    );

    let user_pref2 = None;
    let giveaway2 = store.giveaway(user_pref2);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref2, giveaway2
    );
}
```

Line by line reading of the code
1. We define an enum `ShirtColor` which has two variants, red and blue.
2. We define a struct `Inventory` which contains a vector of `shirtcolor`, each element represents a shirt in inventory.
3. We implement Inventory with two functions, `giveaway` and `most_stocked`
	1. giveaway takes `self` (type `inventory`) and `user_preference` (type `Option` `ShirtColor`) and if user preference has a value, returns it. If user preference has no value, it returns the color of shirt that is most stocked
	2. most stocked takes only `self` and counts the number of each color shirt, and returns the color that is most stocked 
3. Main 
	1. We create an instance of inventory and name it store, as well as put two blue and one red shirt in
	2. We create a user preference of Red wrapped in Some (which is an Option)
	3. We create a variable `giveaway` of type `ShirtColor` by calling the give away function on store
	4. We print the results (user with pref {} gets {}), red red
	5. We rinse and repeat these steps with a `user_preference` of None and get the result 'user with pref None gets blue'

In the `giveaway` method, we get the user preference as a parameter of type `Option<ShirtColor>` and call the `unwrap_or_else` method on `user_preference`. 
The  `unwrap_or_else` method on `Option<T>` is defined by the standard library. It takes one argument: a closure without any arguments that returns a value `T`, in this case `ShirtColor`. If `Option<T>` is Some, it returns the value within the Some, if the `Option<T>` is the None variant, it calls the closure and returns the value returned by the closure. 

We specify the closure expression `|| self.most_stocked()` as the argument to `unwrap_or_else`. This is a closure that takes no parameters itself (if the closure had parameters, they would appear between the two vertical bars). The body of the closure calls `self.most_stocked()`. We’re defining the closure here, and the implementation of `unwrap_or_else` will evaluate the closure later if the result is needed.

### Closure Type Inference and Annotation
- Closures don't usually require you to annotate the types of the parameters or the return value like `fn` functions do.
- Once a type has been inferred for a closure it cannot take another type

### Capturing References or Moving Ownership
Closures can capture values from their environment in three ways, which directly map to the three ways a function can take a parameter:  borrowing immutably, borrowing mutably, and taking ownership.

Example (closure that captures immutable reference to vector `list`):
```rust
fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

    let only_borrows = || println!("From closure: {:?}", list);

    println!("Before calling closure: {:?}", list);
    only_borrows();
    println!("After calling closure: {:?}", list);
}
```

Example (Closure that captures mutable reference to vector `list`):
```rust
fn main() {
    let mut list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

    let mut borrows_mutably = || list.push(7);

    borrows_mutably();
    println!("After calling closure: {:?}", list);
}
```

### Moving Captured Values Out of Closures and the `Fn` Traits

Once a closure has captured a reference or captured ownership of a value from the environment where the closure is defined (thus affecting what, if anything, is moved _into_ the closure), the code in the body of the closure defines what happens to the references or values when the closure is evaluated later (thus affecting what, if anything, is moved _out of_ the closure). A closure body can do any of the following: move a captured value out of the closure, mutate the captured value, neither move nor mutate the value, or capture nothing from the environment to begin with.

The way a closure captures and handles values from the environment affects which traits the closure implements, and traits are how functions and structs can specify what kinds of closures they can use. Closures will automatically implement one, two, or all three of these `Fn` traits, in an additive fashion, depending on how the closure’s body handles the values:

1.  `FnOnce` applies to closures that can be called once. All closures implement at least this trait, because all closures can be called. A closure that moves captured values out of its body will only implement `FnOnce` and none of the other `Fn` traits, because it can only be called once.
2.  `FnMut` applies to closures that don’t move captured values out of their body, but that might mutate the captured values. These closures can be called more than once.
3.  `Fn` applies to closures that don’t move captured values out of their body and that don’t mutate captured values, as well as closures that capture nothing from their environment. These closures can be called more than once without mutating their environment, which is important in cases such as calling a closure multiple times concurrently.

Lets have a look at the definition of the   



### Unwrap on `Option<T>`  yields either T or None, Unwrap on `Result` yields either Ok(T) or Err(E) 

#### If x is an Option. We can extract the value as follows
```rust
fn give_adult(drink: Option<&str>) {
    // Specify a course of action for each case.
    match drink {
        Some("lemonade") => println!("Yuck! Too sugary."),
        Some(inner)   => println!("{}? How nice.", inner),
        None          => println!("No drink? Oh well."),
    }
}
```
