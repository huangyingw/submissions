public class Solution
{
    private void copyNext(RandomListNode head)
    {
        while (head != null)
        {
            RandomListNode newNode = new RandomListNode(head.label);
            newNode.next = head.next;
            head.next = newNode;
            head = head.next.next;
        }
    }

    private void copyRandom(RandomListNode head)
    {
        while (head != null && head.next != null)
        {
            if (head.next.random != null)
            {
                head.next.random = head.random.next;
            }

            head = head.next.next;
        }
    }

    private RandomListNode splitList(RandomListNode head)
    {
        RandomListNode newHead = head.next;

        while (head != null && head.next != null)
        {
            RandomListNode temp = head.next;
            head.next = temp.next;
            head = temp;
        }

        return newHead;
    }

    {
        while (head != null)
        {
            head = head.next;
        }

    }
    public RandomListNode copyRandomList(RandomListNode head)
    {
        if (head == null)
        {
            return null;
        }

        copyNext(head);
        copyRandom(head);
        head = splitList(head);
        return head;
    }
}
