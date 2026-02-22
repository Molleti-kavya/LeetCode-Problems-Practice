# 167
nums = list(map(int,input().strip('[').strip(']').split(',')))
print(nums)
target = int(input())
l,r=0,len(nums)-1
while l<r:
    sum = nums[l]+nums[r]
    if sum > target:
        r -= 1
    elif sum < target:
        l += 1
    else:
        print([l+1,r+1])
        break
