public class Solution
{
    public int minDepth(TreeNode root)
    {
        return minDepth(root, false);
    }

    public int minDepth(TreeNode root, Boolean hasBrother)
    {
        if (root == null)
        {
            return hasBrother ? Integer.MAX_VALUE : 0;
        }

        return 1 + Math.min(minDepth(root.left, root.right != null), minDepth(root.right, root.left != null));
    }
}

