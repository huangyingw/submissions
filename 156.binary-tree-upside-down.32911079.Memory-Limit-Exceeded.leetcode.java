public class Solution
{
    public TreeNode upsideDownBinaryTree(TreeNode root)
    {
        if (root == null)
        {
            return null;
        }

        ArrayList<TreeNode> res = new ArrayList<TreeNode>();
        res.add(null);
        dfs(root, res);
        return res.get(0);
    }

    public TreeNode dfs(TreeNode root, ArrayList<TreeNode> res)
    {
        if (root.left == null)
        {
            res.set(0, root);
            return root;
        }

        TreeNode newRoot = dfs(root.left, res);
        newRoot.left = root.right;
        newRoot.right = root;
        return newRoot.right;
    }
}
