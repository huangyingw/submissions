public class Solution
{
    public ListNode addTwoNumbers(ListNode l1, ListNode l2)
    {
        int carry = 0;
        ListNode head = new ListNode(-1);
        ListNode current = head;

        while (l1 != null | l2 != null)
        {
            if (l1 != null)
            {
                carry += l1.val;
                l1 = l1.next;
            }

            if (l2 != null)
            {
                carry += l2.val;
                l2 = l2.next;
            }

            <<< <<< < Updated upstream
            current.next = new ListNode(carry % 10);
            current = current.next;
            == == == =
                current.next = new ListNode(carry % 10);
            current = current.next;
            >>> >>> > Stashed changes
            carry /= 10;
        }

        return head.next;
    }
}
<<< <<< < Updated upstream
== == == =

    >>>>>>> Stashed changes
