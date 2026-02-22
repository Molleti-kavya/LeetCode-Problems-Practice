# 11
nums = list(map(int,input().strip('[').strip(']').split(',')))
print(nums)
max_water = 0
l,r = 0,len(nums)-1
while l<r:
    width = r-l
    area = min(nums[l],nums[r]) * width
    max_water = max(area,max_water)
    if nums[l] <= nums[r]:
        l += 1
    elif nums[l] > nums[r]:
        r -= 1
print(max_water)