public class Solution
{
    public int rob(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        int[] result = dfs(root);
        return Math.max(result[0], result[1]);
    }

    public int[] dfs(TreeNode root)
    {
        if (root == null)
        {
            int[] result = {0, 0};
            return result;
        }

        int[] result = new int[2];
        int[] left = dfs(root.left);
        int[] right = dfs(root.right);
        // result[0] is when root is selected, result[1] is when not.
        result[0] = root.val + left[1] + right[1];
        result[1] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return result;
    }
}
