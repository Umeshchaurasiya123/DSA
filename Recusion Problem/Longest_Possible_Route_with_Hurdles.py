#  Why the Difference Between visited and maxLength?
# visited:

# Tracks the state of the grid.
# It needs to be reset explicitly during backtracking because it is shared across recursive calls
# (i.e., it’s passed by reference).
# Failing to reset visited[sr][sc] would incorrectly mark a cell as visited for all paths,
# preventing valid paths from being explored.

# maxLength:

# Tracks the length of the current path.
# Since it’s passed as a function parameter
# (by value for immutable types like integers), 
# each recursive call gets an independent copy of the value.
# It doesn’t need manual adjustment when backtracking.


#  here maxlength is integer so at the time of backtrackign it value  remain same  evem on next call . 
#  his value is increase or decrease. because it is pass by value. not pass by refrece. 

#  but visited  list is pass by refrece. so what ever changes happend in next call. while backtracking the changes will reflact. 
#  but not in the case of maxLength. 
# becasue it is pass by value not refrece. 

# Mutable objects (e.g., lists, dictionaries, sets) behave like pass by reference because changes to the object inside the function reflect on the original object.
# Immutable objects (e.g., integers, floats, strings, tuples) behave like pass by value because reassigning them inside the function creates a new object without affecting the original one.
 

def AllTimeLongestPath(mat,sr,sc,dr,dc,visited,maxLength,ans):


    if(sr==dr and sc==dc):
        # visited[sr][sc]=False   not needed becasue we are never marking the dr,dc as visisted. so no need to mark this visited =false 
        return maxLength


    if(sr>=0 and sc>=0 and sr<len(mat) and sc<len(mat[0]) and mat[sr][sc]==1 and visited[sr][sc]==False):
        
        visited[sr][sc]=True

        res=AllTimeLongestPath(mat,sr,sc+1,dr,dc,visited,maxLength+1,ans)
        
        # maxLength=-1
        ans=max(ans,res)



        res=AllTimeLongestPath(mat,sr-1,sc,dr,dc,visited,maxLength+1,ans)
        # maxLength=-1
        ans=max(ans,res)


        res=AllTimeLongestPath(mat,sr,sc-1,dr,dc,visited,maxLength+1,ans)
        # maxLength=-1
        ans=max(ans,res)

        res=AllTimeLongestPath(mat,sr+1,sc,dr,dc,visited,maxLength+1,ans)

        # maxLength=-1
        ans=max(ans,res)

        visited[sr][sc]=False

        
    return ans




def findLongestPath(mat,sr,sc,dr,dc):

    maxLength=float('-inf')

    visited=[ [ False for _ in row] for row in mat]

    maxLength=0

    maxLengthSoFar=0

    ans=0

    longestPath=AllTimeLongestPath(mat,sr,sc,dr,dc,visited,maxLength,ans)


    return longestPath




mat = [ [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 0, 1, 1, 0, 1, 1, 0, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]
 
# find longest path with source (0, 0) and
# destination (1, 7)


total=findLongestPath(mat, 0, 0, 1, 7)

print(total)


