# file: Regular_Expression_Matching.py
# author: Cedric Wille cwille97@bu.edu
# description: LeetCode Regular Expression Matching Problem solution attempt
# date: 2/23/20

class Solution:
    def isMatch(self, s: str, p: str) -> bool: # we must check in reverse because '*' checks for preceding elements, this will be a recursive implementation
        if p[-1] == '.': # case for '.' matches any single character
            print("s[0:-2]:", s[0:-2])
            print("p[0:-2]:", p[0:-2])
            try:
                return Solution.isMatch(self, ''.join(s[0:-1]), ''.join(p[0:-1])) # continue checking all prior characters
            except:
                return False
        
        elif p[-1] == '*': # case for '*' Matches zero or more of the preceding element.
            print("p:", p)
            preceding_element = p[-2] 
            if s[-1] != preceding_element: # preceding element matches zero
                try:
                    return Solution.isMatch(self, ''.join(s[0:-1]), ''.join(p[0:-2])) # recurse without * or preceding element in p
                except:
                    return False
            else: # preceding element matches at least one
                counter = 0 # keep track of how far back we check in the for loop
                for i in s[-1::-1]: # loop backwards
                    counter -= 1 
                    if i != preceding_element: # if the loop reaches a character that no longer matches the pattern
                        try:
                            return Solution.isMatch(self, ''.join(s[0:counter]), ''.join(p[0:-2])) # stop considering the '*' and continue recursing
                        except:
                            return False
                        
        else: # any other character must match 1:1
            try:
                if p[-1] != s[-1]:
                    return False # the characters don't match so there is no overall match
                else:
                    return Solution.isMatch(self, ''.join(s[0:-1]), ''.join(p[0:-1])) # the characters match 1:1 so we continue checking the rest of the expression
            except:
                return False
            
            
            
s = 'aab'
p = 'c*a*b'
print("Solution.isMatch(s, p)",  Solution.isMatch(Solution, s, p))
