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
                    <<< <<< < Updated upstream
                    <<< <<< < Updated upstream
                    == == == =
                        >>> >>> > Stashed changes
                        == == == =
                            >>> >>> > Stashed changes
                            == == == =
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
                        <<< <<< < Updated upstream
                        <<< <<< < Updated upstream
                        == == == =
                            >>> >>> > Stashed changes
                            == == == =
                                >>> >>> > Stashed changes
                                == == == =
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
                        <<< <<< < Updated upstream
                        <<< <<< < Updated upstream
                        == == == =
                            >>> >>> > Stashed changes
                            == == == =
                                >>> >>> > Stashed changes
                                == == == =
                                    >>> >>> > Stashed changes
                    }
                }
            }

            root = leftMost;
        }
    }
}
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
== == == =

    >>>>>>> Stashed changes
    == == == =

        >>>>>>> Stashed changes
        == == == =

            >>>>>>> Stashed changes
