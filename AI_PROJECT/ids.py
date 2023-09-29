#iterative deeping search alg
def df(graph,goal,limit,d):

    root = list(graph.keys())[0]#root value
    #open list list nodes you want to visit
    open_list, temp, path, visited_nodes = [(root,1)], [], [], []
    parent = {root: None}#dict of node and its parent
    cost=0
    for k in graph.keys():
                 parent[k]=None     
    while open_list:
        v,l = open_list.pop()    #node and depth            
        if v in visited_nodes:
                    continue
        visited_nodes.append(v)#set as visited
        if v == goal:#found goal
            while goal!=root:#iterate of all path by assigning the goal to parent until reach to root
                path.insert(0, goal)
                for e in range (len(d)):
                               if  d[e][1] == goal :
                                if d[e][0] == parent[goal]:
                                 cost=cost+ (d[e][2])#calc cost
                goal = parent[goal]
            path.insert(0, root)#finally add root
            break

        for i in graph.get(v,[]):
            if i not in visited_nodes and l < limit:#less than limit then add to open list
                 temp.append(i)
                 parent[i] = v
        while temp:
            temp=sorted(temp)
            open_list.append((temp.pop(),l+1))#save node with its depth
       
    return path,visited_nodes,cost,len(visited_nodes)
def ids(graph, goal,limit,d):
       
    for i in range(1,limit):#its like dfs each time increase the limit until find goal
    
     path,visited,cost,l=df(graph, goal,i,d)
     if path :
        print("found goal  path :",path,"and visited node :",visited,cost,i)
        break
    else:
        print("goal not found",visited)
    return path,visited,cost,l,i



