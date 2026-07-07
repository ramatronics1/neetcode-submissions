class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leng = len(numbers )

        for i in range(leng):
            for j in range(i+1 , leng):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return []            
        