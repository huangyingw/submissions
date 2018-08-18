public class Solution
{
    public  List<Integer> rightSideView(TreeNode root)
    {
        List<Integer> result = new ArrayList<Integer>();
        dfs(result, root, 0);
        return result;
    }

    public  void dfs(List<Integer> result, TreeNode root, int cur)
    {
        if (root == null)
        {
            return;
        }

        if (result.size() <= cur) // it's ok to add
        {
            result.add(root.val);
        }

        dfs(result, root.right, cur + 1);
        dfs(result, root.left, cur + 1);
    }
}
