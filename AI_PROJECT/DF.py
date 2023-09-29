#depth first search alg.
def dfs(d,graph,goal):
    root = list(graph.keys())[0]
     #open list  save nodes you want to visit
    open_list, temp, path, visited_nodes = [root], [], [], []
    parent = {root: None}#save nodes parents
    cost=0
    while open_list:
        v = open_list.pop()#v:current node (pop the last element)
        if v in visited_nodes:
                    continue#jump to next node
        visited_nodes.append(v)#set as visited
        if v == goal:#goal founded
            while goal!=root:
                path.insert(0, goal)#insert at index 0
                for e in range(len(d)):#from costs array calc. path cost
                  if  d[e][1] == goal :
                    if d[e][0] == parent[goal]:
                                 cost=cost+ (d[e][2])           
                goal = parent[goal]#to loop at all path nodes
            path.insert(0, root)#finally add the root
            break
        for i in graph.get(v,[]):#get v child
            if i not in visited_nodes:#add to open list
                 temp.append(i)
                 parent[i] = v
                 temp=sorted(temp)#to open in asc order
        while temp:
            open_list.append(temp.pop())
    if path:
      return path,visited_nodes,cost,len(visited_nodes)
    return "no solution",visited_nodes," ",len(visited_nodes)
                                        

  
