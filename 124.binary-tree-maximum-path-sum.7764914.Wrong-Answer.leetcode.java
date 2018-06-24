public class Solution
{

    private int max;

    public int findMax(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        int left = findMax(root.left);
        int right = findMax(root.left);
        int sum = root.val;

        if (left > 0)
        {
            sum += left;
        }

        if (right > 0)
        {
            sum += right;
        }

        max = Math.max(max, sum);
        return Math.max(left, right) > 0 ? Math.max(left, right) + root.val : root.val;
    }

    public int maxPathSum(TreeNode root)
    {
        max = Integer.MIN_VALUE;
        findMax(root);
        return max;
    }
}
