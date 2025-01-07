

def helper(index,arr,ProductofRight):

    if index>=len(arr):
        return 1;

    ProductofRight[index]=helper(index+1,arr,ProductofRight)
    ans=helper(index+1,arr,ProductofRight)*arr[index]
    
    return ans

    


def findrightProduct(arr):



    ProductofRight=[0]*len(arr)
    index=0

    ans=helper(index+1,arr,ProductofRight)

    # ProductofRight.append(result)
    ProductofRight[0]=ans

    return  ProductofRight



arr=[1,2,3,4]

ans=findrightProduct(arr)

print(ans)





