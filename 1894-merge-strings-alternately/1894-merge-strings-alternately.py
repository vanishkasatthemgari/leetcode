class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged=[]
        mini=min(len(word1),len(word2))
        for i in range(mini):
            merged.append(word1[i])
            merged.append(word2[i])
        merged.extend(word1[mini::])
        merged.extend(word2[mini::])
        return "".join(merged)

        