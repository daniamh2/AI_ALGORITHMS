#beam search alg.
def beams(start,goal, graph, d ,h,l):
    cost={}
    visited=[]#list visited nodes
    priorityQueue=[(0,[start],0)] #list nodes in h order with its cost
    while priorityQueue:
        g,node,cst = priorityQueue.pop(0)#less h value
        v=node[-1]
        if v in visited:
            continue
        visited.append(v)#set as vsited
        if v == goal:#found goal
         for i in range(len(node)):
          return (c,node,visited,len(visited))
        for i in graph.get(v,[]):#get childs
         if i not in visited:
            temp=list(node)
            temp.append(i)
            H=h[i]
            for e in range(len(d)):
             if v==d[e][0] and i==d[e][1] :
               c=cst+d[e][2]#calc cost
            priorityQueue.append((H,temp,c))
        priorityQueue.sort()
        temp=[]
        temp=priorityQueue
        priorityQueue=[]
        for r in range(l):#save just l nodes in proiarity queue(l length of memory)
          if  temp ==[]:
              continue
          s=temp.pop(0)
          priorityQueue.append(s)
    
    return ("","no solution",visited,len(visited))
