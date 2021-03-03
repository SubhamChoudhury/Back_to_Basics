#Optimized DP Probelm

#Function
def maxSubArraySum(a, size):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if(max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if(max_ending_here < 0):
            max_ending_here = 0
    return max_so_far

#Main_Code
a = []
x = int(input("Enter Size of Array: "))
for i in range(0, x):
    inp = int(input("Enter Elements: "))
    a.append(inp)

print("Maximum Contiguous sum is: ", maxSubArraySum(a, x))
