/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution
{
    int kthSmallest(TreeNode root, int k)
    {
        int left = findNodesSum(root.left);
        
        if (left + 1 < k)
        {
            return kthSmallest(root.right, k - left - 1);
        }
        else if (left + 1 > k)
        {
            return kthSmallest(root.left, k);
        }
        else
        {
            return root.val;
        }

    }

    int findNodesSum(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        return findNodesSum(root.left) + findNodesSum(root.right) + 1;
    }
}
