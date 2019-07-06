class MedianFinder
{
    PriorityQueue<Integer> maxheap = new PriorityQueue<Integer>();
    PriorityQueue<Integer> minheap = new PriorityQueue<Integer>(Collections.reverseOrder());
    // Adds a number into the data structure.
    public void addNum(int num)
    {
        maxheap.offer(num);
        minheap.offer(maxheap.poll());

        if (maxheap.size() < minheap.size())
        {
            maxheap.offer(minheap.poll());
        }
    }
    // Returns the median of current data stream
    public double findMedian()
    {
        return maxheap.size() == minheap.size() ? (double)(maxheap.peek() + minheap.peek()) / 2.0 : maxheap.peek();
    }
}
/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
