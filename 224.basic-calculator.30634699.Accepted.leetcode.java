public class Solution
{
    public int calculate(String s)
    {
        Stack<Integer> stack = new Stack<>();
        int res = 0;
        int sign = 1;
        int curSign = 1;

        for (int i = 0; i < s.length(); i++)
        {
            if (s.charAt(i) == '(')
            {
                if (i > 0 && s.charAt(i - 1) == '-')
                {
                    stack.push(-1);
                }
                else
                {
                    stack.push(1);
                }

                sign *= stack.peek();
                curSign = 1;
            }
            else if (s.charAt(i) == ')')
            {
                sign /= stack.pop();
            }
            else if (s.charAt(i) >= '0' && s.charAt(i) <= '9')
            {
                int curNum = 0;

                while (i < s.length() && s.charAt(i) >= '0' && s.charAt(i) <= '9')
                {
                    curNum = curNum * 10 + s.charAt(i) - '0';
                    i++;
                }

                res += sign * curSign * curNum;
                i--;
            }
            else if (s.charAt(i) == '+')
            {
                curSign = 1;
            }
            else if (s.charAt(i) == '-')
            {
                curSign = -1;
            }
        }

        return res;
    }
}
