# Find index of 2 numbers for matching Sum 
## This is using HashMap with O(n) as compared to Brute-force O(n2)

<pre>
  public static int[] twoSum(int[] arr, int sum) {
		int[] indices = new int[2];
		HashMap<Integer, Integer> store = new HashMap<>();
		for(int i = 0; i < arr.length; i++) {
			int s = sum - arr[i];
			if(store.containsKey(s)) {
				indices[0] = store.get(s);
				indices[1] = i;
				return indices;
			}
			store.put(arr[i], i);
		}
		return indices;
	}
  </pre>
