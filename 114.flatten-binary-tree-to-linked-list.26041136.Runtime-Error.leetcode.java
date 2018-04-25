public class Solution
{

    public void flatten(TreeNode root)
    {
        helper(root, null);
    }
    public void helper(TreeNode root, TreeNode pre)
    {
        if (root == null)
        {
            return;
        }

        TreeNode savedRight = pre.right;

        if (pre != null)
        {
            pre.left = null;
            pre.right = root;
        }

        helper(root.left, root);
        helper(savedRight, root.left);
    }
}

