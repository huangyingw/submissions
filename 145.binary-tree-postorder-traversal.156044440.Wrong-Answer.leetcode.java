public class Solution
{
    public ArrayList<Integer> postorderTraversal(TreeNode root)
    {
        if (root == null)
        {
            return null;
        }

        ArrayList<Integer> list = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);

        while (!stack.isEmpty())
        {
            TreeNode top = stack.peek();

            if (top.left == null && top.right == null)
            {
                list.add(top.val);
                stack.pop();
            }
            else if (top.left != null)
            {
                stack.push(top.left);
                top.left = null;
            }
            else if (top.right != null)
            {
                stack.push(top.right);
                top.right = null;
            }
        }

        return list;
    }
}

