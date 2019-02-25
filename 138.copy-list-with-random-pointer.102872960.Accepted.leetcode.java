public class Solution
{
    private void copyNext(Node head)
    {
        while (head != null)
        {
            Node newHead = new Node(head.val);
            newHead.next = head.next;
            newHead.random = head.random;
            head.next = newHead;
            head = head.next.next;
        }
    }

    private void copyRandom(Node head)
    {
        while (head != null)
        {
            if (head.next.random != null)
            {
                head.next.random = head.random.next;
            }

            head = head.next.next;
        }
    }

    private Node splitList(Node head)
    {
        Node newHead = head.next;

        while (head != null && head.next != null)
        {
            Node temp = head.next;
            head.next = temp.next;
            head = temp;
        }

        return newHead;
    }

    public Node copyRandomList(Node head)
    {
        if (head == null)
        {
            return null;
        }

        copyNext(head);
        copyRandom(head);
        return splitList(head);
    }
}
