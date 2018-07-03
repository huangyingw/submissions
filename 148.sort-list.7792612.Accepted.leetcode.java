public class Solution
{
    private ListNode merge(ListNode h1, ListNode h2)
    {
        ListNode dummy = new ListNode(0);
        ListNode prefix = dummy;

        while (h1 != null || h2 != null)
        {
            if (h2 == null || (h1 != null && h1.val < h2.val))
            {
                prefix.next = h1;
                prefix = h1;
                h1 = h1.next;
            }
            else
            {
                prefix.next = h2;
                prefix = h2;
                h2 = h2.next;
            }
        }

        return dummy.next;
    }

    public ListNode sortList(ListNode head)
    {
        if (head == null || head.next == null)
        {
            return head;
        }

        ListNode fast = head, slow = head;

        while (fast.next != null && fast.next.next != null)
        {
            fast = fast.next.next;
            slow = slow.next;
        }

        fast = slow;
        slow = slow.next;
        fast.next = null;
        ListNode l1 = sortList(head);
        ListNode l2 = sortList(slow);
        return merge(l1, l2);
    }
}
