public class Solution
{
    public void connect(TreeLinkNode root)
    {
        if (root == null)
        {
            return;
        }

        while (root != null)
        {
            TreeLinkNode leftMost = null;
            TreeLinkNode nav = null;

            for (; root != null; root = root.next)
            {
                if (leftMost == null)
                {
                    leftMost = root.left != null ? root.left : root.right;
                }

                if (root.left != null && nav != null)
                {
                    nav.next = root.left;
                }

                if (root.right != null && nav != null)
                {
                    nav.next = root.right;
                }

                nav = nav.next;
            }

            root = leftMost;
        }
    }
}
