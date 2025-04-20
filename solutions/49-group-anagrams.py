# 49. Group Anagrams
# Topics: Array, Hash Table, String, Sorting
# https://leetcode.com/problems/group-anagrams/


from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_dict = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = ' '.join([str(x) for x in count])
            anagrams_dict[key].append(s)
        
        return anagrams_dict.values()