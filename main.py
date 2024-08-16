from BytePair import BytePair
from huffman import HuffmanEncoder, Shannon


class main:
    def __init__(self) -> None:
        self.bp =  BytePair() 
        self.encoder = HuffmanEncoder()
        self.leaves = None
        self.bitToSeq = {}
        self.seqToBit = {}

 

    def generate_encoding(self,src):
        with open(src,'r') as some:
            file = some.read()

        tokens = self.bp.tokenize(file,300)
        stats = self.bp.get_single_stats(tokens)

        probs = HuffmanEncoder().generate_probs(stats)

        self.encoder.build_tree(probs.keys(),probs.values())
        self.leaves = self.encoder.generate_encoding()
        
        for l in self.leaves: #l.x , l.encoding
            print(f"For {l.x} we have encoding {l.encoding}")


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
            self.bitToSeq[l.encoding] = "".join(list(map(chr,primaryUnicodes)))
        self.seqToBit = {v:k for k,v in self.bitToSeq.items()}


    
    def encode(self,file):
        binary = ""
        curString = ""
        max_index = len(file)
        i = 0
        while i < max_index:
            curString += file[i]
            if curString in self.seqToBit.keys():
                binary += self.seqToBit[curString]
                curString = ""

            i += 1
        
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



if __name__ == "__main__":
    m = main()
    m.generate_encoding(src="some.txt")
    m.set_lookup_table()
    with open("some.txt",'r') as some:
        file = some.read()
        binary = m.encode(file)
        print(binary)
        print(m.decode(binary))











