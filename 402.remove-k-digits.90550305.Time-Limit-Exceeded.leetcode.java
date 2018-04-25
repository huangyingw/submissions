public class Solution
{
    public String removeKdigits(String A, int k)
    {
        Stack<Integer> stack = new Stack<Integer>();

        for (int i = 0; i < A.length(); i++)
        {
            int num = A.charAt(i) - '0';

            while (!stack.isEmpty() && stack.peek() > num && stack.size() + A.length() - i > A.length() - k)
            {
                stack.pop();
            }

            if (stack.size() + k < A.length())
            {
                System.out.println("stack.size() --> " + stack.size());
                System.out.println("A.length() - k --> " + (A.length() - k));
                System.out.println("k --> " + k);
                System.out.println("num --> " + num);
                stack.push(num);
            }
        }

        StringBuilder sb = new StringBuilder();

        while (!stack.isEmpty())
        {
            sb.append(stack.pop());
        }

        System.out.println("sb -->" + sb);

        while (sb.length() >= 1 && sb.charAt(sb.length() - 1) == '0')
        {
            sb.deleteCharAt(sb.length() - 1);
        }

        if (sb.length() == 0)
        {
            return "0";
        }

        return sb.reverse().toString();
    }
}
