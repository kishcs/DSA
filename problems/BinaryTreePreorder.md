Given the root of a binary tree, return the preorder traversal of its nodes' values.

### Example 1:
Input: root = [1,null,2,3] <br>
Output: [1,2,3]

### Example 2:
Input: root = [] <br>
Output: []

### Example 3:
Input: root = [1] <br>
Output: [1]

### Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

```
public static List<Integer> preorderTraversal(TreeNode root) {
		List<Integer> res = new ArrayList<>();
		if(root == null) {
			return res;
		}
		
		res.add(root.val);
		
		if(root.left != null) {
			res.addAll(preorderTraversal(root.left));
		}
		if(root.right != null) {
			res.addAll(preorderTraversal(root.right));
		}
		return res;
    }
	
	public static List<Integer> preorder(TreeNode root) {
		Stack<TreeNode> s = new Stack<>();
		List<Integer> res = new ArrayList<>();
		if(root == null) {
			return res;
		}
		s.push(root);
		while(!s.isEmpty()) {
			TreeNode tn = s.pop();
			if(tn != null) {
				res.add(tn.val);
				if(tn.right != null) s.push(tn.right);
				if(tn.left != null) s.push(tn.left);
			}
		}
		
		return res;
    }
```
