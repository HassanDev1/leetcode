class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_freq = Counter(nums1)
        num2_freq = Counter(nums2)
        res = []
        
        if len(num1_freq) < len(num2_freq):
            for k,v in num1_freq.items():
                if k in num2_freq:
                    res.append(k)
        else:
            for k,v in num2_freq.items():
                if k in num1_freq:
                    res.append(k)
                    
        return res