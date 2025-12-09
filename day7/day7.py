f=open("test.txt")
space=[]
beam_indices=[]
for line in f.readlines():
    space.append(line[:-1])
    if "S" in line:
        beam_indices.append(line.index("S"))


timelines=1
print(space)
print(beam_indices)
beam_coords=[]
split_count=0
for i in range(len(space)):
    split=[]
    for beam in beam_indices:
        beam_coords.append((beam,i))
        if space[i][beam] == '^':
            split.append(beam)
            print(space[i])
            print("beam",beam)
            print(split)
            

    for beam in split:
         beam_indices.remove(beam)
         beam_indices.append(beam+1)
         beam_indices.append(beam-1)
#         withdups= len(beam_indices)
         beam_indices=list(set(beam_indices))
 #        withoutdups= len(beam_indices)
  #       if withdups> withoutdups:#there has been a merge
         beam_coords.append((beam+1,i))
         beam_coords.append((beam-1,i))
         beam_coords.remove((beam,i))



for i in range(len(space)):
    print("HERE")
    for j in range(len(space[i])):
        if (j,i) in beam_coords:
            space[i]= space[i][:j] + "|" +space[i][j+1:]
    print(space[i])

#'timelines = []
#'for i in range(len(space)):


#DAY 1 CODE
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

                        
