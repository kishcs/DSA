## Pascal's Triange
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif

### Example 1
Input: numRows = 5 <br>
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

```
	public static List<List<Integer>> generate(int numRows) {
		List<List<Integer>> data = new ArrayList<>();
		List<Integer> inner = new ArrayList<>();
		inner.add(1);
		data.add(inner);

		for (int i = 1; i < numRows; i++) {
			inner = new ArrayList<>();
			inner.add(1);
			for (int j = 1; j < i; j++) {
				int val = data.get(i-1).get(j-1) + data.get(i-1).get(j);
				inner.add(val);
			}
			inner.add(1);
			data.add(inner);
		}

		return data;
	}
```
