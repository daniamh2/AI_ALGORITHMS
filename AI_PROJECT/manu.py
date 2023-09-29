#enter graph manually
def manual_graph():
               
        graph = dict()#define graph as dictionary
        def addEdge(node1, node2):
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
        
            graph[node1].append(node2)
        nodes =input("nodes number")
        #enter ndes and edges by user then append edges by addedge fun.
        for _ in range(int(nodes)):
                node1 = int(input("node you want to make their edges"))
                edges = list(map(int, input("Enter multiple values of edges: ").split()))
                
                for i in range(len(edges)):
                  addEdge(node1, edges[i]) 
                       
                  '''' # alp tree
        for _ in range(int(nodes)):
                node1 = (input("node you want to make their edges"))
                edges = list(map(str, input("Enter multiple values of edges: ").split()))
                for i in range(len(edges)):
                  addEdge(node1, edges[i])'''
        print("GRAPH",graph)
        return graph
 