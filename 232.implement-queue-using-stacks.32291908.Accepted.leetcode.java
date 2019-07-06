class MyQueue
{
    Stack<Integer> stack = new Stack<Integer>();
    Stack<Integer> buffer = new Stack<Integer>();
    public void push(int x)
    {
        if (empty())
        {
            stack.push(x);
        }
        else
        {
            while (stack.size() > 0)
            {
                buffer.push(stack.pop());
            }

            stack.push(x);

            while (buffer.size() > 0)
            {
                stack.push(buffer.pop());
            }
        }
    }
    public void pop()
    {
        stack.pop();
    }
    public int peek()
    {
        return stack.peek();
    }
    public boolean empty()
    {
        return stack.isEmpty();
    }
}
