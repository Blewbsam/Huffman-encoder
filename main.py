
from Encoder import Encoder 



if __name__ == "__main__":
    encoder = Encoder()
    encoder.generate_encoding(src="some.txt")
    encoder.set_lookup_table()
    print(encoder.seqToBit.keys())
    print(len(encoder.seqToBit.keys()))
    binary = encoder.encode("some.txt")
    print(binary)
    print(encoder.decode(binary))



    print(encoder.getBytePairEntropy())











