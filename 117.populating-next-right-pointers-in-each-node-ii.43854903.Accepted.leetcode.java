public class Solution
{
    public void connect(TreeLinkNode root)
    {
        while (root != null)
        {
            TreeLinkNode leftMost = null; // the first node of next level
            TreeLinkNode nav = null; // previous node on the same level

            for (; root != null; root = root.next)
            {
                if (leftMost == null)
                {
                    leftMost = root.left != null ? root.left : root.right;
                }

                if (root.left != null)
                {
                    if (nav != null)
                    {
                        nav.next = root.left;
                    }

                    nav = root.left;
                }

                if (root.right != null)
                {
                    if (nav != null)
                    {
                        nav.next = root.right;
                    }

                    nav = root.right;
                }
            }

            root = leftMost; // turn to next level
        }
    }
}
