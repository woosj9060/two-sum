def twoSum(nums, target):
    i = 0
    j = 0
    for firstnum in nums:
        for secondnum in nums:
            if(firstnum + secondnum == target):
                index = [i, j]
            j = j+1
        i = i+1
        j = 0
    return index
            

print("please type number list")
nums = list(map(int, input().split()))
print("please type target")
target = int(input())
print(twoSum(nums,target))
