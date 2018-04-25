public class Solution
{
    public List<Integer> inorderTraversal(TreeNode root)
    {
        List<Integer> inOrder = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode top = root;

        if (top == null)
        {
            return inOrder;
        }

        while (!stack.empty())
        {
            if (top != null || top != null)
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
