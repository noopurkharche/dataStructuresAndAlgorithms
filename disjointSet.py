#Complexity = O(number of operation * g(number of element))
#For practical problems g(number of element) function is <= 4. Thus Complexity = O(number of operations * 4)

class Node:
    def __init__(self, element):
        self.node_name = element
        self.parent = element
        self.rank = 0

class DisjointSets:
    def __init__(self):
        self.sets = {}

    def make_sets(self, element):
        node = Node(element)
        self.sets[element] = node

    def find_set(self, vertex):
        node = self.sets[vertex]
        if node.parent != vertex:
            node.parent = self.find_set(node.parent)
        return node.parent

    def union(self, vertex1, vertex2):
        node1 = self.sets[self.find_set(vertex1)]
        node2 = self.sets[self.find_set(vertex2)]

        if node1.rank > node2.rank:
		
            node2.parent = node1.node_name
        else:
            node1.parent = node2.node_name
            if node1.rank == node2.rank:
                node2.rank += 1

def main():
     set_container = DisjointSets()
     for i in range(1, 8):
         set_container.make_sets(i)

     set_container.union(1, 2)
     set_container.union(2, 3)
     set_container.union(4, 5)
     set_container.union(6, 7)
     set_container.union(5, 6)
     set_container.union(3, 7)

     print(set_container.sets[4].parent)
     print(set_container.find_set(4))
     print(set_container.sets[4].parent)

 if __name__ == "__main__":
     main()
