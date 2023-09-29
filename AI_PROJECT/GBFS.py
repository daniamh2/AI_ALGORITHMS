#greedy best first search alg.
def GBFS(start,goal, graph, d ,h):
    cost={}
    visited=[]#list visited nodes
    priorityQueue=[(0,[start],0)] #sort in h order
    while priorityQueue:
        g,node,cst = priorityQueue.pop(0)
        v=node[-1]#node with less h value
        if v in visited:
            continue
        visited.append(v)#set as visited
        if v == goal: #found goal  
         for i in range(len(node)):
          return (c,node,visited,len(visited))
        for i in graph.get(v,[]):#get v child
            temp=list(node)
            temp.append(i)#append childs
            H=h[i]
            for e in range(len(d)):
             if v==d[e][0] and i==d[e][1] :
               c=cst+d[e][2]#calc cost 
            priorityQueue.append((H,temp,c))#save node and value with its cost in pq
            
        priorityQueue.sort()   #sort  priorityQueue depending on h
    return ("","no solution",visited,len(visited))
