public class Solution
{

    public ListNode mergeTwoLists(ListNode l1, ListNode l2)
    {
        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode fakeHead = new ListNode(0);
        ListNode p = fakeHead;

        while (p1 != null && p2 != null)
        {
            if (p1.val <= p2.val)
            {
                p.next = p1;
                p1 = p1.next;
            }
            else
            {
                p.next = p2;
                p2 = p2.next;
            }

            p = p.next;
        }

        p.next = p1 != null ? p1 : p2;
        return fakeHead.next;
    }

    public ListNode mergeKLists(ArrayList<ListNode> lists)
    {
        if (lists.size() == 0)
        {
            return null;
        }

        ListNode p = lists.get(0);

        for (int i = 1; i < lists.size(); i++)
        {
            p = mergeTwoLists(p, lists.get(i));
        }

        return p;
    }
}

