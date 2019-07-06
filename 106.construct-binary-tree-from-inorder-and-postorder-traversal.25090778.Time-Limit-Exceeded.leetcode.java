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
    public TreeNode helper(HashMap inMap, int[] inorder, int il, int ir, int[] postorder, int pl, int pr)
    {
        if (pr < 0)
        {
            return null;
        }

        TreeNode root = new TreeNode(postorder[pr]);
        int im = (int)inMap.get(postorder[pr]);
        root.left = helper(inMap, inorder, il, im - 1, postorder, pl, pl + im - 1 - il);
        root.right = helper(inMap, inorder, im + 1, ir, postorder, pl + im - il, pr - 1);
        return root;
    }
}
