def getSequenceSum(i, j, k):
    # increment until it equals to j
    # decrement from j until it equals to k

    result = 0

    for num in range(i, j + 1):
        result += num

    for num in range(j - 1, k - 1, -1):  
        result += num

    return result



print(getSequenceSum(5, 9, 6))

    