
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = []
        for i in S:
            if i.isalpha():
                result.append([])
s