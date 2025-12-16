space=[]
beam_indices=[]
f=open("input.txt","r")
day7file=f.readlines()
DP={}

for i in range(len(day7file[0])):
    for j in range(len(day7file)):
        DP[(i,j)]=0
max_row = j

for line in day7file:
    space.append(line[:-1])
    if "S" in line:
        print("1")
        x_coord = line.index("S")
        beam_indices.append(x_coord)
        DP[(x_coord,0)] = 1
print(DP)
        


#DP[beam] = num of timelines ending at certain beam (x,y)  
#DP[(S,0)] = 1
#DP [split] = DP [the one above it] + DP{the other one above it] 

timelines=1

print(space)
print(beam_indices)
beam_coords=[]
split_count=0
for i in range(1,len(space)):
    split=[]
    for beam in beam_indices:
        beam_coords.append((beam,i))
        if space[i][beam] == '^':
            split.append(beam)
            print(space[i])
            print("beam",beam)
            print(split)
            
        else:
            DP[(beam,i)] = DP[(beam,i-1)]

    for beam in split:
         beam_indices.remove(beam)
         beam_indices.append(beam+1)
         beam_indices.append(beam-1)
         withdups= len(beam_indices)
         beam_indices=list(set(beam_indices))
         withoutdups= len(beam_indices)
         beam_coords.append((beam+1,i))
         beam_coords.append((beam-1,i))
         beam_coords.remove((beam,i))
         DP[(beam-1,i)] += DP[(beam,i-1)] 
         DP[(beam+1,i)] += DP[(beam,i-1)] 




for i in range(len(space)):
    print("HERE")
    num_beams=0
    for j in range(len(space[i])):
        if (j,i) in beam_coords:
            space[i]= space[i][:j] + "|" +space[i][j+1:]
    print(space[i])

#'timelines = []
#'for i in range(len(space)):


#part 1 CODE
#print(space)
#print(beam_indices)
#split_count=0
#for i in range(len(space)):
#    split=[]
#    for beam in beam_indices:
#        if space[i][beam] == '^':
#            split.append(beam)
#            print(space[i])
#            print("beam",beam)
#            print(split)
#
#    for beam in split:
#        beam_indices.remove(beam)
#        split_count+=1
#        beam_indices.append(beam+1)
#        beam_indices.append(beam-1)
#        beam_indices=list(set(beam_indices))
#print(split_count)

output = 0
for i in range(len(day7file[max_row])):
    output += DP[(i,max_row)]
print(output)
    


                        

