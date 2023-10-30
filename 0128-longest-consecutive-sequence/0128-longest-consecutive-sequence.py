class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create a dictionary to keep the freq of element
        # iterate through the list and find the starting point
        #keep track of count and then get max_len
        #return max_len
        if len(nums) == 0:
            return 0
        
        start = set(nums)
        max_len = 0
        
        for num in nums:
            if num - 1 not in start:
                count = 0
                while num + count  in start: #count =4 num=4 0
                    count += 1
                max_len = max(max_len,count)
                
        return max_len
        
        
        