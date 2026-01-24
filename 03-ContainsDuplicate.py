nums = list(map(int,input("Enter array : ").replace('[', '')
                .replace(']', '').split(',')))
# O(n^2)
# def duplicate(nums):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]==nums[j]:
#                 return True
#     return False

#O(nlogn)
# def duplicate(nums):
#     nums.sort()
#     for i in range(len(nums)-1):
#         if nums[i]==nums[i+1]:
#                 return True
#     return False

# O(n)
# def duplicate(nums):
#     s=set()
#     for e in nums:
#         if e in s:
#                 return True
#         s.add(e)
#     return False

def duplicate(nums):
    if len(set(nums)) < len(nums):
        return True
    return False

print(duplicate(nums))