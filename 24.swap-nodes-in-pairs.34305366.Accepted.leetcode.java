public class Solution
{
    public ListNode swapPairs(ListNode head)
    {
        return rec(head);
    }
    public ListNode rec(ListNode head)
    {
        if (head == null || head.next == null)
        {
            return head;
        }

        ListNode p = head;
        ListNode q = p.next.next;
        p.next.next = p;
        ListNode newHead = p.next;
        p.next = rec(q);
        return newHead;
    }
}
