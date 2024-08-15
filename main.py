from BytePair import BytePair
from huffman import Encoder, Shannon


class main:
    def __init__(self) -> None:
        self.bp =  BytePair() 
        self.encoder = Encoder()

 

    def generate_encoding(self,src):
        with open(src,'r') as some:
            file = some.read()

        tokens = self.bp.tokenize(file,300)
        stats = self.bp.get_single_stats(tokens)

        probs = Encoder().generate_probs(stats)

        self.encoder.build_tree(probs.keys(),probs.values())
        leaves = self.encoder.generate_encoding()
        
        for l in leaves:
            print(f"For {l.x} we have encoding {l.encoding}")
        










if __name__ == "__main__":
    main()








