import numpy as np
from Nodes import Node, Leaf


class Encoder:

    srcNode = None

    def __init__(self,pair = dict) -> None:
        self.originalProbs = pair.values()
        self.originalKeys  = pair.keys()



    def buildTree(self):
        currentNodes = list(self.originalKeys)
        currentProbs = list(self.originalProbs)
        while True:
            upper_index_min = np.argmin(currentProbs)
            upperProb = currentProbs[upper_index_min]
            upperNode = currentNodes[upper_index_min]
            del currentProbs[upper_index_min]
            del currentNodes[upper_index_min]

            lower_index_min = np.argmin(currentProbs)
            lowerProb = currentProbs[lower_index_min]
            lowerNode = currentNodes[lower_index_min]
            del currentProbs[lower_index_min]
            del currentNodes[lower_index_min]

            newNode = Node(upperNode,lowerNode)
            newNodeProb = upperProb + lowerProb


            currentNodes.append(newNode)
            currentProbs.append(newNodeProb)

            if newNodeProb == 1:
                break
        
        assert currentProbs[0] == 1
        self.srcNode = currentNodes[0]

    # requires srcNode to be set
    # generates and adds encoding to each node until leaf with accumulator
    def generateEncoding():
        assert srcNode != None










Leafa = Leaf("a")
Leafb = Leaf("b")
Leafc = Leaf("c")

init_pair = {
    Leafa: 0.5,
    Leafb: 0.25,
    Leafc: 0.25,
}



encoder = Encoder(init_pair)
encoder.buildTree()
srcNode = encoder.srcNode
print(srcNode.upperChild)
print(srcNode.lowerChild)

