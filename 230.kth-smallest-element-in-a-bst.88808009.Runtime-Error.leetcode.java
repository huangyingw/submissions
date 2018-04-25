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
    private int count = 0;
    private int result = -1;

    public int kthSmallest(TreeNode root, int k)
    {
        count = 0;
        inorderTraversal(root, k);
        return result;
    }

    private void inorderTraversal(TreeNode root, int k)
    {
        inorderTraversal(root.left, k);
        
        if (++count == k)
        {
            result = root.val;
        }
        
        inorderTraversal(root.right, k);
    }
}
