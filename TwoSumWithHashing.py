class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        empty_Dictionary = {}
        result = []

        #length constraints
        if len(nums) < 2 or len(nums) > 10**4:  
            print("Length of the list is out of bounds")
            return [] 
        
        #target constraints
        if target < -10**9 or target > 10**9:
            print("Target is out of bounds")
            return []
        
        
        for index,value in enumerate(nums):

            #max value in list contraints
            if nums[index] < -10**9 or nums[index] > 10**9:
                print(f"The value of {nums[index]} is out of bounds")
                return []
                
            if not (target - value) in empty_Dictionary.keys():
                empty_Dictionary[value] = index
                continue

            if (target - value) in empty_Dictionary.keys():
                result.append(empty_Dictionary[(target-value)])
                result.append(index)
                return result
                
        print(f'No target value found within the list')
        return []


