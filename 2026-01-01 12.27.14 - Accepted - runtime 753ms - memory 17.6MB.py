class Solution:
    def maxLength(self, nums: List[int]) -> int:
        from math import gcd, lcm
        from functools import reduce
        
        def product(arr):
            return reduce(lambda x, y: x * y, arr)
        
        def get_gcd(arr):
            return reduce(gcd, arr)
        
        def get_lcm(arr):
            return reduce(lcm, arr)
        
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            for j in range(i, n):
                subarr = nums[i:j+1]
                p = product(subarr)
                g = get_gcd(subarr)
                l = get_lcm(subarr)
                if p == l * g:
                    max_len = max(max_len, j - i + 1)
        
        return max_len