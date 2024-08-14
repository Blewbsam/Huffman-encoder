class AbstractNode:
    encoding = None

    def addEncoding(self, encoding = str):
        self.encoding = encoding


class Node(AbstractNode):
    parent = None
    upperChild = None
    lowerChild = None

    def __init__(self, upperChild, lowerChild) -> None:
        self.upperChild = upperChild
        self.lowerChild = lowerChild




class Leaf(AbstractNode):
    x = None

    def __init__(self,x):
        self.x = x

