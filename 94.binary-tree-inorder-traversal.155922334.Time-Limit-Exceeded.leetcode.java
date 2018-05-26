public class Solution
{
    public ArrayList<Integer> inorderTraversal(TreeNode root)
    {
        ArrayList<Integer> inOrder = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode current = root;
        stack.push(current);

        while (!stack.empty())
        {
            current = stack.pop();

            if (current != null)
            {
                stack.push(current);
                current = current.left;
            }
            else
            {
                current = stack.pop();
                inOrder.add(current.val);
                current = current.right;
            }
        }

        return inOrder;
    }
}

