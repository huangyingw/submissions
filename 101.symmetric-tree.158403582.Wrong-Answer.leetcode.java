public class Solution
{
    public boolean isSymmetric(TreeNode root)
    {
        if (root == null)
        {
            return true;
        }

        Stack<TreeNode> lefts = new Stack<TreeNode>();
        Stack<TreeNode> rights = new Stack<TreeNode>();
        lefts.push(root.left);
        rights.push(root.right);

        while (!lefts.isEmpty() && !rights.isEmpty())
        {
            TreeNode left = lefts.pop();
            TreeNode right = rights.pop();

            if (left == null || right == null)
            {
                return left == right;
            }

            if (left.val != right.val)
            {
                return false;
            }

            lefts.push(left.left);
            lefts.push(left.right);
            rights.push(right.right);
            rights.push(right.left);
        }

        return lefts.isEmpty() && rights.isEmpty();
    }
}
