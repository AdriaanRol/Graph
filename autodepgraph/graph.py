"""
This contains the definition
"""
class graph():
    """
    A class containing nodes
    """
    def load_graph(self, graph_file):
        """
        Takes in a graph
        """


class node():
    def __init__(self, name):
        self.name = name
        self.state = 'unknown'

    def check_node(self):
        return self.state

    def __call__(self):
        print('hello')

    def __repr__(self):
        return self.name
