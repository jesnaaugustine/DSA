

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
