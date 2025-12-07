import re
f=open("input.txt","r")

operands = []
operators = []
count = 0

for line in f.readlines():
    if '+' in re.split(r"\s+",line[:-1]):
        operators = line[:-1].split()
        #operators = re.split(r"\s+",line[:-1])
    else:
        operands.append(line)
        #operands.append(re.split(r"\s+",line[:-1]))
#for i in range(len(operands)):
#    if "" in operands[i]:
#        operands[i].remove("")
print(operands)
print(operators)
#print(first_nums,operators)
#print(second_nums,third_nums)

output = 0
#ITERATE THROUGH STRING VALUES - if they're all space you're on the next number

next_operator=0
to_calculate=[]
for i in range(len(operands[0])):
    number = ''
    for j in range (len(operands)):
        if operands[j][i] != " " and operands[j][i] != "\n":
            number +=operands[j][i]
    print(number)
    print(to_calculate)
    calculation=0
    if number =='' :#or  re.match(r'\s*',number): 
        if operators[next_operator] == "+":
            print(to_calculate)
            print("PLUS")
            calculation=0
            for j in range(len(to_calculate)):
                    calculation += int(to_calculate[j])
        if operators[next_operator] == "*":
            print(to_calculate)
            print("TIMES")
            calculation=1
            for j in range(len(to_calculate)):
                calculation *= int(to_calculate[j])

        output+= calculation
        to_calculate=[]
        next_operator+=1
    else:
        to_calculate.append(number)
        print(to_calculate)

if to_calculate != []:
    if operators[next_operator] == "+":
        print(to_calculate)
        print("PLUS")
        calculation=0
        for j in range(len(to_calculate)):
                calculation += int(to_calculate[j])
    if operators[next_operator] == "*":
        print(to_calculate)
        print("TIMES")
        calculation=1
        for j in range(len(to_calculate)):
            calculation *= int(to_calculate[j])
    
    output+= calculation
#    if operators[i] == "+":
#        calculation=0
#        for j in range(len(operands)):
#                calculation += int(operands[j][i])
#    if operators[i] == "*":
#        calculation=1
#        for j in range(len(operands)):
#            calculation *= int(operands[j][i])
#    output+= calculation
print(output)
