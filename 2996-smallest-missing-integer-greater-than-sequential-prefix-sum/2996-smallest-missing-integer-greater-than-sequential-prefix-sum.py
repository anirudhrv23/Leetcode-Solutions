class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums) == 1:

            return nums[0]+1
        


        # if nums[0] != nums[1]-1:
        #     return nums[0]
        
        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                sum+=nums[i]
            else:
                break
        
        while sum in nums:
            sum+=1
            

        #     for i in range(0, len(nums)):
        #         if nums[i]>sum and nums[i] = sum+c:
        #             c+=1
        #             continue
        #         sum = nums[i]
        
        return sum


        