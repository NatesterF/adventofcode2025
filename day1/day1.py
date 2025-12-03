import math
f=open("input.txt","r")
directions = {"L":-1,"R":1}
dial = 50
password =0
while command := f.readline():
    magnitude = int(command[1:-1])
    for i in range(magnitude):
        dial = (dial +  directions[command[0]]) % 100
        if dial == 0:
            password += 1


#    if command[0]=="L":
#        if (dial - magnitude)%100 != (dial - magnitude):
#            password += math.ceil(magnitude / 100 )
#
#        dial = (dial - magnitude ) %100
#
#        
#    elif command[0]=="R":
#        if (dial + magnitude)%100 != (dial + magnitude):
#            password += math.ceil(magnitude / 100 )
#        dial = (dial + magnitude)% 100
#    if dial == 0:
#        password += 1
    
    print(command)
    print(dial)
    print(password)
