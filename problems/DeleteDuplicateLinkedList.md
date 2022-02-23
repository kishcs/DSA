Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1
Input: head = [1,1,2] <br>
Output: [1,2]

### Example 2
Input: head = [1,1,2,3,3] <br>
Output: [1,2,3]

```
public static ListNode deleteDuplicates(ListNode head) {
		if(head == null) {
			return null;
		}
		
		ListNode iter = head;
		if(iter.next == null) {
			return head;
		}
		
		while (iter != null && iter.next != null) {
			if(iter.val == iter.next.val) {
				iter.next = iter.next.next;
			} else {
				iter = iter.next;
			}
		}
        return head;
    }
```
