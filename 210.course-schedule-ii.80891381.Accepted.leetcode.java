public class Solution
{
    boolean impossible = false;
    public int[] findOrder(int numCourses, int[][] prerequisites)
    {
        Stack<Integer> stack = new Stack<>();
        List<List<Integer>> graph = new ArrayList<>();
        int[] path = new int[numCourses];

        for (int i = 0; i < numCourses; i++)
        {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < prerequisites.length; i++)
        {
            graph.get(prerequisites[i][0]).add(prerequisites[i][1]);
        }

        for (int i = 0; i < numCourses; i++)
        {
            dfs(stack, graph, path, i);

            if (impossible)
            {
                return new int[0];
            }
        }

        int[] res = new int[numCourses];

        for (int i = numCourses - 1; i >= 0; i--)
        {
            res[i] = stack.pop();
        }

        return res;
    }
    private void dfs(Stack<Integer> stack, List<List<Integer>> graph, int[] path, int course)
    {
        if (path[course] == 2 || impossible)
        {
            return;
        }

        if (path[course] == 1)
        {
            impossible = true;
            return;
        }

        path[course] = 1;

        for (int nextCourse : graph.get(course))
        {
            dfs(stack, graph, path, nextCourse);

            if (impossible)
            {
                return;
            }
        }

        stack.push(course);
        path[course] = 2;
    }
}
