def find(mat, x):
    if 0 <= x and x <= 9:#filter number
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j] == x:
                    return (i, j)
    return (-1,-1)
 
mat = [  [0,2,3]
        ,[8,3,5]
        ,[9,7,6]]

x = 11
i, j = find(mat, x)
 
print(f"\nHUMAM \n linha: {i+1} , coluna: {j+1}")
print(f"\nDEVELOPER \n{find(mat, x)}")

    
