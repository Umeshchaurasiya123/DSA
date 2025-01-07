

def findCombinationSum(arr,ans,temp,sum,index):



    if(sum==0):
        ans.append(temp[:])
        return
    
    for i in range(index,len(arr)):

        if (sum-arr[i])>=0:

            temp.append(arr[i])

            findCombinationSum(arr,ans,temp,sum-arr[i],i)

            temp.remove(arr[i])

    return     
           




def combinationSum(arr,sum):

    ans=[]
    temp=[]

    findCombinationSum(arr,ans,temp,sum,0)

    return ans    




arr = [2, 4, 6, 8]
sum = 8
ans = combinationSum(arr, sum)

print(ans)




