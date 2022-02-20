You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg

### Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4] <br>
Output: [1,1,2,3,4,4]

### Example 2:
Input: list1 = [], list2 = [] <br>
Output: []

### Example 3:
Input: list1 = [], list2 = [0] <br>
Output: [0]

```
package com.prep;

import java.util.HashSet;

public class MergeTwoSortedLinkedLists {

	static class ListNode { 
		int val; 
		ListNode next;

		public ListNode() {}
		ListNode(int x) { 
			val = x; 
			next = null;
		}
		
		ListNode(int x, ListNode n) { 
			val = x; 
			next = n;
		}
	}

	public static void main(String[] args) {
		ListNode first = new ListNode(1);
		insert(first, 2);
		insert(first, 4);
		print(first);

		ListNode second = new ListNode(1);
		insert(second, 3);
		insert(second, 4);
		print(second);

		ListNode merged = mergeTwoLists(first, second);
		print(merged);
	}

	public static void print(ListNode head) {
		if(head == null) {
			return;
		}

		ListNode iter = head;
		do {
			System.out.print(iter.val + " ");
			iter = iter.next;
		} while(iter != null);
		System.out.println();
	}

	public static ListNode insert(ListNode head, int val) {
		ListNode newNode = new ListNode(val);
		newNode.next = null;

		if(head == null) {
			head = newNode;
			return head;
		}

		ListNode iter = head;
		while(iter.next != null) {
			iter = iter.next;
		}
		iter.next = newNode;
		return head;
	}

	public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
		if(list1 == null && list2 == null) {
			return null;
		}
		if(list1 == null) {
			return list2;
		}

		if(list2 == null) {
			return list1;
		}

		ListNode merged = null, head = null;
		ListNode f = list1;
		ListNode s = list2;

		while(f != null && s != null) {
			if(f.val > s.val) {
				if(merged == null) {
					head = new ListNode(s.val, null);
					merged = head;
				} else {
					merged.next = new ListNode(s.val, null);
					merged = merged.next;
				}
				s = s.next;
			} else {
				if(merged == null) {
					head = new ListNode(f.val, null);
					merged = head;
				} else {
					merged.next = new ListNode(f.val, null);
					merged = merged.next;
				}
				f = f.next;
			}	
		}

		if(f == null) {
			while(s != null) {
				merged.next = new ListNode(s.val);
				merged = merged.next;
				s = s.next;
			}
		}

		if(s == null) {
			while(f != null) {
				merged.next = new ListNode(f.val);
				merged = merged.next;
				f = f.next;
			}
		}
		return head;
	}
}

```
