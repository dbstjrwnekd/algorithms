class Solution:
    def to_swap(self, n1:int, n2:int) -> bool:
        return str(n1)+str(n2) < str(n2)+str(n1)
    
    def largestNumber(self, nums: List[int]) -> str:
        i = 0
        while i < len(nums):
            j = 0
            while j < len(nums) - i - 1:
                if self.to_swap(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                j += 1
            i += 1
        
        return str(int(''.join(map(str,nums))))
        