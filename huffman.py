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
            upperProb = currentProbs.pop(upper_index_min)
            upperNode = currentNodes.pop(upper_index_min)

            lower_index_min = np.argmin(currentProbs)
            lowerProb = currentProbs.pop(lower_index_min)
            lowerNode = currentNodes.pop(lower_index_min)

            newNode = Node(upperNode,lowerNode)
            newNodeProb = upperProb + lowerProb


            currentNodes.append(newNode)
            currentProbs.append(newNodeProb)

            if newNodeProb == 1:
                break
        
        assert currentProbs[0] == 1 # total prob must add upto one
        self.srcNode = currentNodes[0]

    # requires srcNode to be set
    # generates and adds encoding to each node until leaf with accumulator
    def generateEncoding(self):
        assert self.srcNode != None
        leaves = list()
        remainingNodes = list()

        self.srcNode.upperChild.encoding = "1"
        self.srcNode.lowerChild.encoding = "0"
        remainingNodes.append(self.srcNode.upperChild)
        remainingNodes.append(self.srcNode.lowerChild)

        while (len(remainingNodes) > 0):
            curNode = remainingNodes.pop(0)
            if (type(curNode) is Leaf):
                leaves.append(curNode)
                continue
            curNode.upperChild.encoding = curNode.encoding + "1"
            curNode.lowerChild.encoding = curNode.encoding + "0"
            remainingNodes.append(curNode.upperChild)
            remainingNodes.append(curNode.lowerChild)



class Shannon:

    def entropy(probs = list):
        ent = 0
        for p in probs:
            ent += p * np.log2(1/p)

        return ent
    
    def expectedLength(codeProbs = dict):
        encodings = codeProbs.keys()
        l = 0
        for e in encodings:
            l += len(e.encoding) * codeProbs[e]
        
        return l





Leafa = Leaf("a")
Leafb = Leaf("b")
Leafc = Leaf("c")
leafd = Leaf("d")
leafe = Leaf("c")
leaff = Leaf("f")
leafj = Leaf("j")

init_pair = {
    Leafa: 0.5,
    Leafb: 0.10,
    Leafc: 0.10,
    leafd: 0.05, 
    leafe: 0.15,
    leaff: 0.08,
    leafj: 0.02,
}



encoder = Encoder(init_pair)
encoder.buildTree()
encoder.generateEncoding()



print(Shannon.entropy(init_pair.values()))
print(Shannon.expectedLength(init_pair))

