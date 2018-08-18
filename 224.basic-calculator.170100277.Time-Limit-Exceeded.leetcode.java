public class Solution
{
    public int calculate(String s)
    {
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(1);
        stack.push(1);
        int result = 0;

        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);

            if (Character.isDigit(c))
            {
                int num = c - '0';

                while (i + 1 < s.length() && Character.isDigit(s.charAt(i + 1)))
                {
                    num = 10 * num + (s.charAt(++i) - '0');
                }

                result += stack.pop() * num;
            }
            else if (c == '+' || c == '(')
            {
                stack.push(stack.peek());
            }
            else if (c == '-')
            {
                stack.push(-1 * stack.peek());
            }
            else if (c == ')')
            {
                stack.pop();
            }
        }

        return result;
    }
}
