public class Solution
{
    public ArrayList<Integer> inorderTraversal(TreeNode top)
    {
        ArrayList<Integer> result = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();

        while (!stack.empty() || top != null)
        {
            while (top != null)
            {
                stack.push(top);
                top = top.left;
            }

            top = stack.pop();
            result.add(top.val);
            top = top.right;
        }

        return result;
    }
}

