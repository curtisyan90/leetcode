class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums.count(target/2)==2 :
            n1=nums.index(target/2)
            for i in range (n1+1,len(nums)):
                if nums[i]==target/2:
                    n2=i
                    return n1,n2
        else:
            for i in range(len(nums)):
                if nums[i] in nums and (target-nums[i]) in nums and nums[i]!=(target-nums[i]):
                    n1=nums.index(nums[i])
                    n2=nums.index(target-nums[i])
                    return n1,n2