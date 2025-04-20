# 1768. Merge Strings Alternately
# Topics: Two Pointers, String
# https://leetcode.com/problems/merge-strings-alternately/


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        shortest_word = word1 if len(word1) < len(word2) else word2
        longest_word = word2 if shortest_word == word1 else word1


        new_word_list = []
        for i in range(len(shortest_word)):
            new_word_list.append(word1[i])
            new_word_list.append(word2[i])

        if len(shortest_word) < len(longest_word):
            new_word_list.append(longest_word[len(shortest_word):])

        return ''.join(new_word_list)