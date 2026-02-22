# 42
nums = list(map(int,input().strip('[').strip(']').split(',')))
print(nums)
l,r = 0,len(nums)-1
lmax,rmax = nums[l],nums[r]
total = 0
while l<r:
    if nums[l] < nums[r]:
        lmax = max(lmax,nums[l])
        if lmax-nums[l] > 0:
            total += lmax-nums[l]
        l += 1
    else:
        rmax = max(rmax,nums[r])
        if rmax-nums[r] > 0:
            total += rmax-nums[r]
        r -= 1
print(total)