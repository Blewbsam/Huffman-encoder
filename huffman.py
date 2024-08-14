

init_pair = {
    "a" : 0.5,
    "b" : 0.5,
}


class Encoder:

    def __init__(self,pair = dict) -> None:
        self.probs = pair.values()
        self.originalKeys  = pair.keys()
        self.currentKeys = self.originalKeys







class Node:
    parent = None
    upperChild = None
    lowerChild = None

    def __init__(self, upperChild, lowerChild) -> None:
        self.upperChild = upperChild
        self.lowerChild = lowerChild







