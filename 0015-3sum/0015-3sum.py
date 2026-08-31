class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        n = len(nums)
        st = set()

        for i in range(0, n):
            j=i+1
            k=n-1
            while(j<k):
                sum = nums[i]+ nums[j]+ nums[k]

                if sum >0:
                    k-=1

                elif sum < 0:
                    j+=1

                else:
                    tp = tuple((nums[i], nums[j],  nums[k]))
                    st.add(tp)
                    j+=1
                    k-=1

                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and nums[k] == nums[k+1]):
                        k-=1

        ans = [list(t) for t in st]            
        return ans













        # st = set()

        # for i in range(0,len(nums)):
        #     hashset = set()

        #     for j in range((i+1), len(nums)):
        #         third = -(nums[i]+ nums[j])
        #         if third in hashset:
        #             triplet = tuple(sorted((nums[i], nums[j], third)))
        #             st.add(triplet)
        #         hashset.add(nums[j])
        
        # ans = [list(t) for t in st]
        # return ans
            
        