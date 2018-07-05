public class Solution
{
    public String reverseWords(String s)
    {
        StringBuilder sb = new StringBuilder(s.trim().replaceAll(" +", " "));
        reverse(sb, 0, sb.length() - 1);

        for (int begin = 0, end = 0; end < sb.length(); end++)
        {
            System.out.printf("%s --> %s\n", end, sb.charAt(end));

            if (end == sb.length() || sb.charAt(end) == ' ')
            {
                reverse(sb, begin, end - 1);
                begin = end + 1;
                System.out.printf("%s --> %s\n", begin, sb.charAt(begin));
            }
        }

        return sb.toString();
    }

    public void reverse(StringBuilder sb, int begin, int end)
    {
        for (; begin < end; begin++, end--)
        {
            char temp = sb.charAt(begin);
            sb.setCharAt(begin, sb.charAt(end));
            sb.setCharAt(end, temp);
        }
    }
}

