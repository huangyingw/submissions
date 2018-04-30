public class Solution
{
    public ArrayList<Integer> postorderTraversal(TreeNode root)
    {
        ArrayList<Integer> postorder = new ArrayList<Integer>();

        if (root == null)
        {
            return postorder;
        }

        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode prev = null;
        stack.push(root);

        while (!stack.isEmpty())
        {
            TreeNode curr = stack.peek();

            if (prev == null || prev.left == curr || prev.right == curr)
            {
                if (curr.left != null)
                {
                    stack.push(curr.left);
                }
                else if (curr.right != null)
                {
                    stack.push(curr.right);
                }
            }
            else if (curr.left == prev)
            {
                if (curr.right != null)
                {
                    stack.push(curr.right);
                }
            }
            else
            {
                postorder.add(curr.val);
                stack.pop();
            }

            prev = curr;
        }

        return postorder;
    }
}

