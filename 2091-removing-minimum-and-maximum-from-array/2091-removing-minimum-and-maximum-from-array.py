class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n = len(nums)
        max_val = min_val = nums[0]

        max_idx, min_idx = 0,0

        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i

            if nums[i] < min_val:
                min_val = nums[i]
                min_idx = i

        i, j = min(max_idx, min_idx) , max(min_idx, max_idx)

        front = j+1

        back = n-i

        both = (i+1) + (n-j)

        return min(front, back, both) 
        