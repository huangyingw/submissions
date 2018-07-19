public class Solution
{
    public ArrayList<ArrayList<Integer>> zigzagLevelOrder(TreeNode root)
    {
        ArrayList<ArrayList<Integer>> ans = new ArrayList<ArrayList<Integer>>();
        traverse(root, 1, ans, true);
        return ans;
    }

    public void traverse(TreeNode root, int level,
                         ArrayList<ArrayList<Integer>> result, Boolean left_to_right)
    {
        if (root == null)
        {
            return;
        }

        if (level > result.size())
        {
            result.add(new ArrayList<Integer>());
        }

        if (left_to_right)
        {
            result.get(level - 1).add(root.val);
        }
        else
        {
            result.get(level - 1).add(0, root.val);
        }

        traverse(root.left, level + 1, result, !left_to_right);
        traverse(root.right, level + 1, result, !left_to_right);
    }
}
