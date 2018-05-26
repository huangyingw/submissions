public class Solution
{
    public List<Integer> inorderTraversal(TreeNode root)
    {
        List<Integer> inOrder = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode top = root;

        while (!stack.empty() || top != null)
        {
            if (top != null)
            {
                stack.push(top);
                top = top.left;
            }
            else
            {
                top = stack.pop();
                inOrder.add(top.val);
                top = top.right;
            }
        }

        return inOrder;
    }
}

