public class Solution
{
    public List<String> wordBreak(String s, List<String> dict)
    {
        Map<String, List<String>> done = new HashMap<>();
        done.put("", new ArrayList<>());
        done.get("").add("");
        return dfs(s, dict, done);
    }

    List<String> dfs(String s, List<String> dict, Map<String, List<String>> done)
    {
        if (done.containsKey(s))
        {
            return done.get(s);
        }

        List<String> ans = new ArrayList<>();

        for (int len = 1; len <= s.length(); len++)    //将s 分割成s1 s2  其中s1长度为len
        {
            String s1 = s.substring(0, len);
            String s2 = s.substring(len);

            if (dict.contains(s1))
            {
                List<String> s2_res = dfs(s2, dict, done);

                for (String item : s2_res)
                {
                    if (item == "")
                    {
                        ans.add(s1);
                    }
                    else
                    {
                        ans.add(s1 + " " + item);
                    }
                }
            }
        }

        done.put(s, ans);
        return ans;
    }
}

