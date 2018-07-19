public class Solution
{
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
    {
        if (root == null || p == null || q == null)
        {
            return null;
        }

        List<TreeNode> pathp = new ArrayList<>();
        List<TreeNode> pathq = new ArrayList<>();
        pathp.add(root);
        pathq.add(root);
        getPath(root, p, pathp);
        getPath(root, q, pathq);
        int i = 0;

        while (i < pathp.size() && i < pathq.size() && pathp.get(i) == pathq.get(i))
        {
            i++;
        }

        return pathp.get(i - 1);
    }

    private boolean getPath(TreeNode root, TreeNode n, List<TreeNode> path)
    {
        if (root == null)
        {
            return false;
        }

        path.add(root);

        if (root == n)
        {
            return true;
        }

        if ((root.left != null && getPath(root.left, n, path)) || (root.right != null && getPath(root.right, n, path)))
        {
            return true;
        }

        path.remove(path.size() - 1);
        return false;
    }
}
