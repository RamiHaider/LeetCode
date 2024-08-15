class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        n = len(nums)

        #length constraints
        if n < 2 or n > 10**4:  
            print("Length of the list is out of bounds")
            return [] 
        
        #target constraints
        if target < -10**9 or target > 10**9:
            print("Target is out of bounds")
            return []
        

        for i in range(n-1):
            for j in range(i+1, n):

                #max value in list contraints
                if nums[i] < -10**9 or nums[i] > 10**9:
                    print(f"The value of {nums[i]} is out of bounds")
                    return []
                if nums[j] < -10**9 or nums[j] > 10**9:
                    print(f"The value of {nums[j]} is out of bounds")
                    return []                  

                if nums[i]+nums[j] == target:
                    return [i,j]
            
        print(f'No target value found within the list')
        return []

test = Solution()
print(test.twoSum([2,7,11,15],9))
print(test.twoSum([2],5))
print(test.twoSum([2,5],6))
print(test.twoSum([100000000000000,4,5,5],3))
