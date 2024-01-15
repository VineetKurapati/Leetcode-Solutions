class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, curr):
            if len(curr) == len(nums):
                result.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(nums, curr)
                    curr.pop()
            

        result = []
        backtrack(nums, [])
        return result