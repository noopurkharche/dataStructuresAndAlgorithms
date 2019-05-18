# social network to represent friends 
import sys

#Node class contains the Vertex information.
class Node(object):
        def __init__(self, name):
                self.node_name=name
                self.friends={}

        #Updates adjacent nodes list.
        def update_friends(self, node1, node2):
                node1.friends[node2.node_name] = node2
                node2.friends[node1.node_name] = node1

        #Used for printing Node object value.
        def __str__(self):
                return "%s %s" %(self.node_name, self.friends)

        def canBeConnected(self, node):
                return path_search(self.node_name, node)

def path_search(start_node, end_node):
        fringe =  []    #Sorted list of nodes available to explore.
        visited = []    #List of nodes that have been visited.

        #Add start node to  fringe.
        fringe.append(start_node)

        while True:
                if len(fringe) == 0:
                        break
                #Remove the visited node from fringe. "explored" will be used to set parent value to  it's  adjacent nodes.
                explored = fringe.pop(0)
                if graph[explored].node_name == end_node:
                        return True
                #parent = explored
                visited.append(explored)
                print(" Explored - " + str(graph[explored].node_name))
                print(" Children - " + str(graph[explored].friends))
                #Add adjacent nodes to fringe.
                for child in graph[explored].friends.keys():
                        if child not in visited:
                                fringe.append(child)
        return False

def read_input_file(filename):
    read_file=open(filename,'r')
    return read_file.readlines()

graph = {}
def main(argv):
        # Get input data file for generating graph, start node and end node values.
        input_filename = sys.argv[1]
        start_node = sys.argv[2]
        end_node = sys.argv[3]

        #Read content of the input file.
        file_input_datalist = read_input_file(input_filename)

        print("\n\nSource : %s" %start_node)
        print( "Destination : %s\n" %end_node)

        #Generate graph from the data given in the input file.
        for row in file_input_datalist:
                elements = row.split()
                if not(elements[0]=="END" and elements[1]=="OF" and elements[2]=="INPUT"):
                    if graph.has_key(elements[0]) == False:
                        graph[elements[0]] = Node(elements[0])
                    if graph.has_key(elements[1]) == False:
                        graph[elements[1]] = Node(elements[1])
                    graph[elements[0]].update_friends(graph[elements[0]], graph[elements[1]])

        res = graph[start_node].canBeConnected(end_node)
        print(res)
        
if __name__ == '__main__':
    main(sys.argv)
