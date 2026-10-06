class WordDictionary:

    def __init__(self):
        self.trie = {}
    def addWord(self, word: str) -> None:
        d = self.trie
        for ch in word:
            if ch not in d:
                d[ch] = {}
            d = d[ch]
        d['#'] = '#'

    def search(self, word: str) -> bool:
        def dfs(d,i):
            if i==len(word):return '#' in d

            ch = word[i]
            if ch!='.':
                if ch not in d:
                    return False
                return dfs(d[ch],i+1)

            for child in d:
                if child=='#':
                    continue
                if dfs(d[child],i+1):
                    return True
            return False            
    
        return dfs(self.trie,0)