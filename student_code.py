class Node:
    def __init__(self,value,dist,prev=None):
        self.value=value
        self.dist=dist
        self.prev=prev
        
def calc_dis(neigh,M,goal,value):
    
#     heuristic_dist=((M.intersections[neigh][0]-M.intersections[goal][0])**2+(M.intersections[neigh][1]-M.intersections[goal][1])**2)**(0.5)
    heuristic_dist=abs(M.intersections[neigh][0]-M.intersections[goal][0])+abs(M.intersections[neigh][1]-M.intersections[goal][1])
    euc_dist=((M.intersections[neigh][0]-M.intersections[value][0])**2+(M.intersections[neigh][1]-M.intersections[value][1])**2)**(0.5)
    tdist=heuristic_dist+euc_dist
    return tdist
        
def shortest_path(M,start,goal):
    start_node=Node(start,0,None)
    open_list=[]
    close_list=[]
    open_list.append(start_node)
    while len(open_list)>0:

        current_node=open_list[0]
        for i in open_list:
            if i.dist<current_node.dist:
                current_node=i

        open_list.remove(current_node)
        close_list.append(current_node)
        
        if current_node.value==goal:
            path=[]
            while current_node!=None:
                path.append(current_node.value)
                current_node=current_node.prev
            return path[::-1]
        for neigh in M.roads[current_node.value]:
            flag=0
            flagclose=0
            dist=calc_dis(neigh,M,goal,current_node.value)
            child_node=Node(neigh,dist,current_node)
            for close_node in close_list:
                if close_node.value==child_node.value:
                    flagclose=1
                    continue
            for open_node in open_list:
                if open_node.value==child_node.value:
                    flag=1
                    if open_node.dist<child_node.dist:
                        continue
                
            
            if flag==0 and flagclose==0:
                open_list.append(child_node)

    return -1
                
        
    
############################experiments################################################################    




# def shortest_path(M,start,goal):
#     print("called")
#     frontier=[]
#     explored=[]
#     frontier.append(start)
#     path=[]
#     dist={}
#     g_dist={}
#     heuristic_dist=((M.intersections[start][0]-M.intersections[goal][0])**2+(M.intersections[start][1]-M.intersections[goal][1])**2)**(0.5)
#     g_dist[start]=0
#     dist[start]=g_dist[start]+heuristic_dist
#     for i in range(10):
# #         for i in frontier:
#         next_node=min(dist, key=dist.get)
#         if next_node==goal:
#             path.append(next_node)
#             return path
# #         if next_node in frontier:
#         print(next_node)
#         frontier.remove(next_node)
#         explored.append(next_node)
#         for neighbour in M.roads[next_node]:
#             if neighbour in explored:
#                 continue
#             tempg=gd(neighbour,next_node,M)+g_dist[next_node]
#             if neighbour in frontier:
#                 if tempg<dist[neighbour]:
#                     path.append(next_node)
# #                     g_dist[neighbour]=tempg
#                     dist[neighbour]=tempg+find_h(neighbour,M,goal)
                    
#                     frontier.append(neighbour)
#             else:
#                 dist[neighbour]=tempg+find_h(neighbour,M,goal)
#                 path.append(neighbour)
# #                 if neighbour not in frontier:
#                 frontier.append(neighbour)
#         print(frontier)
#     return None
# def find_h(neighbour,M,goal):
#     heuristic_dist=((M.intersections[neighbour][0]-M.intersections[goal][0])**2+(M.intersections[neighbour][1]-M.intersections[goal][1])**2)**(0.5)
#     return heuristic_dist
# def gd(neighbour,next_node,M):
#     euc_dist=((M.intersections[neighbour][0]-M.intersections[next_node][0])**2+(M.intersections[neighbour][1]-M.intersections[next_node][1])**2)**(0.5)
#     return euc_dist
                
    








# def find_next_node(frontier,M,goal,start):
# # #     min_dist=None

# #     front=M.roads[start]
    
#     distdic={}
#     for i in frontier:
#         euc_dist=((M.intersections[i][0]-M.intersections[start][0])**2+(M.intersections[i][1]-M.intersections[start][1])**2)**(0.5)
#         heuristic_dist=((M.intersections[i][0]-M.intersections[goal][0])**2+(M.intersections[i][1]-M.intersections[goal][1])**2)**(0.5)
#         dist=euc_dist+heuristic_dist
# #         if [start]+[i] not in distdic.values():
#         distdic[dist]=[start]+[i]

#     return distdic

        
# def shortest_path(M,start,goal):
#     print("shortest path called")
    
#     explored=[]
#     frontier=[]

#     explored.append(start)
#     for i in M.roads[start]:
#         if i not in explored:
            
