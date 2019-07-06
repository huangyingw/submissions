public class Solution
{
    public ArrayList<Integer> preorderTraversal(TreeNode root)
    {
        ArrayList<Integer> list = new ArrayList<Integer>();
        ArrayList<Integer> list2 = new ArrayList<Integer>();

        if (root == null)
        {
            return list;
        }

        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);

        while (stack.size() != 0)
        {
            TreeNode top = stack.peek();

            if (top.left == null && top.right == null)
            {
                list.add(top.val);
                stack.pop();
            }

            if (top.right != null)
            {
                stack.push(top.right);
                top.right = null;
                continue;
            }

            if (top.left != null)
            {
                stack.push(top.left);
                top.left = null;
                continue;
            }
        }

        for (int i = 0; i < list.size(); ++i)
        {
            list2.add(list.get(list.size() - 1 - i));
        }

        return list2;
    }
}
