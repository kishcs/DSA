Given the head of a singly linked list, reverse the list, and return the reversed list.

### Example 1
Input: head = [1,2,3,4,5] <br>
Output: [5,4,3,2,1]

```
public ListNode reverseList(ListNode head) {
        
		if(head == null) {
			return null;
		}
		ListNode rNext = null;
		ListNode iter = head;
		do {
			rNext = new ListNode(iter.val, rNext);
			iter = iter.next;
		} while(iter != null);
		
		return rNext;
	
    }
```
