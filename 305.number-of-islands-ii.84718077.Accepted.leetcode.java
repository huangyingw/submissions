public class Solution 
{
    private int[][] dir = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    public List<Integer> numIslands2(int m, int n, int[][] positions) 
    {
        UnionFind2D islands = new UnionFind2D(m, n);
        List<Integer> ans = new ArrayList<>();
        
        for (int[] position : positions) 
        {
            int x = position[0], y = position[1];
            int p = islands.add(x, y);
            
            for (int[] d : dir) 
            {
                int q = islands.getID(x + d[0], y + d[1]);
                
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
    private int m, n, count;

    public UnionFind2D(int m, int n) 
    {
        this.count = 0;
        this.n = n;
        this.m = m;
        this.id = new int[m * n + 1];
    }

    public int index(int x, int y) { return x * n + y + 1; }

    public int size() { return this.count; }

    public int getID(int x, int y) 
    {
        if (0 <= x && x < m && 0<= y && y < n)
        {
            return id[index(x, y)];
        }
        
        return 0;
    }

    public int add(int x, int y) 
    {
        int i = index(x, y);
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
        while(i != id[i])
        {
            i = id[i];
        }
        
        return i;
    }
}
