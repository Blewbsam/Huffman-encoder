import numpy as np
from Nodes import Node, Leaf


class HuffmanEncoder:

    srcNode = None

    def generate_probs(self,stats = dict):
        # turns frequency to probs
        probs = {}
        totalFrequency = sum(stats.values())
        for k,v in stats.items():
            probs[Leaf(k)] = v/totalFrequency

        print(sum(probs.values()))
        return probs




    def build_tree(self, originalKeys, originalProbs):
        # uses Huffman tree 
        currentNodes = list(originalKeys)
        currentProbs = list(originalProbs)
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


    def generate_encoding(self):
        # requires srcNode to be set
        # generates and adds encoding to each node until leaf with accumulator
        # thus implementing Huffman algorithm
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

        return leaves

class Shannon:

    def entropy(probs = list):
        # calculates list based on Shannon information
        ent = 0
        for p in probs:
            ent += p * np.log2(1/p)

        return ent
    
    def expected_length(codeProbs = dict):
        encodings = codeProbs.keys()
        l = 0
        for e in encodings:
            l += len(e.encoding) * codeProbs[e]
        
        return l