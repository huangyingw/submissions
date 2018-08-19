public class Solution
{
    public int[] findFrequentTreeSum(TreeNode root)
    {
        if (root == null)
        {
            return new int[0];
        }

        Map<Integer, Integer> map = new HashMap<>();
        treeSum(map, root);
        int max = Integer.MIN_VALUE;
        int count = 0;

        for (int key : map.keySet())
        {
            if (map.get(key) > max)
            {
                max = map.get(key);
                count = 1;
            }
            else if (map.get(key) == max)
            {
                count++;
            }
        }

        int[] result = new int[count];
        count = 0;

        for (int key : map.keySet())
        {
            if (map.get(key) == max)
            {
                result[count++] = key;
            }
        }

        return result;
    }

    public int treeSum(Map<Integer, Integer> map, TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }
        else
        {
            root.val = root.val + treeSum(map, root.left) + treeSum(map, root.right);

            if (map.containsKey(root.val))
            {
                map.put(root.val, map.get(root.val) + 1);
            }
            else
            {
                map.put(root.val, 1);
            }

            return root.val;
        }
    }
}
