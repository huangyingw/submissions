class MyStack
{
    Queue<Integer> queue1 = new LinkedList<Integer>();
    Queue<Integer> queue2 = new LinkedList<Integer>();

    public void push(int x)
    {
        if (empty())
        {
            queue1.offer(x);
        }
        else
        {
            if (queue1.size() > 0)
            {
                queue2.offer(x);

                while (queue1.size() > 0)
                {
                    queue2.offer(queue1.poll());
                }
            }
            else if (queue2.size() > 0)
            {
                queue1.offer(x);

                while (queue2.size() > 0)
                {
                    queue1.offer(queue2.poll());
                }
            }
        }
    }

    public void pop()
    {
        if (queue1.size() > 0)
        {
            queue1.poll();
        }
        else if (queue2.size() > 0)
        {
            queue2.poll();
        }
    }

    public int top()
    {
        if (queue1.size() > 0)
        {
            return queue1.peek();
        }
        else if (queue2.size() > 0)
        {
            return queue2.peek();
        }

        return 0;
    }

    public boolean empty()
    {
        return queue1.isEmpty() && queue2.isEmpty();
    }
}

