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
    public List<Integer> postorderTraversal(TreeNode root)
    {
        List<Integer> result = new ArrayList<Integer>();
        dfs(root, result);
        return result;
    }
    public void dfs(TreeNode root, List<Integer> result)
    {
        dfs(root.left, result);
        dfs(root.right, result);
        result.add(root.val);
    }
}
