# Module Tutorial
A clear tutorial on modules in Rust can be found [here](https://www.sheshbabu.com/posts/rust-module-system/).  We will include a boiled down version here. 

Lets assume the following file structure: ![[Pasted image 20221003121154.png]]
### Importing config.rs in main.rs
- To do this simply use `mod config` in main.rs. This declares config as a submodule. 

### To call the print_health_route function defined in `routes/health_route.rs`
To accomplish this we need to do a few things
- Create a file `routes/mod.rs` and declare the routes submodule in `main.rs`
	- `mod routes` within `main.rs`
- Declare the `health_route` submodule in `routes/mod.rs`
	- `pub mod health_routes` within `mod.rs`
- Make the functions within `health_route.rs` public
