from .Frame import Frame

class Frameable:
    def __init__(self, node):
        self.frame = Frame(self.node)
