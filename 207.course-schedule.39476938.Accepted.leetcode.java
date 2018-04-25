public class Solution
{
    public boolean canFinish(int numCourses, int[][] prerequisites)
    {
        List<List<Integer>> adjacencyList = new ArrayList<List<Integer>>();
        int[] in = new int[numCourses];

        for (int i = 0; i < numCourses; i++)
        {
            adjacencyList.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < prerequisites.length; i++)
        {
            adjacencyList.get(prerequisites[i][1]).add(prerequisites[i][0]);
            in[prerequisites[i][0]]++ ;
        }

        LinkedList<Integer> queue = new LinkedList<Integer>();

        for (int i = 0; i < in.length; ++i)
        {
            if (in[i] == 0)
            {
                queue.offer(i);
            }
        }

        while (!queue.isEmpty())
        {
            int t = queue.pop();

            for (Integer a : adjacencyList.get(t))
            {
                in[a]-- ;

                if (in[a] == 0)
                {
                    queue.offer(a);
                }
            }
        }

        for (int i = 0; i < in.length; ++i)
        {
            if (in[i] != 0)
            {
                return false;
            }
        }

        return true;
    }
}

