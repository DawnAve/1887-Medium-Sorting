class Solution(object):
    def reductionOperations(self, nums):
        nums.sort(reverse = True)
        operations = 0
        unique = nums[0] # the maximum number

        for i in range(1, len(nums)): # loop from largetst to smallest
            if nums[i] == unique:   #repeating numbers
                continue
            if nums[i] < unique:
                operations+=i
            unique = nums[i]
        return operations
