public class Solution
{
    public ListNode reverseList(ListNode head)
    {
        ListNode ret = recursive(head);
        head.next = null;
        return ret;
    }
    public ListNode recursive(ListNode head)
    {
        if (head == null || head.next == null)
        {
            return head;
        }

        ListNode second = head.next;
        ListNode ret = recursive(second);
        second.next = head;
        return ret;
    }
}
