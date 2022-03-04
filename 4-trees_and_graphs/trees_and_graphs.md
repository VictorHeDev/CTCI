# Trees and Graphs

Most people are more familiar with trees, even though trees are a type of graph.

### Types of Trees

A tree is a data structure composed of nodes.

- Each tree has a root node
- The root node has zero or more child nodes
- Each child node has zero or more child nodes, and so on

The tree cannot contain cycles. The nodes may or may not be in a particular order, they could have any data types as values, and they may or may not have links back to their parent nodes.

Tree and graph questions typically have a lot of ambiguity, so ask lots of clarifying questions.

### Trees vs. Binary Trees

A binary tree is a tree in which each node has up to two children. Not all trees are binary (2) trees. A node is called a "leaf" node if it has no children.

### Binary Tree vs. Binary Search Tree

By definition, a binary search tree is a binary tree in which every node fits a specific ordering property: all left descendents <= n < all right descendents. This must be true for each node n. This inequality must be true for all of a node's descendents, not just its immediate children.

### Balanced vs. Unbalanced

Complete Binary Trees - binary tree in which every level of the tree is fully filled, except for (maybe) the last level. The nodes are filled from left to right.

Full Binary Trees - binary tree in which every node has either zero or two children. No nodes only have one child.

Perfect Binary Trees - binary tree that is both full and complete. All leaf nodes will be at the same level, and this level has the maximum number of nodes.

### Binary Tree Traversal

Should be comfortable with implementing in-order, post-order, and pre-order traversal. In-order traversal is the most common.

In-order traversal: "visit" the left branch, then the current node, then the right branch.

```python
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node)
        in_order_traversal(node.right)
```

Pre-order traversal: "visits" the current node before its child nodes. In a pre-order traversal, the root is always the first node visited.

```python
def pre_order_traversal(node):
    if node is not None:
        print(node)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
```

Post-order traversal: "visits" the current node after its child nodes. In a post-order-traversal, the root is always the last node visited.

```python
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node)
```

### Binary Heaps (Min-Heaps and Max-Heaps)

Min-heaps: elements are in ascending order. It is a complete binary tree where each node is smaller than its children. Thus, the root node is the minimum element in the tree. Min-heaps have 2 key operations: insert and extract_min.

- Insert: when we insert into a min-heap, we always start by inserting the element at the bottom rightmost spot. Then we "fix" the tree by swapping the new element with its parent, until we find an appropriate spot for the element (bubble up approach).
- Extract_min: remove the minimum element (root element) and swap it with the last element in the heap (bottommost rightmost element). Then bubble/sink down element by swapping with children until the min-heap property is restored.

Max-heaps: elements are in descending order. Same thing as min-heap except the root element is the maximum value of the heap.

### Tries (Prefix Trees)

Trie: variant of an n-ary tree in which characters are stored in each node. Each path down the tree may represent a word. The _ nodes/"null nodes" are used to indicate complete words. The implementation of _ nodes might be a special type of child (such as a TerminatingTrieNode) or a boolean flag.
A true is used to store entire language for quick prefix lookups.

### Graphs

A tree is a type of a graph, but not all graphs are trees. A tree is a connected graph without cycles. Graphs can either be directed (unidirectional) or undirected (bidirectional). A graph might be connected or have multiple isolated subgraphs. A graph can have cycles or be acyclic.

There are 2 common ways to represent a graph:

1. Adjacency List (more common)
2. Adjacency Matrix

### Graph Search

2 most common ways to search a graph are depth-first-search (DFS) and breadth-first-search (BFS).

DFS: explores an entire branch (from root to leaf node) before moving onto next branch. We go deep first, before we go wide. Typically preferred when we want to visit every nod ein the graph, and is a bit simpler to implement.
BFS: start at root and explore each neighbor before going onto any children. We go wide before we go deep. Typically used to find the shortest path between two nodes. BFS is generally better.

When implementing BFS and DFS for a graph, we must keep track if the node has been visited (usually with a "visited" set). If we don't keep track then we risk getting stuck in an infinite loop.

```python
def dfs(root, visited=set()):
    if root is None or root in visited:
        return
    visited.add(root)
    for neighbor in graph[root]:
        dfs(neighbor)
```

```python
from collections import deque
def bfs(root):
    queue = deque([root])
    visited = set()
    while len(queue) > 0:
        current = queue.popleft()
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
```

### Bidirectional Search

Used to find the shortest path between a source and destination node. It operates by essentially running two simultaneous BFS searches, one from each node. When their searches collide, we have found a path.
