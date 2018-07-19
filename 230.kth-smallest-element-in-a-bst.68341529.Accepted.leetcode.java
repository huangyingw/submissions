public class Solution
{
    public int kthSmallest(TreeNode root, int k)
    {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode top = root;

        while (!stack.empty() || null != top)
        {
            if (top != null)
            {
                stack.push(top);
                top = top.left;
            }
            else
            {
                top = stack.pop();

                if (--k == 0)
                {
                    return top.val;
                }

                top = top.right;
            }
        }

        return root.val;
    }
}
