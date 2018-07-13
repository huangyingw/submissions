public class Solution
{
    public String convertToTitle(int n)
    {
        if (n <= 0)
        {
            throw new IllegalArgumentException("Input is not valid!");
        }

        StringBuilder sb = new StringBuilder();

        while (n > 0)
        {
            char ch = (char)(--n % 26 + 'A');
            sb.append(ch);
            n /= 26;
        }

        sb.reverse();
        return sb.toString();
    }
}
