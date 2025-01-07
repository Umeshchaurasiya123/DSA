def rightProduct(index,arr,rightMemory):

    if index>=len(arr):
        return 1
    
    if(rightMemory[index]!=0):
        return rightMemory[index]

    productSoFar=rightProduct(index+1,arr,rightMemory)*arr[index]


    rightMemory[index]=productSoFar

    return productSoFar


def leftProduct(index,arr,leftMemory):

    if index<0:
        return 1
    
    if(leftMemory[index]!=0):
        return leftMemory[index]
    
    productSoFar=leftProduct(index-1,arr,leftMemory)*arr[index]

    leftMemory[index]=productSoFar

    return productSoFar



def findProdcut(arr):
 
    
    leftMemory=[0]*len(arr)
    rightMemory=[0]*len(arr)

    rightResult=[]
    leftResult=[0]*len(arr)


    for index in range(len(arr)-1,-1 ,-1):
        print(index)
        leftResult[index]=leftProduct(index-1,arr,leftMemory)
    

    for index in range(len(arr)):

        rightResult.append(rightProduct(index+1,arr,rightMemory))
        
    
    print("left result is ",leftResult)
    print("right result is ",rightResult)

    ans= [leftResult[i]*rightResult[i] for i in range(len(arr))]

    return ans

arr=[1,2,3,4]
arr1=[-1,1,0,-3,3]

print("Product of all the element excepct the self is ",findProdcut(arr1))
















