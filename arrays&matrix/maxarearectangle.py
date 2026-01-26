import math
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_dia = 0
        ans = 0
        for l,b in dimensions:
            dia_len = math.sqrt(l*l + b*b)
            if dia_len > max_dia or (max_dia == dia_len and l*b > ans):
                max_dia = dia_len
                ans = l*b
        return ans
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.areaOfMaxDiagonal([[2,3],[1,4],[3,4]]))  # Output: 12
    print(sol.areaOfMaxDiagonal([[1,2],[3,4],[5,6]]))  # Output: 30
    print(sol.areaOfMaxDiagonal([[1,1],[2,2],[3,3]]))  # Output: 9
    print(sol.areaOfMaxDiagonal([[1,2]]))  # Output: 2
    print(sol.areaOfMaxDiagonal([[5,6]]))  # Output: 30
'''
remeber the to track the max diagonal length and area
if the diagonal length is same then we check for area
and update the area if it is greater'''