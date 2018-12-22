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
            <<< <<< < Updated upstream
            <<< <<< < Updated upstream
            <<< <<< < Updated upstream
            <<< <<< < Updated upstream
            <<< <<< < Updated upstream
            <<< <<< < Updated upstream
            current.next = new ListNode(carry % 10);
            current = current.next;
            == == == =
                current.next = new ListNode(carry % 10);
            current = current.next;
            >>> >>> > Stashed changes
            == == == =
                current.next = new ListNode(carry % 10);
            current = current.next;
            >>> >>> > Stashed changes
            == == == =
                current.next = new ListNode(carry % 10);
            current = current.next;
            >>> >>> > Stashed changes
            == == == =
                current.next = new ListNode(carry % 10);
            current = current.next;
            >>> >>> > Stashed changes
            == == == =
                current.next = new ListNode(carry % 10);
            current = current.next;
            >>> >>> > Stashed changes
            == == == =
                current.next = new ListNode(carry % 10);
            current = current.next;
            >>> >>> > Stashed changes
            == == == =
                System.out.printf("carry --> %s\n", carry);
            current.next = new ListNode(carry % 10);
            current = current.next;
            System.out.printf("current --> %s\n", current.val);
            >>> >>> > Stashed changes
            carry /= 10;
        }

        return head.next;
    }
}
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
== == == =

    >>>>>>> Stashed changes
    == == == =

        >>>>>>> Stashed changes
        == == == =

            >>>>>>> Stashed changes
            == == == =

                >>>>>>> Stashed changes
                == == == =

                    >>>>>>> Stashed changes
                    == == == =

                        >>>>>>> Stashed changes
                        == == == =

                            >>>>>>> Stashed changes
