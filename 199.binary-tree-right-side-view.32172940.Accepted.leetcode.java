public class Solution
{
    public  List<Integer> rightSideView(TreeNode root)
    {
        List<Integer> res = new ArrayList<Integer>();
        dfs(res, root, 0);
        return res;
    }

    public  void dfs(List<Integer> res, TreeNode root, int cur)
    {
        if (root == null)
        {
            return;
        }

        if (res.size() <= cur) // it's ok to add
        {
            res.add(root.val);
        }

        dfs(res, root.right, cur + 1);
        dfs(res, root.left, cur + 1);
    }
}

