class Solution
{
    int kthSmallest(TreeNode root, int k)
    {
        return kthSmallestDFS(root, k);
    }

    int kthSmallestDFS(TreeNode root, Integer k)
    {

        if (root == null)
        {
            return -1;
        }

        int val = kthSmallestDFS(root.left, k);

        if (k == 0)
        {
            return val;
        }

        if (--k == 0)
        {
            return root.val;
        }

        return kthSmallestDFS(root.right, k);
    }
}
