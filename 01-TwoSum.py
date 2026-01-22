nums = [1,3,4]
target = 7
# Approach 1 - Brute Force
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         if nums[i]+nums[j]== target:
#             print(i,j)

# for i in range(len(nums)):
#     need = target - nums[i]
#     if need in nums and nums.index(need) != i:
#         print(i,nums.index(need))

# Approach 2 - Two pass Hash Table
d=dict()
for i in range(len(nums)):
    d[nums[i]]=i
for i in range(len(nums)):
    need = target - nums[i]
    if need in d.keys() and d[need] != i:
            print(i,d[need])