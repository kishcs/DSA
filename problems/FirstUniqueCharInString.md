Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Input: s = "leetcode" <br>
Output: 0

Input: s = "aabb" <br>
Output: -1

Input: s = "loveleetcode" <br>
Output: 2

Input: s = "abccbad" <br>
Output: 6

### Constraints:
1 <= s.length <= 105 <br>
s consists of only lowercase English letters.

```
public static int firstUniqChar(String s) {
		char[] chars = s.toCharArray();
		int[] pos = new int[26];
		for (int i = 0; i < pos.length; i++) {
			pos[i] = -1;
		}
		HashMap<Character, Integer> map = new HashMap<>();
		for (int i = chars.length - 1; i >= 0; i--) {
			map.put(chars[i], map.getOrDefault(chars[i], 0) + 1);
			pos[chars[i] - 'a'] = i;
		}
		int index = Integer.MAX_VALUE;
		for (char c : map.keySet()) {
			if (map.get(c) == 1 && pos[c - 'a'] != -1 && index > pos[c - 'a']) {
				index = pos[c - 'a'];
			}
		}
		if (index == Integer.MAX_VALUE) {
			return -1;
		}
		return index;
	}

	public static int firstUniqChar2(String s) {
		char[] chars = s.toCharArray();

		LinkedHashMap<Character, Integer> map = new LinkedHashMap<>();
		for (int i = chars.length - 1; i >= 0; i--) {
			map.put(chars[i], map.getOrDefault(chars[i], 0) + 1);
		}

		for (int i = map.keySet().size()-1; i >= 0; i--) {
			char c = (char)map.keySet().toArray()[i];
			if(map.get(c) == 1) {
				return s.indexOf(c);
			}
		}

		return -1;
	}
```
