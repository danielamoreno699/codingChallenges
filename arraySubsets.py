def findMax(arr):
    subsetA = []
    max_value = float('-inf')
    
    for i in arr:
        if i > max_value:
            max_value = i
            subsetA.append(max_value)

    for i in arr:
        if i == max_value:
            print(f"{i} is the maximum value in the array.")
        else:
            print(f"{i} is not the maximum value in the array.")
    
    return subsetA

subsetA = findMax([3, 7, 5, 6, 2])
print("SubsetA:", subsetA)
