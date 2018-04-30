public class Codec
{
    public String serialize(TreeNode root)
    {
        StringBuilder sb = new StringBuilder();
        buildString(root, sb);
        return sb.toString();
    }

    private void buildString(TreeNode node, StringBuilder sb)
    {
        if (node == null)
        {
            sb.append("null,");
        }
        else
        {
            sb.append(node.val + ",");
            buildString(node.right, sb);
            buildString(node.left, sb);
        }
    }

    public TreeNode deserialize(String data)
    {
        Deque<String> nodes = new LinkedList<>();
        nodes.addAll(Arrays.asList(data.split(",")));
        return buildTree(nodes);
    }

    private TreeNode buildTree(Deque<String> nodes)
    {
        String val = nodes.remove();

        if (val.equals("null"))
        {
            return null;
        }

        TreeNode node = new TreeNode(Integer.valueOf(val));
        node.right = buildTree(nodes);
        node.left = buildTree(nodes);
        return node;
    }
}
