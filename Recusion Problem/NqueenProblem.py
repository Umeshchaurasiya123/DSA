import copy


def findQueen(row,n,emptyBoard,cols,positiveSet,negativeSet,result):
     

    # base case

    if row==n:

        # result.append(emptyBoard[:])  this is creating a shallow copy of list. basically copying the data in the fist list only. 
        # does not copying all the data. 

        # use copy.deepcopy
        result.append(copy.deepcopy(emptyBoard))
        return
        


     
    for col in range(n):

        if col in cols  or (row+col) in positiveSet or (row-col) in negativeSet:
            continue

        emptyBoard[row][col] ="Q"
        cols.add(col)
        positiveSet.add(row+col)
        negativeSet.add(row-col)

        findQueen(row+1,n,emptyBoard,cols,positiveSet,negativeSet,result)

        emptyBoard[row][col]="."
        cols.remove(col)
        positiveSet.remove(row+col)
        negativeSet.remove(row-col)


    return



def findNqueen(n,emptyBoard,cols,positiveSet,negativeSet,result):

    
    row=0
    
    findQueen(row,n,emptyBoard,cols,positiveSet,negativeSet,result)


    return




# program to find the nqueen. 

n=4
emptyBoard= [["."]*n  for _ in range(n)]

cols=set()
positiveSet=set()
negativeSet=set()
result=[]

findNqueen(n,emptyBoard,cols,positiveSet,negativeSet,result)

print(result)
# print(["a"]*4)

# print(emptyBoard)








# mat = [ 
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]



# both are same 


# visited = [[False for _ in row] for row in mat]

# myList=[]
# for row in mat:
#     temp=[]
#     for eachElement in row:
#         temp.append(False)
#     myList.append(temp)

# print(myList)

# print(visited)

