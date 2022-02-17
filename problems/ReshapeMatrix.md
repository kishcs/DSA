
## Reshape the Matrix

https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg
![https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg]()

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
<pre>
public int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length;
		int n = mat[0].length;
		
		if(m*n != r*c) {
			return mat;
		}
		
		int i = 0;
		int [] tmp = new int[m*n];
		for (int[] row : mat) {
			for (int col : row) {
				tmp[i++] = col;
			}
		}
		/*
		 * for (int j : tmp) { System.out.print(j+" "); } System.out.println();
		 */
		
		int[][] res = new int[r][c];
		i = 0;
		for (int j = 0; j < res.length; j++) {
			for (int k = 0; k < res[j].length; k++) {
				res[j][k] = tmp[i++];
			}
		}
		
		return res;
    }
</pre>
