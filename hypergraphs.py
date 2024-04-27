class Hypergraph():
    def __init__(self):
        self.vertices = []
        self.hyperedges = [{}]

    def addVertex(self,vertex):
        self.vertices.append(vertex)
    
    def addVertices(self, vertices):
        for vertex in vertices:
            self.addVertex(vertex)

    def addHyperedge(self, hyperedge_key, hyperedge_vertices):
        # edge = dict(name = edge_key, vertices = edge_vertices)
        hyperedge = {}
        hyperedge[hyperedge_key] = hyperedge_vertices
        self.hyperedges.append(hyperedge)

    def printVertices(self):
        for vertex in self.vertices:
            print(vertex)

    def printHyperedges(self):
        for hyperedge in self.hyperedges:
            for hyperedge_key, hyperedge_vertices in hyperedge.items():
                print(hyperedge_key, ": ", hyperedge_vertices)
            # print(hyperedge)


hypergraph = Hypergraph()
hypergraph.addVertex(1)
hypergraph.addVertices([2,3,4])
hypergraph.addHyperedge(1, hyperedge_vertices=[2,3])
hypergraph.addHyperedge(2, hyperedge_vertices=[4,3])
hypergraph.printVertices()
hypergraph.printHyperedges()