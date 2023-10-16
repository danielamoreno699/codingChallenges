from itertools import combinations

def findMax(arr):
    subsetA = []
    subsetB = []
    sorted_arr_desc = sorted(arr, reverse=True)

    # for i in range(len(sorted_arr_desc) - 1):
    #     subsetA.append([sorted_arr_desc[i], sorted_arr_desc[i + 1]])
    for i in range(len(sorted_arr_desc)):
        for j in range(i + 1, len(sorted_arr_desc)):
            pair = [sorted_arr_desc[i], sorted_arr_desc[j]]
            subsetA.append(pair)

    for subA in subsetA:
        exclusion = [element for element in arr if element not in subA]
        subsetB.append(exclusion)

    for i in range(len(subsetA)):
        subA = subsetA[i]
        subB = subsetB[i]
        print("SubsetA:", subA)
        print("SubsetB:", subB)

        if sum(subA) > sum(subB):
            print('subA', subA)
            print('SubsetA is greater')
            return subA

        else:
            print('SubsetA is not greater')

findMax([3, 7, 5, 6, 2])
