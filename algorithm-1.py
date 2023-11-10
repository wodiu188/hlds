def two_sum(nums, target):
    head = 0
    tail = len(nums) - 1
    while tail > head:
        value = target - nums[head]
        while value < nums[tail]:
            tail -= 1
        if nums[head] + nums[tail] == target:
            return [head, tail]
        head += 1


nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # 输出 [0, 1]
