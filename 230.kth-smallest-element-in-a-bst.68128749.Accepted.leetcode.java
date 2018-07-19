public class Solution
{
    public int kthSmallest(TreeNode root, int k)
    {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode current = root;

        while (current != null || !stack.isEmpty())
        {
            if (current != null)
            {
                stack.push(current);
                current = current.left;
            }
            else
            {
                current = stack.pop();

                if (--k == 0)
                {
                    return current.val;
                }

                current = current.right;
            }
        }

        return root.val;
    }
}
