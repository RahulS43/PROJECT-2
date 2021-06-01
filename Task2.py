def print_positives(list):
    for val in list:
        if val>0:
            print(val)
            
inp_ints=list(map(int,input("Enter the numbers : ").split()))

print("The positive numbers from the given sequence are : ")

print_positives(inp_ints)

