import numpy as np 
f=open("input.txt",'r')
output = 0
for line in f.readlines():
    joltage=0
    num_list = [int(line[i]) for i in range(len(line)-1)]
    print(num_list)
    n=len(num_list)
    dp = np.zeros(shape=(n,13)) #let DP[k,l] be the largest number (of length l) made using indices k,k+1,...,n-1 of numlist
    dp[n-1][1] = num_list[n-1] 
    for pos in range(n-2,-1,-1): #start at the end of the list and work backwards
        for length in range(1,min(n-pos,12)+1):
            current_candidate = num_list[pos]*10**(length-1) + dp[pos+1][length-1]  #prepending current position to the best possible length-1 number
            dp[pos][length] = max(current_candidate,dp[pos+1][length])

    joltage = dp[0][12]
    print(joltage)
    output+=joltage
#########PART 1 CODE #############
#for line in f.readlines():
#    joltage=0
#    num_list = [int(line[i]) for i in range(len(line)-1)]
#    print(num_list)
#    max_digit = max( num_list[:-1])
#    max_digindex = num_list.index(max_digit)
#    other_digit = max(num_list[max_digindex+1:])
#    joltage=max_digit*10 + other_digit
#    print(joltage)
#    output+=joltage
#
print(output)

