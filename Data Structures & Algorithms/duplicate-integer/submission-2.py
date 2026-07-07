class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):  # Step 2: Linear scan
            if nums[i] == nums[i - 1]:  # Check for adjacent duplicates
               return True  # Duplicate found
        return False       
               
                