class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S.lower()
        result = [S]
        l = len(S)
        for i in range(l):
            if S[i].isalpha():
                for j in result[:]:
                    result.append(j[:i] + j[i].upper() + j[i+1:])
        return result
        
# sol = Solution()
# print(sol.letterCasePermutation('a1b2'))