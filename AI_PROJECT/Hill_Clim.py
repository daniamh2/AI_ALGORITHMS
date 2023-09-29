#hill climbing searh fun.
def Hill_Climbing(graph,start,heuristic,d,g):
    path,PrevNode=[start],[heuristic[start],start]#prevnode to save h,node
    cost=0
    v=[start]#current node= root
    while 1:
       child=graph.get(start,[])
       child.sort()
       PQ=[]
       temp=[]
       if child:
           for i in child :
               if i not in v:
                      v.append(i)#set as visited
               PQ.insert(0,(heuristic[i],i))          
               PQ.sort()  #sort in order of heuristic        
               (H,node)=PQ.pop(0)             

               if H <= PrevNode[0]:
                    PQ=[]
                    child=[]#clear prev child (dont save previous nodes)
                    path.append(node)#calc path
                    for e in range (len(d)):
                                    if  d[e][1] == node :
                                        if d[e][0] == PrevNode[1]: 
                                            cost=cost+ (d[e][2])    #calc cost                              
                    if node==g:#found goal
                            return path,cost,v,len(v) 
                    PrevNode=[H,node]
                    start=node 
                    child=graph.get(start,[])#new child value 
                    child.sort()  
                    break 
                                                         
       else:
               return "no solution"," ",v,len(v)
