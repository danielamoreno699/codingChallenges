# def sum(arr, target):
#     left = 0
#     right = len(arr) - 1
   

#     for i in range(len(arr)):
#         while left < right:
#             current_sum = arr[i] + arr[left] + arr[right]

#             if (current_sum - target == 1):
#                 return current_sum
#             else:
#                 left += 1
#                 right -= 1
        

#     return None 

# result = sum([-1, 2, 1, -4], 1)
# print(result)
def threeSumClosest(nums, target):
    nums.sort()  # Sort the input list first
    closest = float('inf')  # Initialize closest with positive infinity
    result = 0

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            distance = current_sum - target

            if abs(distance) < abs(closest):
                closest = distance
                result = current_sum

            if current_sum < target:
                left += 1
            else:
                right -= 1

    return result

print(threeSumClosest([-1, 2, 1, -4], 1))