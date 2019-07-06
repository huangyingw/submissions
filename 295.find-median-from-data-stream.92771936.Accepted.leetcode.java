class MedianFinder
{
    PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
    PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(Collections.reverseOrder());
    public void addNum(int num)
    {
        minHeap.offer(num);
        maxHeap.offer(minHeap.poll());

        while (maxHeap.size() > minHeap.size() + 1)
        {
            minHeap.offer(maxHeap.poll());
        }
    }
    public double findMedian()
    {
        if (maxHeap.size() > minHeap.size())
        {
            return maxHeap.peek();
        }
        else
        {
            return ((double)minHeap.peek() + (double)maxHeap.peek()) / 2;
        }
    }
}
