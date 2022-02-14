# Maximum Contigous SubArray
## Bruteforce approach
- Execution time takes long time.
- for large input, Time limit may exceed

<pre>
public int maxSubArray(int[] nums) {
    int maxSum = Integer.MIN_VALUE;
		int currSum = 0;
		for (int j = 0; j < nums.length; j++) {
			currSum = 0;
			for (int i = j; i < nums.length; i++) {
				currSum = currSum + nums[i];
				if(maxSum < currSum) {
					maxSum = currSum;
				}
			}	
		}
		return maxSum;
 }
</pre>
