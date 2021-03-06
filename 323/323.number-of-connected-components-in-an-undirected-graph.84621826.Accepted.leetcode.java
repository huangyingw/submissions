public class Solution 
{
    public int countComponents(int n, int[][] edges) 
    {
        unionFind uf = new unionFind(n);
        
        for (int[] edge : edges) 
        {
            if (!uf.isConnected(edge[0], edge[1])) 
            {
                uf.union(edge[0], edge[1]);
            }
        }
        
        return uf.findCount();
    }
    
    public class unionFind
    {
        int[] ids;
        int count;
            
        public unionFind(int num) 
        {
            this.ids = new int[num];
            
            for (int i = 0; i < num; i++) 
            {
                ids[i] = i;
            }
            
            this.count = num;
        }
            
        public int find(int i) 
        {
            while(i != ids[i])
            {
                i = ids[i];
            }
            
            return i;
        }
            
        public void union(int i1, int i2) 
        {
            int id1 = find(i1);
            int id2 = find(i2);
            
            if(id1 == id2)
            {
                return;
            }
            
            ids[id1] = id2;
            count--;
        }
            
        public boolean isConnected(int i1, int i2) 
        {
            return find(i1) == find(i2);
        }
            
        public int findCount() 
        {
            return count;
        }
    }
}
