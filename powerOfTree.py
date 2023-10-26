def isPowerOfThree(n):
    if n == 1:
        return True
    if n <=0 or n % 3 != 0:
        return False
    return isPowerOfThree(n // 3) 
    
print(isPowerOfThree(27))