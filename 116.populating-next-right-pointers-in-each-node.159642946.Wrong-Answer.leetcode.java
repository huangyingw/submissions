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
                parent = parent.right;
                son.next = parent != null ? parent.left : null;
                son = son.next;

                if (son != null)
                {
                }
            }

            parent = back;
            son = parent.left;
        }
    }
}
