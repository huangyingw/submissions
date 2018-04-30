/**
 * Definition for binary tree
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
        ArrayList<Integer> preorder = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();

        if (root != null)
        {
            stack.push(root);

            while (!stack.isEmpty())
            {
                TreeNode p = stack.pop();

                while (p != null)
                {
                    preorder.add(p.val);

                    if (p.right != null)
                    {
                        stack.push(p.right);
                    }

                    p = p.left;
                }
            }
        }

        return preorder;
    }
}
