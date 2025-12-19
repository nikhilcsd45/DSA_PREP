
from collections import deque


def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
            
        
        queue = deque([(beginWord, 1)])  # (current_word, transformation_count)
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        queue.append((newWord, level + 1))
                        wordSet.remove(newWord)  # mark as visited

        return 0
