public class Solution
{
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p)
    {
        Stack<TreeNode> stack = new Stack<TreeNode>();

        if (root == null || p == null)
        {
            return null;
        }

        stack.push(root);
        boolean isNext = false;

        while (!stack.isEmpty())
        {
            TreeNode top = stack.pop();

            if (top.right == null && top.left == null)
            {
                if (isNext)
                {
                    return top;
                }

                if (p.val == top.val)
                {
                    isNext = true;
                }

                continue;
            }

            if (top.right != null)
            {
                stack.push(top.right);
                top.right = null;
            }

            stack.push(top);

            if (top.left != null)
            {
                stack.push(top.left);
                top.left = null;
            }
        }

        return null;
    }
}

