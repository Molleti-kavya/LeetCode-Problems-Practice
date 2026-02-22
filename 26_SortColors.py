# 75
nums = list(map(int,input().strip('[').strip(']').split(',')))
print(nums)
l,k,r = 0,0,len(nums)-1
while k <= r:
    if nums[k]==0:
        nums[k],nums[l]=nums[l],nums[k]
        l += 1
        k += 1
    elif nums[k]==1:
        k += 1
    elif nums[k]==2:
        nums[k],nums[r]=nums[r],nums[k]
        r -= 1
print(nums)