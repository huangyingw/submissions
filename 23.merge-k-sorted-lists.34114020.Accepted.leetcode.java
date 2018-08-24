public class Solution
{
    public ListNode mergeKLists(ListNode[] lists)
    {
        PriorityQueue<ListNode> heap = new PriorityQueue<ListNode>(10, new Comparator<ListNode>()
        {
            public int compare(ListNode l1, ListNode l2)
            {
                return l1.val - l2.val;
            }
        });

        for (ListNode node : lists)
        {
            if (node != null)
            {
                heap.add(node);
            }
        }

        ListNode dummy = new ListNode(-1);
        ListNode nav = dummy;

        while (!heap.isEmpty())
        {
            ListNode top = heap.poll();
            nav.next = top;
            nav = top;

            if (top.next != null)
            {
                heap.add(top.next);
            }
        }

        return dummy.next;
    }
}
