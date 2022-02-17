## Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

### Example 1
Input: prices = [7,1,5,3,6,4]

Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

### Example 2

Input: prices = [7,6,4,3,1]

Output: 0

Explanation: In this case, no transactions are done and the max profit = 0.

<pre>
	public static int maxProfit2(int[] prices) {
		int min = prices[0];
		int p = 0;
		for (int i = 1; i < prices.length; i++) {
			if(min > prices[i]) {
				min = prices[i];
			} else if(p < prices[i] - min) {
				p = prices[i] - min;
			}
		}
		return p;
	}
</pre>

Explanation: https://harshitjain.home.blog/2019/08/22/best-time-to-buy-and-sell-stock/


## Maximum Difference Between Increasing Elements
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.

### Example 1
Input: nums = [7,1,5,4]<br>
Output: 4<br>
#### Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

### Example 2
Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].

<pre>
 public int maximumDifference(int[] nums) {
        int diff = -1;
        int min = nums[0];
        
        for(int i = 1; i < nums.length; i++) {
            if(min > nums[i]) {
                min = nums[i];
            } else if(nums[i]-min != 0 && diff < nums[i]-min) {
                diff = nums[i]-min;
            }
        }
        return diff;
    }
</pre>
