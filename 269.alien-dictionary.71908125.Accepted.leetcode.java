public class Solution
{
    public String alienOrder(String[] words)
    {
        // Step 1: build the graph
        Map<Character, Set<Character>> graph = new HashMap<>();

        for (int i = 0; i < words.length; i++)
        {
            String current = words[i];

            for (int j = 0; j < current.length(); j++)
            {
                if (!graph.containsKey(current.charAt(j)))
                {
                    graph.put(current.charAt(j), new HashSet<Character>());
                }
            }

            if (i > 0)
            {
                connectGraph(graph, words[i - 1], current);
            }
        }

        // Step 2: toplogical sorting
        StringBuffer sb = new StringBuffer();
        Map<Character, Integer> visited = new HashMap<Character, Integer>();
        Iterator it = graph.entrySet().iterator();

        while (it.hasNext())
        {
            Map.Entry pair = (Map.Entry) it.next();
            char vertexId = (char) pair.getKey();

            if (toplogicalSort(vertexId, graph, sb, visited) == false)
            {
                return "";
            }
        }

        return sb.toString();
    }
    private void connectGraph(Map<Character, Set<Character>> graph, String prev, String current)
    {
        if (prev == null || current == null)
        {
            return;
        }

        int len = Math.min(prev.length(), current.length());

        for (int i = 0; i < len; i++)
        {
            char p = prev.charAt(i);
            char q = current.charAt(i);

            if (p != q)
            {
                if (!graph.get(p).contains(q))
                {
                    graph.get(p).add(q);
                }

                break;
            }
        }
    }
    private boolean toplogicalSort(char vertexId, Map<Character, Set<Character>> graph, StringBuffer sb,
                                   Map<Character, Integer> visited)
    {
        if (visited.containsKey(vertexId))
        {
            // visited
            if (visited.get(vertexId) == -1)
            {
                return false;
            }

            // already in the list
            if (visited.get(vertexId) == 1)
            {
                return true;
            }
        }
        else
        {
            // mark as visited
            visited.put(vertexId, -1);
        }

        Set<Character> neighbors = graph.get(vertexId);

        for (char neighbor : neighbors)
        {
            if (toplogicalSort(neighbor, graph, sb, visited) == false)
            {
                return false;
            }
        }

        sb.insert(0, vertexId);
        visited.put(vertexId, 1);
        return true;
    }
}
