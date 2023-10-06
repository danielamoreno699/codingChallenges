def setZeroes(list):
   

    #find zero
    #set the col and rows to 0
    #modify the matrix
    n = 3
    m = 3
    
    for i in range(0, n):
 
        for j in range(0, m):
 
            # Printing jth element of ith row
            print(list[i][j], end=" ")
    
        print()
 
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
       