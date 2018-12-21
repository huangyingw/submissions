<<< <<< < Updated upstream
public class Solution
{
    public List<String> generateAbbreviations(String word)
    == == == =
        public class Solution
    {
        public List<String> generateAbbreviations(String word)
        >>> >>> > Stashed changes
        {
            List<String> result = new ArrayList<String>();
            dfs(0, word.toCharArray(), new StringBuffer(), 0, result);
            return result;
        }
        <<< <<< < Updated upstream

        public void dfs(int pos, char[] word, StringBuffer sb, int count, List<String> result)
        {
            int len = word.length;
            int sbOriginSize = sb.length();

            if (pos == len)
            {
                if (count > 0)
                {
                    sb.append(count);
                }

                result.add(sb.toString());
            }
            else
            {
                //choose to abbr word[pos]
                dfs(pos + 1, word, sb, count + 1, result);

                //choose not to abbr word[pos]
                //first append previous count to sb if count>0
                if (count > 0)
                {
                    sb.append(count);
                }

                sb.append(word[pos]);
                dfs(pos + 1, word, sb, 0, result);
            }

            == == == =
                public void dfs(int pos, char[] word, StringBuffer sb, int count, List<String> result)
            {
                int len = word.length;
                int sbOriginSize = sb.length();

                if (pos == len)
                {
                    if (count > 0)
                    {
                        sb.append(count);
                    }

                    result.add(sb.toString());
                }
                else
                {
                    //choose to abbr word[pos]
                    dfs(pos + 1, word, sb, count + 1, result);

                    //choose not to abbr word[pos]
                    //first append previous count to sb if count>0
                    if (count > 0)
                    {
                        sb.append(count);
                    }

                    sb.append(word[pos]);
                    dfs(pos + 1, word, sb, 0, result);
                }

                >>> >>> > Stashed changes
                sb.setLength(sbOriginSize);
            }
        }
