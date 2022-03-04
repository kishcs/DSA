# Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

### Example 1:
- Input: strs = ["flower","flow","flight"]
- Output: "fl"

### Example 2:
- Input: strs = ["dog","racecar","car"]
- Output: ""

- Explanation: There is no common prefix among the input strings.

### Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lower-case English letters.


### Slow way

```
public String longestCommonPrefix(String[] strs) {
        if(strs.length == 1) {
            return strs[0]; 
        }
        int len = strs.length;
        for(int i = 1; i < len; i++) {
            if(strs[i].length() == 0) {
                return "";
            }    
        }

        String prefix = strs[0];
        for(int i = 1; i < len; i++) {
            prefix = prefix(prefix, strs[i]);
        }
        return prefix;
    }
    public String prefix(String a, String b) {
        int len1 = a.length();
        int len2 = b.length();
        String p = "";
        for(int j=0, k=0; j<len1 && k<len2; j++, k++) {
            if(a.charAt(j) != b.charAt(k)) {
                break;
            }
            p = p + a.charAt(j);
        }
        return p;
    }
```
