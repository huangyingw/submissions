class MyQueue
{
  Stack<Integer> stack = new Stack<Integer>();
  Stack<Integer> buffer = new Stack<Integer>();

  public void push(int x)
  {
    stack.push(x);
  }

  public void pop()
  {
    if (buffer.isEmpty())
    {
      shiftStacks();
    }

    buffer.pop();
  }

  public int peek()
  {
    if (buffer.isEmpty())
    {
      shiftStacks();
    }

    return buffer.peek();
  }

  private void shiftStacks()
  {
    while (!stack.isEmpty())
    {
      buffer.push(stack.pop());
    }
  }

  public boolean empty()
  {
    return stack.isEmpty();
  }
}

