public class Solution
{
    public int reverse(int x)
    {
        boolean isNeg = x < 0 ? true : false;
        x = Math.abs(x);
        int result = 0;

        while (x != 0)
        {
            int digit = x % 10;
            x = x / 10;

            if (isNeg == false && result * 10 + digit > Integer.MAX_VALUE)
            {
                return Integer.MAX_VALUE;
            }

            if (isNeg == true  && result * (-10) - digit < Integer.MIN_VALUE)
            {
                return Integer.MIN_VALUE;
            }

            result = result * 10 + digit;
        }

        return isNeg == true ? -result : result ;
    }
}
