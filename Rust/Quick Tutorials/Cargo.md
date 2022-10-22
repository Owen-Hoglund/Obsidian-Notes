# Quick Tutorial
Cargo is the [Rust](https://www.rust-lang.org/) [_package manager_](https://doc.rust-lang.org/cargo/appendix/glossary.html#package-manager ""package manager" (glossary entry)"). Cargo downloads your Rust [package](https://doc.rust-lang.org/cargo/appendix/glossary.html#package ""package" (glossary entry)")'s dependencies, compiles your packages, makes distributable packages, and uploads them to [crates.io](https://crates.io/), the Rust community’s [_package registry_](https://doc.rust-lang.org/cargo/appendix/glossary.html#package-registry ""package registry" (glossary entry)").

## **[Getting Started](https://doc.rust-lang.org/cargo/getting-started/index.html)**

### Starting a new package with Cargo
Use `cargo new`:
`$ cargo new hello_world`
Cargo defaults to making a binary program. You can use the suffix `--lib` instead 

### To compile a project
Use: `cargo build`
### To compile and run a project
Use: `cargo run`