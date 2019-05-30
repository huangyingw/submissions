public class Solution
{
    public int countUnivalSubtrees(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        ArrayList<Integer> sum = new ArrayList<Integer>();
        sum.add(0);
        dfs(root, sum);
        return sum.get(0);
    }

    public boolean dfs(TreeNode root, ArrayList<Integer> sum)
    {
        if (root == null)
        {
            return true;
        }

        boolean left = dfs(root.left, sum);
        boolean right = dfs(root.right, sum);

        if (left && right && (root.left == null || root.val == root.left.val) && (root.right == null || root.val == root.right.val))
        {
            sum.set(0, sum.get(0) + 1);
            return true;
        }

        return false;
    }
}
