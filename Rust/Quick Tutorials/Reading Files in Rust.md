# File Stream in Rust
To begin, youll want to employ some `use` declarations
```
use std::fs::File
use std::io::prelude::*
```

## The following is for Reading and Writing text files

## Reading a file 
### To open a file:
```
let mut example_file = File::open("example.txt").expect("Can't Open File")
```

### To put the  entire contents of the file into a variable:
```
let mut contents = String::new();
example_file.read_to_string(&mut contents).expect("Can't Read File")
```

From here, you can modify or utilize the file in any way that you would do so with a string. 

## Writing to a file
To create and write to a file:
```
let mut example_new_file = File::create("output.txt").expect("Error message");
example_new_file.write_all(b"This will be in the file")
```