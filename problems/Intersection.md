
# Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

### Example 1
Input: nums1 = [1,2,2,1], nums2 = [2,2]

Output: [2,2]

<pre>
public int[] intersect(int[] nums1, int[] nums2) {
        
		HashMap<Integer, Integer> map = new HashMap<>();
		ArrayList<Integer> list = new ArrayList<>();
		int m = nums1.length;
		int n = nums2.length;
		
		if(m > n) {
			for (int i : nums2) {
				map.put(i, map.getOrDefault(i, 0) + 1);
			}
			
			for (int i : nums1) {
				map.put(i, map.getOrDefault(i, 0) - 1);
				if(map.get(i) >= 0) {
					list.add(i);
				}
			}
		} else {
			for (int i : nums1) {
				map.put(i, map.getOrDefault(i, 0) + 1);
			}
			
			for (int i : nums2) {
				map.put(i, map.getOrDefault(i, 0) - 1);
				if(map.get(i) >= 0) {
					list.add(i);
				}
			}
		}
		int [] common = new int[list.size()];
		int i = 0;
		for (Integer integer : list) {
			common[i++] = integer;
		}
		return common;
	
  }
</pre>
