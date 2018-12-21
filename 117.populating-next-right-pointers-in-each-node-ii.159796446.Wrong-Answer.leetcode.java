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
                    <<< <<< < Updated upstream
                    == == == =
                        System.out.printf("root --> %s\n", root.val);
                    >>> >>> > Stashed changes
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
                        <<< <<< < Updated upstream
                        == == == =
                            System.out.printf("nav --> %s\n", nav.val);
                        >>> >>> > Stashed changes
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
                        <<< <<< < Updated upstream
                        == == == =
                            System.out.printf("nav --> %s\n", nav.val);
                        >>> >>> > Stashed changes
                    }
                }
            }

            root = leftMost;
        }
    }
}
<<< <<< < Updated upstream
== == == =

    >>>>>>> Stashed changes
