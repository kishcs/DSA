Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

### Example 1
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], <br>
target = 3 <br>
Output: true <br>
https://assets.leetcode.com/uploads/2020/10/05/mat.jpg
```
package com.prep.medium;

public class Search2DMatrix {
	public static void main(String[] args) {
		int[][] matrix = {
				{1,3,5,7},
				{10,11,16,20},
				{23,30,34,60}};	//[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
		int target = 11;
		boolean stat = searchMatrix(matrix, target);
		System.out.println(stat);
	}
	
	public static boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        int targetRow = -1;
        for (int i = 0; i < m; i++) {
			    if(target >= matrix[i][0] && target <= matrix[i][n-1]) {
				    targetRow = i;
				    break;
			    }
		    }
        if(targetRow == -1) {
        	return false;
        }
        for (int i = 0; i < n; i++) {
			    if(target == matrix[targetRow][i]) {
				    return true;
			    }
		    }
		    return false;
      }
  }

```
