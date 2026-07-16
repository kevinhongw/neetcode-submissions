class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0

        for num in nums:
            if num:
                product = product * num
            else:
                zero_count += 1
        
        if zero_count > 1:
            return [0] * len(nums)

        result = [0] * len(nums)
        for i, num in enumerate(nums):
            print(i)
            print(num)
            if zero_count > 0:
                result[i] = 0 if num != 0 else product
            else:
                result[i] = product // num

        return result
        