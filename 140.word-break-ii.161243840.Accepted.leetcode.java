public class Solution
{
    // 我们用DFS来解决这个问题吧
    public static List<String> wordBreak(String s, List<String> dict)
    {
        if (s == null || s.length() == 0 || dict == null)
        {
            return null;
        }

        List<String> ret = new ArrayList<String>();
        List<String> path = new ArrayList<String>();
        int len = s.length();
        // i: 表示从i索引开始的字串可以word break.
        boolean[] D = new boolean[len + 1];
        D[len] = true;

        for (int i = len - 1; i >= 0; i--)
        {
            for (int j = i; j <= len - 1; j++)
            {
                // 左边从i 到 j
                D[i] = false;

                if (D[j + 1] && dict.contains(s.substring(i, j + 1)))
                {
                    D[i] = true;
                    break;
                }
            }
        }

        dfs4(s, dict, path, ret, 0, D);
        return ret;
    }

    public static void dfs4(String s, List<String> dict, List<String> path, List<String> ret, int index, boolean canBreak[])
    {
        int len = s.length();

        if (index == len)
        {
            // 结束了。index到了末尾
            StringBuilder sb = new StringBuilder();

            for (String str : path)
            {
                sb.append(str);
                sb.append(" ");
            }

            // remove the last " "
            sb.deleteCharAt(sb.length() - 1);
            ret.add(sb.toString());
            return;
        }

        // if can't break, we exit directly.
        if (!canBreak[index])
        {
            return;
        }

        for (int i =  index; i < len; i++)
        {
            // 注意这些索引的取值。左字符串的长度从0到len
            String left = s.substring(index, i + 1);

            if (!dict.contains(left))
            {
                // 如果左字符串不在字典中，不需要继续递归
                continue;
            }

            // if can't find any solution, return false, other set it
            // to be true;
            path.add(left);
            dfs4(s, dict, path, ret, i + 1, canBreak);
            path.remove(path.size() - 1);
        }
    }
}

