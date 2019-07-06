class Solution
{
    int kthSmallest(TreeNode root, int k)
    {
        int left = findNodesSum(root.left);

        if (left + 1 == k)
        {
            return root.val;
        }
        else if (left + 1 < k)
        {
            return kthSmallest(root.right, k - left - 1);
        }
        else
        {
            return kthSmallest(root.left, k);
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
