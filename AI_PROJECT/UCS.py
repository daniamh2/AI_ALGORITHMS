 #  uniform_cost_search function  
def uniform_cost_search(start,goal, graph, cost ):
    visited_nodes=[]
    priorityQueue=[(0,[start])] #priorityQueue of costs
    while priorityQueue:
        cst,node = priorityQueue.pop(0)#(less cost)
        v=node[-1]#current node=last child in node 
    
        if v in visited_nodes:
            continue
        visited_nodes.append(v)#set as isited node
        if v == goal:#foun goal
            return (cst,node,visited_nodes,len(visited_nodes))
        for i in graph.get(v,[]):#get v child 
            temp=list(node)
            temp.append(i)
            temp.sort()#get in order
            for e in range(len(cost)):
             if v==cost[e][0] and i==cost[e][1] :#calc cost 
              total_cost=cst + cost[e][2]
            priorityQueue.append((total_cost,temp))#insert in priorityQueue node with cost 
        priorityQueue.sort()#sort in asc order of cost value
       
    return ("","no solution",visited_nodes,len(visited_nodes))


