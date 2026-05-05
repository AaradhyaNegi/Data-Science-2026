nums = [0,1,0,3,12]

left, right = 0 , 1

while left <= len(nums) - 1 and right <= len(nums) - 1:
    if nums[left] == 0:
        while nums[right] != 0 and right <= len(nums) - 1:
            right += 1
    temp = nums[right]
    nums[right] = nums[left]
    nums[left] = temp
    left += 1