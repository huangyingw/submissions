public class Solution
{
    public int evalRPN(String[] tokens)
    {
        int returnValue = 0;
        String operators = "+-*/";
        Stack<String> stack = new Stack<String>();

        for (String token : tokens)
        {
            if (!operators.contains(token)) // push to stack if it is a number
            {
                stack.push(token);
            }
            else // pop numbers from stack if it is an operator
            {
                int a = Integer.valueOf(stack.pop());
                int b = Integer.valueOf(stack.pop());

                switch (token)
                {
                case "+":
                    stack.push(String.valueOf(a + b));
                    break;

                case "-":
                    stack.push(String.valueOf(b - a));
                    break;

                case "*":
                    stack.push(String.valueOf(a * b));
                    break;

                case "/":
                    stack.push(String.valueOf(b / a));
                    break;
                }
            }
        }

        returnValue = Integer.valueOf(stack.pop());
        return returnValue;
    }
}

