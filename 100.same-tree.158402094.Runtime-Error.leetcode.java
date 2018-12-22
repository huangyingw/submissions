public class Solution
{
    public boolean isSameTree(TreeNode p, TreeNode q)
    {
        if (null == p)
        {
            return q == p;
        }

        if (p.val != q.val)
        {
            return false;
        }

        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
== == == =

    >>>>>>> Stashed changes
    == == == =

        >>>>>>> Stashed changes
        == == == =

            >>>>>>> Stashed changes
            == == == =

                >>>>>>> Stashed changes
                == == == =

                    >>>>>>> Stashed changes
                    == == == =

                        >>>>>>> Stashed changes
                        == == == =

                            >>>>>>> Stashed changes
                            == == == =

                                >>>>>>> Stashed changes
                                == == == =

                                    >>>>>>> Stashed changes
