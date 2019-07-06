public class Solution
{
    public void flatten(TreeNode root)
    {
        dfs(root, root);
    }
    public void dfs(TreeNode root, TreeNode pre)
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

        dfs(root.left, root);
        dfs(savedRight, root.left);
    }
}
