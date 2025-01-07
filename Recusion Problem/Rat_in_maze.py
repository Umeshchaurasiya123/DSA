
def find_path(rows,cols,maze,n,result,visit,current_path):
    # print(current_path)

    if rows<0 or rows>=n or cols<0 or cols>=n or maze[rows][cols]==0 or visit[rows][cols]==True:
        return


    if rows == n - 1 and cols == n - 1:
        result.append(current_path)
        return
    
    if  0 <= rows < n and 0 <= cols < n and maze[rows][cols] == 1:
        
        visit[rows][cols]=True

        find_path(rows,cols+1,maze,n,result,visit,current_path=current_path+"R")
        find_path(rows,cols-1,maze,n,result,visit,current_path=current_path+"L")
        find_path(rows-1,cols,maze,n,result,visit,current_path=current_path+"U")
        find_path(rows+1,cols,maze,n,result,visit,current_path=current_path+"D")

        visit[rows][cols]=False

        return






maze = [
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 1]
]

n = len(maze)
# List to store all the valid paths
result = []
# Store current path
current_path = ""

# creating the visisted array to prevent the infinte loops. 
# this is interesing case
visited=[[False]*n]*n

visit=[[False for _ in range(n)] for _ in range(n)]

if maze[0][0] != 0 and maze[n - 1][n - 1] != 0:
    # Function call to get all valid paths
    find_path(0, 0, maze, n, result,visit,current_path)

print(result)
