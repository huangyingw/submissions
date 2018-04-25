public class Solution
{
    public ArrayList<Integer> preorderTraversal(TreeNode top)
    {
        ArrayList<Integer> result = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();

        while (!stack.empty() || null != top)
        {
            if (top != null)
            {
                stack.push(top);
                result.add(top.val);
                top = top.left;
            }
            else
            {
                top = stack.pop();
                top = top.right;
            }
        }

        return result;
    }
}

