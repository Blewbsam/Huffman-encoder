

class BytePair:
    # Performs BytePairing given a file and records merges in specific lookup table
    # implementation of BytePair was taken from https://github.com/karpathy/minbpe/blob/master/minbpe/base.py

    def __init__(self):
        self.PairToToken = {} #pair token to new token mapping
        self.TokenToPair = {}



    def init_tokenize(self,text):
        # returns unicode of the text
        return list(map(ord,text))
    
    def get_single_stats(self,tokens):
        # returns dicitonary of frequency of each token in tokens
        stats = dict()
        for s in tokens:
            stats[s] = stats.get(s,0) + 1

        return stats

    def get_pair_stats(self,tokens):
        # returns dicitonary of frequency of each pair of tokens in tokens
        stats = dict()
        for pair in zip(tokens, tokens[1:]):
            stats[pair] = stats.get(pair,0) + 1
        return stats

    
    def merge(self,tokens, pair, newToken):
        # replaces given pair everywhere in tokens with newToken
        newTokens = []
        i = 0
        while i < len(tokens):
            if tokens[i] == pair[0] and i < len(tokens) - 1 and tokens[i+1] == pair[1]:
                newTokens.append(newToken)
                i += 2
            else:
                newTokens.append(tokens[i])
                i += 1
        return newTokens

 

    def tokenize(self,file,vocabSize):
        # makes vocabSize - 256 merges according to frequency of tokens in file
        assert vocabSize > 256
        numMerges = vocabSize - 256
        tokens = self.init_tokenize(file)
        merges = {}

        for i in range(numMerges):
            stats = self.get_pair_stats(tokens)
            curPair = max(stats, key=stats.get)
            newToken = 256 + i 
            print(f"Merging {curPair} into new token {newToken}.")
            tokens = self.merge(tokens,curPair,newToken)
            merges[curPair] = newToken

        self.PairToToken = merges
        self.TokenToPair = {v:k for k,v in merges.items()}
        return tokens
    
    