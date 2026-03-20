/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        Map<Integer, Node> memory = new HashMap<>();
        return clone(memory, node);
    }


    private Node clone(Map<Integer, Node> map, Node node){
        if(node == null){
            return null;
        }
        Node chosen;
        if(map.containsKey(node.val)){
            return map.get(node.val);
        } else {
            chosen = new Node(node.val);
            map.put(node.val, chosen);
        }


        for(Node child : node.neighbors){
            Node clonedChild = clone(map, child);
            chosen.neighbors.add(clonedChild);
        }

        return chosen;
    }
}