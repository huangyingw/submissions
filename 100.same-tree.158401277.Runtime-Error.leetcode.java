public class Solution
{
    public boolean isSameTree(TreeNode p, TreeNode q)
    {
        if (p == q)
        {
            return true;
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
== == == =

    >>>>>>> Stashed changes
    == == == =

        >>>>>>> Stashed changes
