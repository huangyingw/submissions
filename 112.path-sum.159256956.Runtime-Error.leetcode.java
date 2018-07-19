public class Solution
{
    public boolean hasPathSum(TreeNode root, int sum)
    {
        if (root != null && root.left == null && root.right == null)
        {
            return  root.val == sum;
        }

        boolean left = hasPathSum(root.left, sum - root.val);
        boolean right = hasPathSum(root.right, sum - root.val);
        return  left || right;
    }
}
