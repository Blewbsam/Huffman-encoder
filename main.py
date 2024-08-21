
from Encoder import Encoder 
import matplotlib.pyplot as plt 
import pandas as pd




embeddings_sizes = [300, 350, 400, 450 ,500, 550 ,600, 650, 700, 750, 800, 850, 900,1000]

if __name__ == "__main__":

    respectiveEntropies = []
    respectiveLengths = []
    for embeddings_size in embeddings_sizes:
        encoder = Encoder(embeddings_size)
        encoder.generate_encoding(src="some.txt")
        encoder.set_lookup_table()
        entropy = encoder.getBytePairEntropy()
        expectedLength = encoder.getExpectedLength()
        respectiveEntropies.append(entropy)
        respectiveLengths.append(expectedLength)

    

    df = pd.DataFrame({"Embedding size":embeddings_sizes , "Entropy" : respectiveEntropies, "Expected length" : expectedLength})
    df.to_csv("sample.csv", sep=",")

    plt.plot(embeddings_sizes,respectiveEntropies, "-")
    plt.plot(embeddings_sizes,respectiveLengths, "--")
    plt.xlabel("Size of Byte Pair Embedding table")
    plt.ylabel("Shannon entropy")

    plt.savefig('foo.png')

    plt.show()


    
















