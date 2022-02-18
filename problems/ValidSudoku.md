Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

### Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png

```
package com.prep;

import java.util.HashMap;

public class ValidSudoku {

	public static void main(String[] args) {
		char[][] board = {
				{'.','.','4','.','.','.','6','3','.'},
				{'.','.','.','.','.','.','.','.','.'},
				{'5','.','.','.','.','.','.','9','.'},
				{'.','.','.','5','6','.','.','.','.'},
				{'4','.','3','.','.','.','.','.','1'},
				{'.','.','.','7','.','.','.','.','.'},
				{'.','.','.','1','.','.','.','.','.'},
				{'.','.','.','.','.','.','.','.','.'},
				{'8','.','.','3','.','.','.','.','.'}
		};
		/*
				 [['.','.','.','9','.','.','.','.','.'],
				 ['.','.','.','.','.','.','.','.','.'],
				 ['.','.','3','.','.','.','.','.','1'],
				 ['.','.','.','.','.','.','.','.','.'],
				 ['1','.','.','.','.','.','3','.','.'],
				 ['.','.','.','.','2','.','6','.','.'],
				 ['.','9','.','.','.','.','.','7','.'],
				 ['.','.','.','.','.','.','.','.','.'],
				 ['8','.','.','8','.','.','.','.','.']]
		 */
		/*{
				{'8','3','.','.','7','.','.','.','.'},
				{'6','.','.','1','9','5','.','.','.'},
				{'.','9','8','.','.','.','.','6','.'},
				{'8','.','.','.','6','.','.','.','3'},
				{'4','.','.','8','.','3','.','.','1'},
				{'7','.','.','.','2','.','.','.','6'},
				{'.','6','.','.','.','.','2','8','.'},
				{'.','.','.','4','1','9','.','.','5'},
				{'.','.','.','.','8','.','.','7','9'}
				};*/

		boolean stat = isValidSudoku2(board);
		System.out.println(stat);
	}

	public static boolean isValidSudoku(char[][] board) {
		//(1, 1), (1, 4), (1, 7)
		//(4, 1), (4, 4), (4, 7)
		//(7, 1), (7, 4), (7, 7)
		/*
		  (0, 0), (0, 1), (0, 2)
		  (1, 0), (1, 1), (1, 2)
		  (2, 0), (2, 1), (2, 2)
		 */
		HashMap<Integer, Integer> map = null;
		//For all 3x3 matrix
		for (int p = 1; p <= 7; p+=3) {
			for (int q = 1; q <= 7; q+=3) {
				int m = p;
				int n = q;
				map = new HashMap<>();
				for (int i = m-1; i <= m+1; i++) {
					for (int j = n-1; j <= n+1; j++) {
						char element = board[i][j];
						if(element != '.') {
							int elem = Integer.parseInt(element+"");
							map.put(elem, map.getOrDefault(elem, 0) + 1);
							if(map.get(elem) > 1) {
								return false;
							}
						}
					}
				}
				//System.out.println(map);
			}
		}
		//System.out.println('FOR ROWS');
		//For all rows
		for (int i = 0; i <= 8; i++) {
			map = new HashMap<>();
			for (int j = 0; j <= 8; j++) {
				char element = board[i][j];
				if(element != '.') {
					int elem = Integer.parseInt(element+"");
					map.put(elem, map.getOrDefault(elem, 0) + 1);
					if(map.get(elem) > 1) {
						return false;
					}
				}
			}
			//System.out.println('row:'+i + ', map:'+map);
		}

		//For all columns
		for (int i = 0; i <= 8; i++) {
			map = new HashMap<>();
			for (int j = 0; j <= 8; j++) {
				char element = board[j][i];
				if(element != '.') {
					int elem = Integer.parseInt(element+"");
					map.put(elem, map.getOrDefault(elem, 0) + 1);
					if(map.get(elem) > 1) {
						return false;
					}
				}
			}
		}

		return true;
	}

	public static boolean isValidSudoku2(char[][] board) {
		char val;
		for (int i=0; i<9; i++){
			for (int j=0; j<9; j++){
				val = board[i][j];
				if (val != '.'){
					//row check
					for (int k = 0; k < 9; k++ ){
						if (board[k][j] == val && k != i){
							return false;
						}
					}
					//col Check
					for (int k = 0; k < 9; k++ ){
						if (board[i][k] == val && k != j ){
							return false;
						}
					}
					//square check
					int a = Math.floorDiv(i+3,3)*3-3;
					int b = Math.floorDiv(j+3,3)*3-3;
					for (int p = a; p < a+3; p++ ){
						for (int q = b; q < b+3; q++ ){
							if (board[p][q] == val && p != i && q != j){
								return false;
							}
						}
					}
				}
			}
		}
		return true;
	}
}

```
