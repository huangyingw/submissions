/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class Solution 
{  
    class Node 
    {  
        TreeNode node;  
        int column;  
    
        Node(TreeNode node, int column) 
        {  
            this.node = node;  
            this.column = column;  
        }  
    } 
    
    public List<List<Integer>> verticalOrder(TreeNode root) 
    {  
        List<List<Integer>> results = new ArrayList<>();  
        
        if (root == null) 
        {
            return results;  
        }
        
        Map<Integer, List<Integer>> map = new HashMap<>();  
        LinkedList<Node> queue = new LinkedList<>();  
        queue.add(new Node(root, 0));  
        
        while (!queue.isEmpty()) 
        {  
            Node node = queue.remove();  
            List<Integer> list = map.get(node.column);  
            
            if (list == null) 
            {  
                list = new ArrayList<>();  
                map.put(node.column, list);  
            }  
            
            list.add(node.node.val);  
            
            if (node.node.left != null)
            {
                queue.add(new Node(node.node.left, node.column-1));  
            }
            
            if (node.node.right != null) 
            {
                queue.add(new Node(node.node.right, node.column+1));  
            }
        }  
        
        List<Integer> columns = new ArrayList<>(map.keySet());  
        Collections.sort(columns);  
        
        for(int i=0; i<columns.size(); i++) 
        {  
            results.add(map.get(columns.get(i)));  
        }  
        
        return results;  
    }  
}
