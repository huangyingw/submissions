public class Solution
{
    public TreeNode buildTree(int[] inorder, int[] postorder)
    {
        HashMap inMap = new HashMap();

        for (int i = 0; i < inorder.length; i++)
        {
            inMap.put(inorder[i], i);
        }

        TreeNode root = helper(inMap, inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1);
        return root;
    }
    public TreeNode helper(HashMap inMap, int[] inorder, int inLeft, int inRight, int[] postorder, int poLeft, int poRight)
    {
        if (poRight < 0)
        {
            return null;
        }

        if (poLeft == poRight)
        {
            return new TreeNode(postorder[poRight]);
        }

        TreeNode root = new TreeNode(postorder[poRight]);
        int im = (int)inMap.get(postorder[poRight]);
        root.left = helper(inMap, inorder, inLeft, im - 1, postorder, poLeft, poLeft + im - 1 - inLeft);
        root.right = helper(inMap, inorder, im + 1, inRight, postorder, poLeft + im - inLeft, poRight - 1);
        return root;
    }
}
