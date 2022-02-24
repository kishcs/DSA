Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

### Example 1:
Input: s = "()" <br>
Output: true

### Example 2:
Input: s = "()[]{}" <br>
Output: true

### Example 3:
Input: s = "(]" <br>
Output: false

### Constraints:
- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.

```
public static boolean isValid(String s) {
		char[] data = s.toCharArray();
		ArrayList<Character> stack = new ArrayList<>();
		//Stack<Character> st = new Stack<>(); //we can use stack class directly
		int open = 0;
		for (char c : data) {
			if(c == '(' || c == '[' || c == '{') {
				stack.add(0, c);
				open++;
			} else if(c == ')') { 
				open--;
				if(stack.size() > 0 && stack.remove(0) != '(') {
					return false;
				}
			} else if(c == ']' ) { 
				open--;
				if(stack.size() > 0 && stack.remove(0) != '[') {
					return false;
				}
			} else if(c == '}') { 
				open--;
				if(stack.size() > 0 && stack.remove(0) != '{') {
					return false;
				}
			}
		}
		if(stack.size() > 0) {
			return false;
		}
		if(open < 0) {
			return false;
		}
		return true;
	}
```
