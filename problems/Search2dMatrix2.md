

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

### Example 1
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]] <br>
target = 5 <br>
Output: true <br>

https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg

```
package com.prep.medium;

public class Search2DMatrix2 {

	public static void main(String[] args) {
		
		int[][] matrix = {
				{1,4,7,11,15},
				{2,5,8,12,19},
				{3,6,9,16,22},
				{10,13,14,17,24},
				{18,21,23,26,30}};	//[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
		int target = 26;
		boolean stat = searchMatrix(matrix, target);
		System.out.println(stat);
	}
	
	public static boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        int i = 0, j = n-1;
        while(i < m && j >= 0) {
        	if(target == matrix[i][j]) {
        		return true;
        	} else if(target < matrix[i][j]) {
        		j--;
        	} else if(target > matrix[i][j]) {
        		i++;
        	}
        }
        return false;
    }
}

```
