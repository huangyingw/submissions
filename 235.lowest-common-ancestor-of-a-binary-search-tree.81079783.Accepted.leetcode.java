public class Solution
{
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
    {
         while (true)
        {
            if (root == null || p == null || q == null)
            {
                return null;
            }

            if (Math.max(p.val, q.val) < root.val)
            {
                root = root.left;
            }
            else if (Math.min(p.val, q.val) > root.val)
            {
                root = root.right;
            }
            else
            {
                return root;
            }
        }
    }
}
