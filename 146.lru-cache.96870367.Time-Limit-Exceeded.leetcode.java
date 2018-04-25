public class LRUCache
{
    private class Node
    {
        Node prev;
        Node next;
        int key;
        int value;

        public Node(int key, int value)
        {
            this.key = key;
            this.value = value;
            this.prev = null;
            this.next = null;
        }
    }

    private int capacity;
    private HashMap<Integer, Node> hs = new HashMap<Integer, Node>();
    private Node head = new Node(-1, -1);
    private Node tail = new Node(-1, -1);

    public LRUCache(int capacity)
    {
        this.capacity = capacity;
        tail.prev = head;
        head.next = tail;
    }

    public int get(int key)
    {
        if (!hs.containsKey(key))
        {
            return -1;
        }

        Node node = hs.get(key);
        node.prev.next = node.next;
        node.next.prev = node.prev;
        printNodes();
        moveToTail(node);
        return node.value;
    }

    public void printNodes()
    {
        Node node = head.next;

        while (node.next != null)
        {
            System.out.println(node.key + "->" + node.value + ",");
            node = node.next;
        }

        System.out.println();
    }

    public void put(int key, int value)
    {
        if (get(key) != -1)
        {
            hs.get(key).value = value;
            return;
        }

        if (hs.size() == capacity)
        {
            hs.remove(head.next.key);
            head.next = head.next.next;
            head.next.prev = head;
        }

        Node insert = new Node(key, value);
        hs.put(key, insert);
        moveToTail(insert);
        printNodes();
    }

    private void moveToTail(Node current)
    {
        tail.prev.next = current;
        current.prev = tail.prev;
        tail.prev = current;
        current.next = tail;
    }
}
