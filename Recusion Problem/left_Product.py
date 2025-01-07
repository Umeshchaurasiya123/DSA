

def findLeftProduct(arr):

    ResultantArray=[]

    def helper(index):

        print(index)
        if  index<0:
            return 1; 

        result=helper(index-1)*arr[index]

        return result
    


    for i in range(len(arr)):

        leftProduct=helper(i-1)

        ResultantArray.append(leftProduct)

    return ResultantArray

    


arr=[2,3,4,5]

ans=findLeftProduct(arr)

print(ans)



# now do the memorization. 


#  in memorization. we check whether subproblem is already exist  memory. if not than we calcualre and  stored in memory for future release. 
# 
# 
#  

def findLeftProductWithMemorization(arr):

    ResultantArray=[]
    memorizationIndexd=[0]*len(arr)
    def helper(index):

        if(memorizationIndexd[index]!=0):
            return memorizationIndexd[index]


        print(index)
        if  index<0:
            return 1; 

        result=helper(index-1)*arr[index]

        memorizationIndexd[index]=result

        return result
         


    for i in range(len(arr)):

        leftProduct=helper(i-1)

        ResultantArray.append(leftProduct)

    return ResultantArray


arrs=[2,3,4,5]

answer=findLeftProductWithMemorization(arrs)

print(ans)


    
