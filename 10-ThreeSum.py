# 15
nums = list(map(int,input().strip('[').strip(']').split(',')))
nums.sort()
print(nums)
result = []
for i in range(len(nums)-1):
    if nums[i]>0:
        break
    if i>0 and nums[i]==nums[i-1]:
        continue
    l = i+1
    r = len(nums)-1
    while l<r:
        total = nums[i] + nums[l] + nums[r]
        if total > 0:
            r -= 1
        elif total < 0:
            l += 1
        else:
            result.append([nums[i],nums[l],nums[r]])
            l += 1
            r -= 1
            while l<r and nums[l-1]==nums[l]:
                l +=1
            while l<r and nums[r]==nums[r+1]:
                r -= 1
print(result)