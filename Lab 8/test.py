
nums = [3, 2, 4]
target = 6


def twoSum(nums, target):
    arr = [(n,i) for i, n in enumerate(nums)]
    arr.sort()
    left, right = 0, len(nums) - 1
    return arr
    while left < right:
        sum = arr[left[0]] + arr[right[0]]
        if sum == target:
            return [arr[left[1]], arr[right[1]]]
        elif sum < target:
            left += 1
        else:
            right -= 1



print(twoSum(nums, target))
