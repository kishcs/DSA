Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

### Example 3:
Input: head = [1,2,6,3,4,5,6], val = 6 <br>
Output: [1,2,3,4,5]

### Example 2:
Input: head = [], val = 1 <br>
Output: []

### Example 3:
Input: head = [7,7,7,7], val = 7 <br>
Output: []

```
public ListNode removeElements(ListNode head, int val) {
        
        if(head == null) {
            return head;
        }
        
        if(head.next == null) {
        	if(head.val == val) {
        		return null;
        	}
            return head;
        }
        
        ListNode prev = head;
        ListNode curr = head.next;
        
        while(curr != null) {
            if(curr.val == val) {
                prev.next = curr.next;
                curr = prev.next;
            } else {
            	prev = curr;
                curr = curr.next;	
            }
        }
        
        if(head.val == val) {
        	head = head.next;
        }
        //print(head);
        return head;
    
    }
```

### Another Simple Solution
```
public static ListNode remove(ListNode head, int val) {
		if(head == null){
            return null;
        }
        while(head != null && head.val == val){
            head = head.next;
        }
        if(head == null){
            return null;
        }
        ListNode temp = head;
        while(head.next != null){
            if(head.next.val == val){
                head.next = head.next.next;
            }
            else {
                head = head.next;
            }
        }
        return temp;
	}
```
