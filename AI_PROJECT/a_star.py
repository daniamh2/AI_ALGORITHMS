# a star seach algo.
def AStarSearch(start,goal, graph, cost ,h):
    visited=[]
    priorityQueue=[(0,[start])] #depending on g+h 
    while priorityQueue:
        cst,node = priorityQueue.pop(0)#node with less value of g+h
        v=node[-1]#last child reached
        if len(node)!=1 :
          cst=cst-h[node[-1]]
        if v in visited:
            continue
        visited.append(v)#set as visited
        if v == goal:#found goal
            return (visited,node,cst,len(visited))
        g=graph.get(v,[])#find childs
        g.sort()#open in asc order of nodes
        for i in g:
            temp=list(node)
            temp.append(i)
            for e in range(len(cost)):
             if v==cost[e][0] and i==cost[e][1] :
              COST=cst+ cost[e][2]
              G_h=COST+h[i]#g+h value
            priorityQueue.append((G_h,temp))
        priorityQueue.sort()

    return (visited,"no solution"," ",len(visited))