#             frontier.append(i)
    
#     distdic=find_next_node(frontier,M,goal,start)
#     print(frontier)
#     print(explored)
#     print(distdic)
#     for j in range(10):
#         flag=0
#         removenode=distdic[min(distdic.keys())]
#         removedist=min(distdic.keys())

#         del distdic[removedist]
        
#         if removenode[-1] not in explored:
#             explored.append(removenode[-1])
#             if removenode[-1] in frontier:
#                 frontier.remove(removenode[-1])
#         for i in M.roads[removenode[-1]]:
            
#             if i not in explored:
#                 if i not in frontier:
#                     frontier.append(i)
#                     flag=1
#         if flag==0:
#             removenode[-1]=frontier[0]
                
#         distdic2=find_next_node(frontier,M,goal,removenode[-1])

#         removenode2=distdic2[min(distdic2.keys())]
#         removedist2=min(distdic2.keys())
#         newlist=[]
#         for i in removenode2+removenode:
#             if i not in newlist:
#                 newlist.append(i)
#         print(";;;;",newlist)
#         distdic[removedist+removedist2]=newlist
#         print(distdic,explored,frontier)
#         print(distdic,explored,frontier)
#         else:
            
#             explored.append(frontier[-1])
#             frontier.pop()
#             distdic2,frontier=find_next_node(frontier[-1],M,goal,frontier)

#             removenode2=distdic2[min(distdic2.keys())]
#             removedist2=min(distdic2.keys())
#             newlist=[]
#             for i in removenode2+removenode:
#                 if i not in newlist:
#                     newlist.append(i)

#             distdic[removedist+removedist2]=newlist
#     print(distdic)
    

    
    
    

# def find_next_node(start,M,goal,frontier):
# #     min_dist=None

#     front=M.roads[start]
    
#     distdic={}
#     for i in front:
#         euc_dist=((M.intersections[i][0]-M.intersections[start][0])**2+(M.intersections[i][1]-M.intersections[start][1])**2)**(0.5)
#         heuristic_dist=((M.intersections[i][0]-M.intersections[goal][0])**2+(M.intersections[i][1]-M.intersections[goal][1])**2)**(0.5)
#         dist=euc_dist+heuristic_dist
# #         if [start]+[i] not in distdic.values():
#         distdic[dist]=[start]+[i]
#         frontier.append(i)
# #             flag=0
# #         else:
# #             flag=1
#     return distdic,frontier

        
# def shortest_path(M,start,goal):
#     print("shortest path called")
    

#     explored=[]
#     frontier=[]
    
#     explored.append(start)
#     front=[]
#     for i in M.roads[start]:
#         if i not in frontier and i not in explored:
#             frontier.append(i)
#     distdic=find_next_node(frontier,start,M,goal)
#     for i in range(100):

#         removenode=distdic[min(distdic.keys())]
#         removedist=min(distdic.keys())

#         del distdic[removedist]
# #         if removenode[-1]in frontier:
# #             frontier.remove(removenode[-1])
# #         if removenode[-1] not in explored:
#         explored.append(removenode[-1])
#         for i in M.roads[removenode[-1]]:
#             if i not in frontier and i not in explored:
#                 frontier.append(i)
#         distdic2=find_next_node(frontier,removenode[-1],M,goal)

#         removenode2=distdic2[min(distdic2.keys())]
#         removedist2=min(distdic2.keys())
#         newlist=[]
#         for i in removenode2+removenode:
#             if i not in newlist:
#                 newlist.append(i)

#         distdic[removedist+removedist2]=newlist
# #             print(distdic)
#         else:
            
#             explored.append(frontier[-1])
#             frontier.pop()
#             distdic2,frontier=find_next_node(frontier[-1],M,goal,frontier)

#             removenode2=distdic2[min(distdic2.keys())]
#             removedist2=min(distdic2.keys())
#             newlist=[]
#             for i in removenode2+removenode:
#                 if i not in newlist:
#                     newlist.append(i)

#             distdic[removedist+removedist2]=newlist
#     print(distdic)
            
            
            
            
#             one iter
#             removenode=distdic[max(distdic.keys())]
#             removedist=max(distdic.keys())
#             del distdic[removedist]
#     #         if removenode[-1] not in explored:

#             distdic2=find_next_node(removenode[-1],M,goal)

#             removenode2=distdic2[min(distdic2.keys())]
#             removedist2=min(distdic2.keys())
#             newlist=[]
#             for i in removenode2+removenode:
#                 if i not in newlist:
#                     newlist.append(i)

#             distdic[removedist+removedist2]=newlist
            
#         print(distdic)
        
 
    return
