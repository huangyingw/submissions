public class Solution
{
    public void connect(TreeLinkNode root)
    {
        while (root != null)
        {
            TreeLinkNode leftMost = null;
            TreeLinkNode nav = null;

            for (; root != null; root = root.next)
            {
                leftMost = root.left;

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

