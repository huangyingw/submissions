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
            while (son != null)
            {
                son.next = parent.right;
                son = son.next;
                System.out.printf("son --> %s\n", son.val);
                parent = parent.next;
                System.out.printf("parent --> %s\n", parent.val);
                son.next = parent != null ? parent.left : null;
            }

            parent = parent.left;
            son = parent.left;
        }
    }
}
