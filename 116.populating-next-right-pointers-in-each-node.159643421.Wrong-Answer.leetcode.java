public class Solution
{
    void connect(TreeLinkNode root)
    {
        if (root == null)
        {
            return;
        }

        TreeLinkNode parent = root, son = root.left;

        while (son != null)
        {
            TreeLinkNode back = son;

            while (son != null)
            {
                son.next = parent.right;
                son = son.next;
                System.out.printf("son  --> %s\n", son.val);
                parent = parent.right;
                System.out.printf("parent 1 --> %s\n", parent.val);
                son.next = parent != null ? parent.left : null;
                son = son.next;

                if (son != null)
                {
                    System.out.printf("son  --> %s\n", son.val);
                }
            }

            parent = back;
            System.out.printf("parent 2 --> %s\n", parent.val);
            son = parent.left;

            if (son != null)
            {
                System.out.printf("son  --> %s\n", son.val);
            }
        }
    }
}

