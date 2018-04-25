public class Solution 
{
    public String removeKdigits(String A, int k) 
    {
        Stack<Integer> stack = new Stack<Integer>();
        
        for (char c : A.toCharArray())
        {
            int num = c - '0';
            
            while (!stack.isEmpty() && stack.peek() > num && k-- > 0)
            {
                stack.pop();
            }
            
            stack.push(num);
        }
        
        StringBuilder sb = new StringBuilder();
        
        while (!stack.isEmpty())
        {
            sb.append(stack.pop());    
        }
        
        while (sb.charAt(sb.length() - 1) == '0')
        {
            sb.deleteCharAt(sb.length() - 1);    
        }
        
        return sb.reverse().toString();
    }
}