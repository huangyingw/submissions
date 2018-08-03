class Solution
{
    public int kthSmallest(TreeNode root, int k)
    {
        Stack<TreeNode> stack = new Stack<TreeNode>();

        while (k > 0 && (!stack.empty() || root != null))
        {
            if (root != null)
            {
                stack.push(root);
                root = root.left;
            }
            else
            {
                root = stack.pop();

                if (--k == 0)
                {
                    return root.val;
                }

                root = root.right;
            }
        }

        return root.val;
    }
}
