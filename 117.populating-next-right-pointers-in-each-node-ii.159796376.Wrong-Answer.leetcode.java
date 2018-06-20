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
                if (root != null)
                {
                    System.out.printf("nav --> %s\n", root.val);
                }

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

                    nav = root.next;

                    if (nav != null)
                    {
                        System.out.printf("nav --> %s\n", nav.val);
                    }
                }

                if (root.right != null)
                {
                    if (nav != null)
                    {
                        nav.next = root.right;
                    }

                    nav = root.right;

                    if (nav != null)
                    {
                        System.out.printf("nav --> %s\n", nav.val);
                    }
                }
            }

            root = leftMost;
        }
    }
}

