

def bfs(graph,start_node):
    visited =set()
    qu =[]
    qu.append(start_node)
    ans =[]
    visited.add(start_node)
    while qu:
        ans.append(qu[0])
        for j in graph[qu[0]]:
            if j not in visited:
                visited.add(j)
                qu.append(j)
        qu.pop(0)
    return ans
        
def dfs(graph,start_node):
    ans =[]
    visited=set()
    def inner(gr,start):
        if start in visited:
            return
        ans.append(start)
        visited.add(start)
        for i in graph[start]:
            if i not in visited:
                inner(gr,i)
    inner(graph,start_node)
    return ans

'''
Problem Statement: Given an undirected Graph consisting of V vertices numbered from 0 to V-1 and E edges. The ith edge is represented by [ai,bi], denoting a edge between vertex ai and bi. We say two vertices u and v belong to a same component if there is a path from u to v or v to u. Find the number of connected components in the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
'''
def components(V,E):
    graph ={k:[k] for k in range(V)}
    for e in E:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    is_visited=[0]*V
    comp=0
    def dfs(gr,st):
        if is_visited[st]==0:
            return
        
        for c in gr[st]:
            if is_visited[c] !=1:
                is_visited[c]=1
                dfs(gr,c)
    for i in range(V):
        if is_visited[i]==0:
            is_visited[i]=1
            dfs(graph,i)
            comp+=1
    return comp
##letcode-994. Rotting Oranges
def orangesRotting(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        is_visited =[[0 for _ in range(n)] for _ in range(m)]
        min_time=0
        qu=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    qu.append(((i,j),0))
                    is_visited[i][j]=2
        while qu:
            k=qu[0][0][0]
            l=qu[0][0][1]
            min_time=max(min_time,qu[0][1])
            if k-1>=0 and grid[k-1][l]==1 and is_visited[k-1][l]!=2:
                qu.append(((k-1,l),qu[0][1]+1))
                is_visited[k-1][l]=2
            if k+1<len(grid) and grid[k+1][l]==1 and is_visited[k+1][l]!=2:
                qu.append(((k+1,l),qu[0][1]+1))
                is_visited[k+1][l]=2
            if l-1>=0 and grid[k][l-1]==1 and is_visited[k][l-1]!=2:
                qu.append(((k,l-1),qu[0][1]+1))
                is_visited[k][l-1]=2
            if l+1<len(grid[0]) and grid[k][l+1]==1 and is_visited[k][l+1]!=2:
                qu.append(((k,l+1),qu[0][1]+1))
                is_visited[k][l+1]=2
            qu.pop(0)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and is_visited[i][j]==0:
                    return -1
        return min_time
#detecting cycle keep the parent along with node in the queue. If the neighbour node is visisted and its not equal to parent node then return tru
# becoz its visisted by other node due to cycle. Same approch for both BFS and DFS
def iscycle(graph):
    is_visited=set()
    
    def bfs(graph,queue):
        nonlocal is_visited
        while queue:
            cur = queue.pop(0)
            for ng in graph[cur[0]]:
                if ng not in is_visited:
                    queue.append((ng,cur[0]))
                    is_visited.add(ng)
                elif ng in is_visited and cur[1]!=ng:
                    return True
        return False
    for st in graph:
        if st not in is_visited:
            is_visited.add(st)
            flag=bfs(graph,[(st,-1)])
            if flag:
                return flag
                
    return False

def isCycle_dfs(graph):
    is_visited=set()
    def dfs(graph,start):
        if start[0] in is_visited:
            return True
        is_visited.add(start[0])
        for ng in graph[start[0]]:
            flag =False
            if ng !=start[1]:
                flag = dfs(graph,(ng,start[0]))
            if flag:
                return flag
    for k in graph:
        if k not in is_visited:
            flag =dfs(graph,(k,-1))
            if flag:
                return flag
    return False

def isCycle_directed(graph):
    is_visited=set()
    is_pathvisited=set()
    def inner(gr,start):
        if start in is_visited and start in is_pathvisited:
            return True
        is_visited.add(start)
        is_pathvisited.add(start)
        for ng in gr[start]:
            flag = False
            flag = inner(gr,ng)
            if flag:
                return flag
            is_pathvisited.remove(ng)
    for i in graph:
        if i not in is_visited:
            f = inner(graph,i)
            if f:
                return f
    return False
#207. Course Schedule
def canFinish(numCourses, prerequisites):
    graph ={k:[] for k in range(numCourses)}
    for pre in prerequisites:  
        graph[pre[1]].append(pre[0])
    
    is_visited =set()
    is_pathvisited =set()
    def dfs(gr,start):
        if start[0] in is_visited and start[0] in is_pathvisited:
            return True
        is_visited.add(start[0])
        is_pathvisited.add(start[0])
        for ng in gr[start[0]]:
            flag = dfs(gr,(ng,start[0]))
            if flag:
                return flag
            is_pathvisited.remove(ng)
    for i in range(numCourses):
        if i not in is_visited:
            flag =dfs(graph,(i,-1))
            if flag:
                return not flag
            is_pathvisited.remove(i)
    return True

#542. 01 Matrix
def updateMatrix(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    row = len(mat)
    column = len(mat[0])
    ans =[[0 for _ in range(column)] for _ in range(row)]
    visisted =set()
    qu=[]
    for i in range(row):
        for j in range(column):
            if mat[i][j]==0:
                qu.append(((i,j),0))
                visisted.add((i,j))
    while qu:
        cur = qu.pop(0)
        c_r =cur[0][0]
        c_c =cur[0][1]
        ans[c_r][c_c]=cur[1]
        if c_r-1>=0 and (c_r-1,c_c) not in visisted:
            qu.append(((c_r-1,c_c),cur[1]+1))
            visisted.add((c_r-1,c_c))
        if c_r+1<row and (c_r+1,c_c) not in visisted:
            qu.append(((c_r+1,c_c),cur[1]+1))
            visisted.add((c_r+1,c_c))
        if c_c-1>=0 and (c_r,c_c-1) not in visisted:
            qu.append(((c_r,c_c-1),cur[1]+1))
            visisted.add((c_r,c_c-1))
        if c_c+1<column and (c_r,c_c+1) not in visisted:
            qu.append(((c_r,c_c+1),cur[1]+1))
            visisted.add((c_r,c_c+1))
    return ans


    



if __name__=='__main__':
    graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
    #print(bfs(graph,'A'))
    print(dfs(graph,'A'))
    V = 4
    edges = [[0,1],[1,2]]
    print(components(V,edges))
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(orangesRotting(grid))
    gr ={1:[2],2:[1,3],3:[2],4:[5,6],5:[4,6],6:[4,5],7:[8],8:[7]}
    gr_notcylce ={1:[2,3],2:[5,6],3:[4,7],4:[3],5:[2],6:[2],7:[3,8],8:[7]}
    #print(iscycle(gr))
    print(isCycle_dfs(gr_notcylce))
    directedgraph_cycle ={1:[2],2:[3],3:[4,7],4:[5],5:[6],6:[],7:[5],8:[9],9:[10],10:[8]}
    directedgraph_notcycle={1:[2],2:[3],3:[4,7],4:[5],5:[6],6:[],7:[5],8:[9],9:[10],10:[]}
    print(isCycle_directed(directedgraph_notcycle))
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    print(updateMatrix(mat))

