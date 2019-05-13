#Given a directed, acyclic graph of N nodes.  
#Find all possible paths from node 0 to node N-1, and return them in any order.

def allPathsSourceTarget(graph):
        output = []
        print('graph ' + str(graph[0]))
        dfs(graph, len(graph), output, 0, [0])
        print(output)

def dfs(graph, n, output, index, path):
    if index == n or len(graph[index]) == 0:
        output.append(path)
        #print(output)
        return
    # consider one row at a time and do DFS
    for edge in graph[index]:
        dfs(graph, n, output, edge, path+[edge])
    

graph = [[1,2], [3], [3], []]
allPathsSourceTarget(graph)
