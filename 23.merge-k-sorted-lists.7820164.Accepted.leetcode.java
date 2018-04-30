public class Solution {
		public ListNode mergeKLists(ArrayList<ListNode> lists) {
			PriorityQueue<ListNode> heap = new PriorityQueue<ListNode>(10,
					new Comparator<ListNode>() {
						@Override
						public int compare(ListNode l1, ListNode l2) {
							return l1.val - l2.val;
						}
					});

			for (ListNode node : lists) {
				if (node != null) {
					heap.add(node);
				}
			}

			ListNode dummy = new ListNode(-1);
			ListNode result = dummy;

			while (!heap.isEmpty()) {
				ListNode top = heap.poll();

				result.next = top;
				result = top;

				if (top.next != null) {
					heap.add(top.next);
				}
			}

			return dummy.next;
		}
	}

