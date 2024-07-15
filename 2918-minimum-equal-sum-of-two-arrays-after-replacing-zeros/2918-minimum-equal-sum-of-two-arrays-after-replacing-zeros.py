class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int: 
#         zerosOfNums1, zerosOfNums2 = nums1.count(0), nums2.count(0)
#         sum1, sum2 = sum(nums1), sum(nums2)
#         if zerosOfNums1==0 and zerosOfNums2==0 and sum1 != sum2: return -1
#         if zerosOfNums1==0 and zerosOfNums2!=0 and sum1 < sum2 + zerosOfNums2: return -1
#         if zerosOfNums1!=0 and zerosOfNums2==0 and sum1 + zerosOfNums1 > sum2: return -1
        
#         return max(sum1+zerosOfNums1,sum2+zerosOfNums2)
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        count_zero1 = nums1.count(0)
        count_zero2 = nums2.count(0)
        sum1 += count_zero1
        sum2 += count_zero2
        
        if count_zero1 == 0 and count_zero2 == 0 and  sum1 != sum2:return -1
        if count_zero1 == 0 and count_zero2 > 0 and sum2 > sum1 : return -1
        if count_zero1 > 0 and count_zero2 ==0 and sum1 > sum2 : return -1
        
        return max(sum1,sum2)
        
       
        
        
            
            
            
        
        
        
        