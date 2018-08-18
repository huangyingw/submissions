public class Solution
{
    public int longestValidParentheses(String s)
    {
        int result = 0;
        Stack<Integer> stack = new Stack<Integer>();
        char[] arr = s.toCharArray();

        for (int i = 0; i < arr.length; i++)
        {
            if (arr[i] == ')' && !stack.isEmpty() && arr[stack.peek()] == '(')
            {
                stack.pop();

                if (stack.isEmpty())
                {
                    result = i + 1;
                }
                else
                {
                    result = Math.max(result, i - stack.peek());
                }
            }
            else
            {
                stack.push(i);
            }
        }

        return result;
    }
}
