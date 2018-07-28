public class Solution
{
    public ListNode reverseList(ListNode head)
    {
        if (head == null)
        {
            return head;
        }

        ListNode prev = null;

        while (head != null)
        {
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }

        return prev;
    }
}
