from BytePair import BytePairEncoding
from huffman import HuffmanEncoder, Shannon

class Encoder:

    def __init__(self, numEmbeddings) -> None:
        self.numEmbeddings = numEmbeddings
        self.bp =  BytePairEncoding() 
        self.encoder = HuffmanEncoder()
        self.leaves = None
        self.probs = None
        self.bitToSeq = {}
        self.seqToBit = {}



    def generate_encoding(self,src):
        with open(src,'r') as some:
            file = some.read()

        tokens = self.bp.tokenize(file,self.numEmbeddings)
        stats = self.bp.get_single_stats(tokens)

        self.probs = HuffmanEncoder().generate_probs(stats)

        self.encoder.build_tree(self.probs.keys(),self.probs.values())
        self.leaves = self.encoder.generate_encoding()
        


    def set_lookup_table(self):
        
        for l in self.leaves:
            primaryUnicodes = []
            unicodes = []
            unicodes.append(l.x)
            while len(unicodes) > 0:
                curUnicode = unicodes.pop(0)
                if (int(curUnicode) < 256):
                    primaryUnicodes.append(curUnicode)
                else:
                    try:
                        bi1,bi2 = self.bp.TokenToPair[curUnicode]
                        unicodes.insert(0,bi2)
                        unicodes.insert(0,bi1)
                    except:
                        print(curUnicode, " not found in TokenToPair.")
                        primaryUnicodes.append(0)
            self.bitToSeq[l.encoding] = "".join(list(map(chr,primaryUnicodes)))
        self.seqToBit = {v:k for k,v in self.bitToSeq.items()}



    def encode(self,src):
        with open(src,'r') as f:
            file = list(f.read())
        

        binary = ""
        curString = ""
        max_index = len(file)
        i = 0
        runTime = 0
        while i < max_index:
            addition = file[i]
            # if ord(addition) > 1000:
            #     addition = ""
            curString += addition
            if curString in self.seqToBit.keys():
                binary += self.seqToBit[curString]
                curString = ""

            i += 1
            runTime += 1
        
        print(curString)
        return binary


    def decode(self,binary):
        sequence = ""
        curSeq = ""
        max_index = len(binary)
        i = 0
        while i < max_index:
            curSeq += binary[i]
            if curSeq in self.bitToSeq.keys():
                sequence += self.bitToSeq[curSeq]
                curSeq = ""

            i += 1
        
        return sequence


    def getBytePairEntropy(self):
        return Shannon.entropy(self.probs.values())

    def getExpectedLength(self):
        return Shannon.expected_length(self.probs)