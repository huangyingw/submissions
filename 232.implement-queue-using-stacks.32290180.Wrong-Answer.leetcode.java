class MyQueue
{
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();

    public void push(int x)
    {
        if (empty())
        {
            stack1.push(x);
        }
        else
        {
            if (stack1.size() > 0)
            {
                stack2.push(x);

                while (stack1.size() > 0)
                {
                    stack2.push(stack1.pop());
                }
            }
            else if (stack2.size() > 0)
            {
                stack1.push(x);

                while (stack2.size() > 0)
                {
                    stack1.push(stack2.pop());
                }
            }
        }
    }

    public void pop()
    {
        if (stack1.size() > 0)
        {
            stack1.pop();
        }
        else if (stack2.size() > 0)
        {
            stack2.pop();
        }
    }

    public int peek()
    {
        if (stack1.size() > 0)
        {
            return stack1.peek();
        }
        else if (stack2.size() > 0)
        {
            return stack2.peek();
        }

        return 0;
    }

    public boolean empty()
    {
        return stack1.isEmpty() && stack2.isEmpty();
    }
}

