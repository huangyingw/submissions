public class Solution
{
    private int[][] dir = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
    public List<Integer> numIslands2(int m, int n, int[][] positions)
    {
        UnionFind2D islands = new UnionFind2D(m * n);
        List<Integer> ans = new ArrayList<>();

        for (int[] position : positions)
        {
            int x = position[0], y = position[1];
            int p = islands.add(x * n + y);

            for (int[] d : dir)
            {
                int q = islands.getID((x + d[0]) * n + y + d[1]);

                if (q > 0 && !islands.find(p, q))
                {
                    islands.unite(p, q);
                }
            }

            ans.add(islands.size());
        }

        return ans;
    }
}
class UnionFind2D
{
    private int[] id;
    private int count;
    public UnionFind2D(int size)
    {
        this.count = 0;
        this.id = new int[size];
    }
    public int size()
    {
        return this.count;
    }
    public int getID(int index)
    {
        return id[index];
    }
    public int add(int i)
    {
        id[i] = i;
        ++count;
        return i;
    }
    public boolean find(int p, int q)
    {
        return root(p) == root(q);
    }
    public void unite(int p, int q)
    {
        int i = root(p);
        int j = root(q);
        id[i] = j;
        --count;
    }
    private int root(int i)
    {
        while (i != id[i])
        {
            i = id[i];
        }

        return i;
    }
}
