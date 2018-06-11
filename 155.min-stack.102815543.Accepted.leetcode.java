class MinStack
{
    private Stack<Integer> data = new Stack<Integer>();
    private Stack<Integer> min = new Stack<Integer>();
    
    public void push(int x)
    {
        data.push(x);

        if (min.empty() || x <= min.peek())
        {
            min.push(x);
        }
    }

    public void pop()
    {
        int temp = data.pop();

        if (temp == min.peek())
        {
            min.pop();
        }
    }

    public int top()
    {
        return data.peek();
    }

    public int getMin()
    {
        return min.peek();
    }
}
