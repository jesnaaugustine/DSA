

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
