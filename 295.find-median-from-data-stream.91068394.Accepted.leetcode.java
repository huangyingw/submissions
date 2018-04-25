class MedianFinder
{
    PriorityQueue<Integer> maxheap = new PriorityQueue<Integer>();
    PriorityQueue<Integer> minheap = new PriorityQueue<Integer>(Collections.reverseOrder());

    public void addNum(int num)
    {
        minheap.offer(num);
        maxheap.offer(minheap.poll());

        if (maxheap.size() > minheap.size() + 1)
        {
            minheap.offer(maxheap.poll());
        }
    }

    public double findMedian()
    {
        return maxheap.size() == minheap.size() ? (double)(maxheap.peek() + minheap.peek()) / 2.0 : maxheap.peek();
    }
}
