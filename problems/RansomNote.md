Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

### Example 1:
Input: ransomNote = "a", magazine = "b" <br>
Output: false

### Example 2:
Input: ransomNote = "aa", magazine = "ab" <br>
Output: false

### Example 3:
Input: ransomNote = "aa", magazine = "aab" <br>
Output: true

#### Constraints:
- 1 <= ransomNote.length, magazine.length <= 105 <br>
- ransomNote and magazine consist of lowercase English letters.

```
public static boolean canConstruct(String ransomNote, String magazine) {
		HashMap<Character, Integer> map = new HashMap<>();
		for (char c : magazine.toCharArray()) {
			map.put(c, map.getOrDefault(c, 0) + 1);
		}
		
		for (char c : ransomNote.toCharArray()) {
			map.put(c, map.getOrDefault(c, 0) - 1);
			if(map.get(c) == -1) {
				return false;
			}
		}
		
		return true;
	}
```
