## iter 
iter takes a collection and returns an iterator. Say we want to iterate through all the values in a vector without worrying about how many elements are in the vector, and without accessing the values specifically (ie example[1] etc). We can do the following:
```
fn main() {

    let ex: [i32; 5] = [1,4,6,3,78];
    let result= ex.iter();
    for i in result{
        println!("element: {}", i)
    }
}
```
When run, this yields:
```
element: 1 
element: 4 
element: 6 
element: 3 
element: 78
```

In python this is done automatically. Now, what can we do with it?
## Map
Map transforms one iterator into another by means of an argument. The same as a map works in mathematics from one set to another. Say that we want to alter each element of a vector the same way, for example, by adding 1 to each element, we can do that with a map. We first use iter to turn the vector into an iterator. Lets alter the code above. 
``` Rust
fn main() {
    let ex: [i32; 5] = [1,4,6,3,78];
    let result= ex.iter().map(|x| x+1);
    for i in result{
        println!("element: {}", i)
    }
}
```
When run, this yields:
``` Rust 
element: 2 
element: 5 
element: 7 
element: 4 
element: 79
```

One can see how useful this can be, not only for compact code, but also, if for example you want a function to return a modified version of an array or vector. Let us now examine collect. 

## Collect
Ok, now we have an iterator, and furthermore, we have altered that iterator using a map. Now we want to keep the product in a more useful, more permanent form. Maybe that form is a string of characters, maybe its a vector, maybe its an array. Collect is here to help. 
