public class Solution
{
    public boolean isPalindrome(ListNode head)
    {
        if (head == null)
        {
            return true;
        }

        ListNode slow = head;
        ListNode fast = slow.next;

        while (fast != null && fast.next != null && fast.next.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode end = reverseList(slow.next);

        while (head != null && end != null)
        {
            if (head.val != end.val)
            {
                return false;
            }

            head = head.next;
            end = end.next;
        }

        return true;
    }

    public ListNode reverseList(ListNode head)
    {
        if (head == null || head.next == null)
        {
            return head;
        }

        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode curr = head.next;

        while (curr != null)
        {
            ListNode nextNode = curr.next;
            curr.next = dummy.next;
            dummy.next = curr;
            curr = nextNode;
        }

        head.next = null;
        return dummy.next;
    }
}
