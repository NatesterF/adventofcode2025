f=open("input.txt",'r')
fresh_ranges=[]
toggle=False
fresh_ingredients=[]

def find_overlap(pair1,pair2):
    start1 = pair1[0]
    end1 = pair1[1]
    start2 = pair2[0]
    end2=pair2[1]
    return (start1 <= start2  and end1 >= start2) or (start2 <= start1 and end2 >= start1) or (start1 <= end2 and end1 >= end2) or (start2 <= end1 and end2 >= end1)
for line in f.readlines():
    if line=="\n":
        toggle = True
    else:
        if not toggle:
            temp= line[:-1].split("-")
            start = int(temp[0])
            end=int(temp[1])
            overlap_found=False
            for pair in fresh_ranges:
                if find_overlap((start,end),pair): 
                    fresh_ranges.remove(pair)
                    fresh_ranges.append((min(start,pair[0]),max(end,pair[1])))
                    overlap_found = True
                    break
            if not overlap_found:
                fresh_ranges.append((start,end))
#            for i in range(int(temp[0]),int(temp[1])+1):
#                if not( i in fresh_ingredients):
                   # merge ranges

                   # fresh_ingredients.append(i)
#            fresh_ingredients.extend(list(range(int(temp[0]),int(temp[1])+1)))

#fresh =0
#for line in f.readlines():
#    if line=="\n":
#        toggle = True
#    else:
#        if not toggle:
#            temp= line[:-1].split("-")
#            fresh_ranges.append((int(temp[0]),int(temp[1])))
#        else:
#            ingredient = int(line[:-1])
#            for (start,end) in fresh_ranges:
#                if ingredient <= end and ingredient >= start:
#                    fresh +=1
#                    break
#
changed = True
output = fresh_ranges.copy()
while changed:
    changed= False
    for first_range in output:
        for second_range in output:
            if first_range != second_range:
                if find_overlap(first_range,second_range):
                    if first_range in output and second_range in output:
                        changed = True
                        output.remove(first_range)
                        output.remove(second_range)
                        output.append((min(first_range[0],second_range[0]),max(first_range[1],second_range[1])))
print(fresh_ranges)
print(output)
fresh_ranges=output.copy()
num_fresh=0
for pair in fresh_ranges:
    num_fresh += (pair[1] - pair[0])+1



#fresh_ingredients=set(fresh_ingredients)
print(len(fresh_ingredients))
print(num_fresh)

