/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution
{
    public List<Integer> preorderTraversal(TreeNode root)
    {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List preorder = new ArrayList();

        if (root == null)
        {
            return preorder;
        }

        stack.push(root);

        while (!stack.isEmpty())
        {
            TreeNode current = stack.pop();
            preorder.add(current.val);

            if (current.right != null)
            {
                stack.push(current.right);
            }

            if (current.left != null)
            {
                stack.push(current.left);
            }
        }

        return preorder;
    }
}
