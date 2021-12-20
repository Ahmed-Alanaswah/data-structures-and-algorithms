
# Add Node
# Add Edge
# Get neighbors
# Get nodes
# Size
# BFS

from collections import deque

class Queue:
  def __init__(self):
    self.dq = deque()

  def enqueue(self, value):
    self.dq.append(value)
  
  def dequeue(self):
    return self.dq.pop()
  
  def __len__(self):
    return len(self.dq)



class Vertex:
  """
  Input:Value
  What is doing: Store the value
  Return: None
  """
  def __init__(self, value):
    self.value = value

class Edge:
  """
  Input: Vertex, weight
  What is doing: Store the vertex and the weight
  Return: None
  """
  def __init__(self,vertex, weight):
    self.vertex = vertex
    self.weight = weight

class Graph:
  """
  Input: None
  What is doing: It is creating an empty graph 
  Return: None
  """
  def __init__(self):
    self.__adj_list = {}
    

  """
  Input : Value
  What is doing : add node to the Graph
  Return : node
  """
  def add_node(self, value):
    node = Vertex(value)
    self.__adj_list[node] = []
    return node

  """
  Input: start_vertex, end_vertex , 
  weight:optional
  What is doing: Creat an edge and append the edge to the value of
  start_vertex inside the adj_list
  Return: None
  """
  def add_edge(self, start_vertex, end_vertex, weight=0):
    if start_vertex not in self.__adj_list:
      raise KeyError("Start Vertex is not found")
    if end_vertex not in self.__adj_list:
      raise KeyError("Start Vertex is not found")
    edge = Edge(end_vertex, weight)
    self.__adj_list[start_vertex].append(edge)
    
  """
  Input : Vertex
  What is doing: Get all neighbors for a vertex
  Return: a list of edges
  """
  def get_neighbors(self, vertex):
    return self.__adj_list.get(vertex, [])
  
  

  """
  Input : None
  What is doing : get all the nodes in the graph as a set or list
  Return : a list or set of the nodes
  """
  def get_nodes(self):
    return self._adj_list.keys()

  """
  Input: None
  What is doing: find the length of the adj_list
  Return: int The size(the length of adj_list)
  """
  def size(self):
    return len(self.__adj_list)

  """
  Input: Start_vertex
  What is doing: it will traverse throught all nodes
  Return: A list of nodes
  """
  def breadth_first(self,start_vertex):

        queue=Queue()
        visited=set()
        result=[]
        queue.enqueue(start_vertex)
        visited.add(start_vertex)
        result.append(start_vertex.value)
        if start_vertex==None:
            return "It is an empty graph"
        while len(queue):
            current_vertex = queue.dequeue()

        neighbors = self.get_neighbors(current_vertex)

        for edge in neighbors:
            neighbor = edge.vertex

            if neighbor not in visited:
                queue.enqueue(neighbor)
                visited.add(neighbor)
                result.append(neighbor.value)

        return result


def business_trip(graph, array):
    
    try:
        cost = 0
        for city in range(len(array)):
            edges = graph.get_neighbors(array[city])

            if city + 1 <= len(array) -1:

                cost_check = cost

                for neighbor in edges:
                    if array[city + 1] == neighbor.vertex:
                        cost += neighbor.weight

                if cost == cost_check:
                    return None

        return f'${cost}'

    except:
        raise Exception("Please check your inputs and try again.")

if __name__=="__main__":
    graph=Graph()
    val1=graph.add_node("A")
    val2=graph.add_node("B")
    val3=graph.add_node("C")
    graph.add_edge(val1,val2,50)
    graph.add_edge(val1,val3,1)
    graph.add_edge(val2,val3,1)
    print(graph.breadth_first(val1))

    print('===========')
    print(business_trip(graph, ["Arendelle", "Monstropolis", "Naboo"]))