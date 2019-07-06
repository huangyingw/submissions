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
        preorderTraversal(root, preorder);
        return preorder;
    }
    public void preorderTraversal(TreeNode root, List preorder)
    {
        if (root == null)
        {
            return;
        }

        preorder.add(root.val);
        preorderTraversal(root.left, preorder);
        preorderTraversal(root.right, preorder);
    }
}
