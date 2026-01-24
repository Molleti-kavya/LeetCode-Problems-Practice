nums = list(map(int,input("Enter array : ").replace('[','').replace(']','').split(',')))

def exceptSelfProduct(nums):
    prelist = []

    prefix = 1
    for i in nums:
        prelist.append(prefix)
        prefix *= i

    suffix = 1
    postlist = []
    for i in range(len(nums) - 1, -1, -1):
        postlist.append(suffix)
        suffix *= nums[i]
    postlist = postlist[::-1]

    for i in range(len(prelist)):
        prelist[i] *= postlist[i]
    return prelist
print(exceptSelfProduct(nums))