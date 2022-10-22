# Enumerate
Tool that wraps the result of an iterator and returns each element as part of a tuple that counts index.

# [Derive(Debug)]

adding `[Derive(Debug)]` directly above a struct definition lets us do things like 
```rust
#[derive(Debug)] 
struct Rectangle { 
	width: u32,
	height: u32, 
	} 
fn main() {
	let rect1 = Rectangle { width: 30, height: 50, }; 
	println!("rect1 is {:?}", rect1); }

```

Now we can easily print out the values of a struct as they are at a given moment.

# Debug
