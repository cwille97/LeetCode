class Solution:
    def groupAnagrams(self, strs):
        
        d = {}
        
        for i in range(len(strs)):
            x = ''.join(sorted(strs[i]))
            if x not in d:
                d[x] = [strs[i]]
            else:
                d[x].append(strs[i])
        
        return d.values()

