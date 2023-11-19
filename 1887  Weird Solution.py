class Solution(object):
    def reductionOperations(self, nums):
        n = len(nums)
        freq = [0] * 50001
        for num in nums:
            freq[num] += 1
        res, operations = 0, 0
        for i in range(50000, 0, -1):
            if freq[i] > 0:
                operations += freq[i]
                res += operations - freq[i]  
                #很有意思的想法，这里代表的是这个意思：
                #把最大数变成i需要x步，并且把x加到最后的res中
                #其实可以写成：
                #res += operations
                #operations += freq[i]
                #这两个变量有一个时间差，怪怪的，估计现在能明白估计马上就忘
        return res
