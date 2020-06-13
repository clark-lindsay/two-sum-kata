def two_sum(nums, target):
    for firstIndex, num1 in enumerate(nums):
        for secondIndex, num2 in enumerate(nums):
            if (num1 + num2 == target):
                if (firstIndex != secondIndex):
                    return [firstIndex, secondIndex]
    return []
