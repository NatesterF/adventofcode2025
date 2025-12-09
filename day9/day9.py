f=open("input.txt","r")
corner_list = []
for line in f.readlines():
    corner_list.append([int(x) for x in line[:-1].split(",")])

print(corner_list)

green_tiles=[]
for i in range(-1,len(corner_list)-1):
    if corner_list[i][0] == corner_list[i+1][0]: #Same x coord
        for j in range(min(corner_list[i][1],corner_list[i+1][1])+1,max(corner_list[i][1],corner_list[i+1][1])):
            green_tiles.append((corner_list[i][0],j))
#    else: # same y coord
#        for j in range(min(corner_list[i][0],corner_list[i+1][0])+1,max(corner_list[i][0],corner_list[i+1][0])):
#            green_tiles.append((j,corner_list[i][1]))
#


x_coords = [red[0] for red in corner_list]
y_coords = [red[1] for red in corner_list]
for j in range(max(y_coords)+1):
    green_found = False
    for i in range(max(x_coords)+1):
        if not green_found and ( (i,j) in green_tiles or [i,j] in corner_list) :
            green_found = True
        elif green_found and ((i,j) not in green_tiles ) and [i,j] not in corner_list:
            green_tiles.append((i,j))
        elif green_found and ((i,j) in corner_list or (i,j) in green_tiles):
            green_found = False # reached an extremity 
        
def find_rec_area(coords1,coords2):
    return (abs(coords1[0] - coords2[0]) +1) * (abs(coords1[1] - coords2[1]) +1)
def all_green(coords1,coords2):
    for i in range(min(coords1[0],coords2[0]),max(coords1[0],coords2[0])):
        for j in range(min(coords1[1],coords2[1]),max(coords1[1],coords2[1])):
            if not( (i,j) in green_tiles or [i,j] in corner_list):
                return False
    return True

#for j in range(max(y_coords)+2):
#    line=""
#    for i in range(max(x_coords)+2):
#        if [i,j] in corner_list:
#            line += "#"
#        elif (i,j) in green_tiles:
#            line+="X"
#        else:
#            line+="."
#    print(line)

largest_area = 0
for coords1 in corner_list:
    for coords2 in corner_list:
        print(coords1,coords2)
        if coords1 != coords2 and all_green(coords1,coords2):
            area=find_rec_area(coords1,coords2)
            if area > largest_area:
                largest_area = area
           


###Part 1 #####
#def find_rec_area(coords1,coords2):
#    return (abs(coords1[0] - coords2[0]) +1) * (abs(coords1[1] - coords2[1]) +1)
#
#print(corner_list)
#largest_area = 0
#for coords1 in corner_list:
#    for coords2 in corner_list:
#        if coords1!= coords2:
#            area=find_rec_area(coords1,coords2)
#            if area > largest_area:
#                largest_area = area
print(largest_area)
