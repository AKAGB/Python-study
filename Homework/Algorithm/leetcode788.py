class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        alp = {
            '0': '0',
            '1': '1',
            '2': '5',
            '3': 'x',
            '4': 'x',
            '5': '2',
            '6': '9', 
            '7': 'x', 
            '8': '8',
            '9': '6',
        }
        result = 0
        for i in range(1, N):
            s = str(i)
            t = ''.join(list(map(lambda x: alp[x], s)))
            print(t)
            if 'x' not in t and s != t:
                result += 1
        return result

sol = Solution()
sol.rotatedDigits(2)