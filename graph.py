import collections
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.animation
import warnings


def BFS(graph, root): 
    visited, queue, result = set([root]), collections.deque([root]), collections.deque([(root,root)])
    while queue: 
        v = queue.popleft()
        for neighbour in graph[v]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour)
                result.append((v, neighbour)) 
    return result


def DFSUtil(g, node, visited, result): 
    visited[node]= True
    for child in g[node]: 
    	if visited[child] == False: 
       	    result.append((node, child)) 
            DFSUtil(g, child, visited, result) 
    
def DFS(graph, root): 
        result=collections.deque([(root, root)])
        visited = graph.fromkeys(graph, False)
        DFSUtil(graph, root, visited, result) 
        return result


def FindShortestWay(graph, start, end, path=[]):
        path=path+[start]
        if start==end: return path
        if not start in graph: return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = FindShortestWay(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

def fromAM2AL(graph):
    return [[ 1 if j in i else 0 for j in graph.keys()] for i in graph.values()]



def make_animated_graph(graph, path, title):
    def draw_me(num):
       ax.clear()
       ax.set_title(title, fontsize=12)
       ax.set_xticks([])
       ax.set_yticks([])
       nx.draw_networkx_edges(d2, ax=ax, pos=pos, with_labels = True, edge_color="gray")
       nx.draw_networkx_edges(d2, ax=ax, pos=pos, with_labels = True, edgelist=edgelist, edge_color="red", width=3)
       nx.draw_networkx_nodes(d2, ax=ax, pos=pos, node_color="gray", with_labels = True)
       nx.draw_networkx_nodes(d2, ax=ax, pos=pos, nodelist=nodelist, node_color="red", with_labels = True)
       nx.draw_networkx_labels(d2, ax=ax, pos=pos)
       if path:
          new=path.popleft()
          edgelist.append(new)
          nodelist.append(new[1])
   
    fig = plt.figure(figsize=(8, 6))
    fig.canvas.set_window_title('Графы')
    ax = fig.subplots()
    edgelist, nodelist=[], [path[0][0]]
    #install graphviz and be pleased or...
    #pos = nx.nx_pydot.pydot_layout(graph, prog='fdp')    
    pos = nx.spring_layout(graph, k=0.5, iterations=170, scale=1.4)
    warnings.filterwarnings("ignore")
    ani = matplotlib.animation.FuncAnimation(fig, draw_me, frames=len(result), interval=700, repeat=False)
    plt.show()


if __name__ == '__main__':
    d2=nx.random_tree(28, seed=177)
    graph=nx.to_dict_of_lists(d2) 

    print('\n\n\nПоздравляем если все работает! Ох и возни же было с этим!')
    print('\n\n\nВот наш граф как список смежности:')
    print(graph)

    print('\n\n\nВот наш граф как таблица смежности:')
    am=fromAM2AL(graph)
    for line in am: print(line)

    print('\n\nBFS путь обхода')
    result=BFS(graph, 0)
    print([r[1] for r in result])
    make_animated_graph(d2, result, 'Рандомный граф! Поиск в ширину')
 
    print('\n\nDFS путь обхода')
    result=DFS(graph, 0)
    print([r[1] for r in result])
    make_animated_graph(d2, result, 'Рандомный граф! Теперь поиск в глубину')
   
    print('\n\n\nВот наш новый граф как список смежности:')
    d2=nx.pappus_graph()
    graph=nx.to_dict_of_lists(d2)     
    print(graph)

    find=10
    print('\n\nКратчайший путь до узла {}'.format(find))
    result=FindShortestWay(graph, 0,find)
    print(result if result else 'Нет пути')
    result=collections.deque(zip(result[:-1], result[1:])) if result else collections.deque([(0,0)])      
    make_animated_graph(d2, result, 'Рандомный граф! Поиск кратчайшего пути от {} до {}'.format(0, find))
    

