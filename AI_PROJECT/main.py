#  Dania Hilal
#bridth first search alg.
def bfs(d,graph,goal):
            cost=0
            root = list(graph.keys())[0]#asssign root value
            #open list  save nodes you want to visit
            open_list, path, visited_nodes = [root], [],  []
            parent = {root: None}       #save nodes parents
            for k in graph.keys():
                 parent[k]=None    
                 
            while open_list:
                v = open_list.pop(0)#v:current node(pop first element)
                if v in visited_nodes:
                    continue#jump to next node
                visited_nodes.append(v)
                if v == goal:#goal founded
                    while goal!=root:
                        path.insert(0, goal)#insert at index 0
                        for e in range(len(d)):#from costs array calc. path cost
                            #find the correct tuple to add cost
                               if  d[e][1] == goal :
                                if d[e][0] == parent[goal]:
                                 cost=cost+ (d[e][2])
                        goal = parent[goal]
                    path.insert(0, root)#finally add the root
                    break      #exit
                temp=[]
                for e in (graph.get(v,[])):#return child of v
                          temp.append(e)#append nodes child 
                          if parent[e]:
                                      continue
                          parent[e] = v      
                temp.sort()#to open in asc. order
                open_list.extend(temp)#add temp to open list
            if path:
               return path,visited_nodes,len(visited_nodes),cost
            return "no solution",visited_nodes,len(visited_nodes)," "
   
   
#random graph function 
def rand_graph(n):
        nodes=[]  #define nodes array     
        graph = dict()#define dictionary to sttore graph
        #enter nodes values
        for i in range(n):
           nodes.append(i)
           graph[i]=[]   
        nodes.pop(0)  
        
        def addEdge( node1, node2):
           if node2 not in graph[node1]:
             if node1 != node2:
              graph[node1].append(node2)
              
        #iterate each node and enter its nodes by add edge
        for x in range (len(nodes)):
                    edges = random.choices(nodes, weights = None, k = random.randint(0,4))
                    edges=sorted(edges)
                    print(i,edges)
                    for i in range(len(edges)):
                     addEdge(x, edges[i])
        print(graph)
        return graph
'''#rand alphapet graph
def rand_agraph(n):
        nodes=[]       
        graph = dict()
        for i in range(n):
           nodes.append(chr(97+i))
           graph[chr(97+i)]=[]     
        def addEdge( node1, node2):
           if node2 not in graph[node1]:
             graph[node1].append(node2)
        
        for x in  (nodes):
                    edges = random.choices(nodes, weights = None, k = random.randint(0,4))
                    print(i,edges)
                    edges=sorted(edges)
                    print(i,edges)
                    for i in range(len(edges)):
                     addEdge(x, edges[i])
        print(graph)
        for key, val in graph.items():
              print(f"{key}-->{val}")
                
        return graph'''
        
#import algorithms files
from DF import*#dfs
from UCS import*
from a_star import*
from GBFS import*
from dls import*
from ids import*
from Hill_Clim import*
from beams import*
from manu import*
from prettytable import PrettyTable
import networkx as nx
import matplotlib.pyplot as plt
import random
G = nx.DiGraph()
x = PrettyTable()
x.field_names=["algorithm","path","visited nodes","visited nodes number","cost"]


i=int(input("How would you like to enter the graph: 1:manual,2:randomly,3:stored?    "))
if i==2:
    graph=rand_graph(9)  
elif i==3:
    graph={0:[1],1:[3,2,4] ,2:[5,6,7],3:[7],4:[7],7:[8],8:[1],5:[],6:[],9:[]}
else:
    graph=manual_graph()

#heuristic array
heuristic={0:40,
    1:30,
    2:14,
    3:14,
    4:18,
    5:7,
    6:9,
    7:2
    ,8:2,
    9:0} 
#assign costs randomly (range 1-30)
d=[]
for key, val in graph.items():
    for e in range(len(graph[key])):
                   d.append((key,val[e],random.randint(1,30)))
print ("costs",d)       
#to draw the graph using networkx lib
for e in range (len(d)):
           G.add_edge(d[e][0],d[e][1],weight=d[e][2])
           

pos = nx.spring_layout(G,k=1, iterations=10)

nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.2')
#add all edges with weights
edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="blue", font_size=6, label_pos=0.4)
plt.show()       #view graph
     
#calling alg. functions
path,visited_nodes,cost,lend= dfs(d,graph,7)
print("found goal  path of dfs :",path,"and visited node :",visited_nodes,lend,cost)
x.add_row(["dfs",path,visited_nodes,lend,cost])#add row of table

path,visited_nodes,len,cost= bfs(d,graph,7)
print("found goal  path of bfs:",path,"and visited node :",visited_nodes,len,cost)
x.add_row(["bfs",path,visited_nodes,len,cost])#add row of table

path,visited,cost,len=dls(graph, 7,4,d)
if path:
    print("found goal  path of dls :",path,"and visited node :",visited,cost)
else:
    print("goal not found visited of dls",visited)
x.add_row(["dls",path,visited,len,cost])#add row of table

goal,limit = 7,7
path,visited,cost,len,l=ids(graph, goal,limit,d)
if path:
    print("found goal  path of ids:",path,"and visited node :",visited,cost,l)
else:
    print("goal not found of ids",visited)
x.add_row(["ids",(path,"in depth" ,l),visited,len,cost])#add row of table

start= d[0][0]
(cost,path,visited,len)=uniform_cost_search(start,7,graph,d)
print(("the cost is :",cost," and the path of ucs is :",path))
x.add_row(["ucs",path,visited,len,cost])#add row of table

cost,path,v,l = beams(start,7,graph,d,heuristic,3)
if path:
    print("found Solution of gbfs:",path,cost,v,l)
x.add_row(["beam search",path,v,l,cost])#add row of table

cost,path,visited,len = GBFS(start,7,graph,d,heuristic)
if path:
    print("found Solution of gbfs:",path,cost)
x.add_row(["gbfs",path,visited,len,cost])#add row of table

visited,path,cost,len = AStarSearch(start,7,graph,d,heuristic)
if path:
    print("found Solution of a*:",path)
    print("and the cost is :",cost)
x.add_row(["a*",path,visited,len,cost])#add row of table

path,c,v,len = Hill_Climbing(graph,start,heuristic,d,7)
print("found Solution of hill climbing:",path,c)
x.add_row(["Hill_Climbing",path,v,len,c])#add row of table

print(x)
print("graph:",graph)
print("cost graph:",d)
print("heuristic:",heuristic)
