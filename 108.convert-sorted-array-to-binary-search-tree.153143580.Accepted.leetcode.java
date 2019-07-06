public class Solution
{
    private TreeNode sortedArrayToBST(int[] num, int left, int right)
    {
        if (left > right || left < 0 || right < 0)
        {
            return null;
        }

        int mid = left + (right - left) / 2;
        TreeNode node = new TreeNode(num[mid]);
        node.left = sortedArrayToBST(num, left, mid - 1);
        node.right = sortedArrayToBST(num, mid + 1, right);
        return node;
    }
    public TreeNode sortedArrayToBST(int[] num)
    {
        return sortedArrayToBST(num, 0, num.length - 1);
    }
}
