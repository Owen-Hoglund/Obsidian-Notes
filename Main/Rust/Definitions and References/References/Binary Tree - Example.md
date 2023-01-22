## Binary Tree Implementation
```rust
type ChildNode<T> = Option<Box<TreeNode<T>>>;

struct BinaryTree<T> {
	head: Option<TreeNode<T>>
}

struct TreeNode<T> {
	left: ChildNode<T>
	right: ChildNode<T>>,
	value: type
}

enum Op<T> {
	Add,
	Sub,
	Div,
	Mul,
	Id(T)
}

impl TreeNode<i32> {
	pub fn new(op: Op<i32>, left: TreeNode<i32>, right TreeNode<i32>) -> self{
		TreeNode::<i32> {
			op: op, left: Some(Box::new(left)), right: Some(Box::new(right))
		}
	}
	pub fn find(node: TreeNode<i32>, value: i32) -> TreeNode {
		if node.value == value{ return node}
		else if node.left != None { return find(node, value)}
		else if node.left != None { return find(node, value)}
		else {return None}
	}
}

```