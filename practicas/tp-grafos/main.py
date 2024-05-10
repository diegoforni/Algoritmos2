class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, parent_key, child_key):
        if self.root is None:
            # If the tree is empty, create a root node with the given child key
            self.root = TreeNode()
            self.root.key = child_key
            return True
        else:
            # Search for the parent node
            parent_node = self._find_node(self.root, parent_key)
            if parent_node:
                # If parent node is found, create a new child node and add it to the parent's children list
                new_child = TreeNode()
                new_child.key = child_key
                if parent_node.children is None:
                    parent_node.children = [new_child]
                else:
                    parent_node.children.append(new_child)
                new_child.parent = parent_node
                return True
            else:
                print("Parent not found.")
                return False

    def _find_node(self, current_node, key):
        # Helper function to find a node with the given key starting from the current node
        if current_node.key == key:
            return current_node
        elif current_node.children:
            for child in current_node.children:
                found_node = self._find_node(child, key)
                if found_node:
                    return found_node
        return None

    def print(self):
        if self.root is None:
            return

        def print_node(node, level=0):
            print("  " * level, end="")
            if node.children is None:
                print(f"{node.key} ({level}) -")
            else:
                print(f"{node.key} ({level})")

            if node.children:
                for child in node.children:
                    print_node(child, level + 1)

        print("Printing tree:")
        print_node(self.root)

class TreeNode:
    def __init__(self):
        self.parent = None
        self.children = None
        self.key = None



graph = {}
def graph_insert(graph, node1, node2):
    if node1 not in graph:
        graph[node1] = []
    graph[node1].append(node2)
    if node2 not in graph:
        graph[node2] = []
    graph[node2].append(node1)
    return graph

def print_graph(graph):
    for node in graph:
        print(f"{node}: {graph[node]}")




def bsf(graph, start):
    tree = Tree()
    visited = []
    queue = []
    current = start
    visited.append(start)
    tree.insert(None, start)
    
    for element in graph[current]: 
        queue.append(element)
        graph[element].remove(current)

    for element in queue:
        tree.insert(start, element)

    while len(queue) > 0:
        current = queue.pop(0)
        for element in graph[current]:
            if element not in visited and element not in queue:
                queue.append(element)
                tree.insert(current, element)
                graph[element].remove(current)

        visited.append(current)
    return tree



# Big O notation of bsf:
# O(V + E) where V is the number of vertices and E is the number of edges. In the worst case, we will visit all the vertices and edges of the graph.
def dfs(graph, start):
    stack = []
    visited = {}
    for node in graph: # O(V)
        visited[node] = False
    stack.append(start)
    tree = Tree()
    tree.insert(None, start)
    visited[start] = True

    while len(stack) > 0:
        current = stack[-1]  # Get the top element of the stack
        next_node = None
        for neighbor in graph[current]:
            if not visited[neighbor]:
                next_node = neighbor
                break
        if next_node is not None:
            stack.append(next_node)
            tree.insert(current, next_node)
            visited[next_node] = True
        else:
            stack.pop()

    return tree




# Big O notation of dfs:
# O(V + E) where V is the number of vertices and E is the number of edges. In the worst case, we will visit all the vertices and edges of the graph.

def detectCycle(graph, start):
    stack = []
    visited = {}
    parent = {}
    
    for node in graph:
        visited[node] = False
        parent[node] = None
    
    stack.append(start)

    while stack:
        current = stack.pop()
        visited[current] = True

        for neighbor in graph[current]:
            if not visited[neighbor]:
                stack.append(neighbor)
                parent[neighbor] = current
            elif parent[current] != neighbor:
                print(f"Cycle detected at node {neighbor}")
                return True
    return False



graphNoCycle = {}
graphNoCycle = graph_insert(graphNoCycle, 1, 5)
graphNoCycle = graph_insert(graphNoCycle, 1, 6)
graphNoCycle = graph_insert(graphNoCycle, 1, 7)
graphNoCycle = graph_insert(graphNoCycle, 7, 2)
graphNoCycle = graph_insert(graphNoCycle, 2, 4)
graphNoCycle = graph_insert(graphNoCycle, 2, 6)
print_graph(graphNoCycle)



print(detectCycle(graphNoCycle, 1))  # False
