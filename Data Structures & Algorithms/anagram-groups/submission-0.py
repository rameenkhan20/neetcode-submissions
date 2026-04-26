class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}

        if len(strs) == 0:
            return [[""]]
        else:
            for i in range(len(strs)):
                current_word = "".join(sorted(strs[i]))
                if current_word not in anagram_groups:
                    anagram_groups[current_word] = [strs[i]]
                else:
                    anagram_groups[current_word].append(strs[i])

        return list(anagram_groups.values())
