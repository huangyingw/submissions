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
                parent = parent.next;
                son.next = parent != null ? parent.left : null;
                son = son.next;
            }

            parent = parent.left;
            son = parent.left;
        }
    }
}
