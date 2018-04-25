public class Solution
{
    public  List<Integer> rightSideView(TreeNode root)
    {
        List<Integer> res = new ArrayList<Integer>();

        if (root == null)
        {
            return res;
        }

        dfs(res, root, 0);
        return res;
    }

    public  void dfs(List<Integer> res, TreeNode root, int cur)
    {
        if (res.size() <= cur) // it's ok to add
        {
            res.add(root.val);
        }

        if (root.right != null)
        {
            dfs(res, root.right, cur + 1);
        }

        if (root.left != null)
        {
            dfs(res, root.left, cur + 1);
        }

        return;
    }
}

