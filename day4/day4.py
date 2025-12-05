f=open("input.txt","r")

grid=[]
for line in f.readlines():
    grid.append(list(line[:-1]))

accesible =[]

num_removed=0
while(True):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                count = -1# it always counts itself so initialise as -1 to counterract
                for difx in range(-1,2):
                    print("difx=",difx)
                    for dify in range(-1,2):
                        if i+dify >= 0 and i + dify < len(grid) and j + difx >=0 and j+difx < len(grid[0]):
                            if grid[i+dify][j+difx] == "@":
          #                      print(i,j)
                                count+=1
                if count <4:
                    accesible.append((i,j))
   # print(len(accesible) )
    if len(accesible) == 0 : #if we cannot remove/access any more we're done
        break
    num_removed += len(accesible)
    for coords in accesible:
        grid[coords[0]][coords[1]] = '.' 
    accesible=[]
print(num_removed)
#######PART 1 CODE###########
#accesible =0
#for i in range(len(grid)):
#    for j in range(len(grid[0])):
#        if grid[i][j] == "@":
#            count = -1
#            for difx in range(-1,2):
#                print("difx=",difx)
#                for dify in range(-1,2):
#                    if i+dify >= 0 and i + dify < len(grid) and j + difx >=0 and j+difx < len(grid[0]):
#                        if grid[i+dify][j+difx] == "@":
#                            print(i,j)
#                            count+=1
#            if count <4:
#                accesible +=1 
#print(accesible) 
