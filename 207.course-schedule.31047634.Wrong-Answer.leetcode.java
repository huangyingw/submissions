public class Solution
{
    public boolean canFinish(int numCourses, int[][] prerequisites)
    {
        List<Set<Integer>> graph = new ArrayList<Set<Integer>>();
        int[] in = new int[numCourses];

        for (int i = 0; i < numCourses; i++)
        {
            graph.add(new HashSet<Integer>());
        }

        // fill the adjacency list
        for (int i = 0; i < prerequisites.length; i++)
        {
            graph.get(prerequisites[i][1]).add(prerequisites[i][0]);
            ++in[prerequisites[i][0]];
        }

        LinkedList<Integer> queue = new LinkedList<Integer>();

        for (int i = 0; i < numCourses; ++i)
        {
            if (in[i] == 0)
            {
                queue.offer(i);
            }
        }

        while (!queue.isEmpty())
        {
            int t = queue.pop();

            for (Integer a : graph.get(t))
            {
                --in[a];

                if (in[a] == 0)
                {
                    queue.push(a);
                }
            }
        }

        for (int i = 0; i < numCourses; ++i)
        {
            if (in[i] != 0)
            {
                return false;
            }
        }

        return true;
    }
}

