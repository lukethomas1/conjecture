# Recursive function based on Collatz conjecture
def operation(index, tries):
    result = 0
    tries += 1
    
    if(index % 2 == 0):
        result = index / 2
        
        if(result == 1):
            return tries
        else:
            return operation(result, tries)
            
    if(index % 2 == 1):
        result = index  * 3 + 1
        return operation(result, tries)
# End operation


min = 0;
max = 0;

while min <= 0 and min >= max:
    # Prompt user for input
    input = input("Enter a range to test the conjecture. (Ex. '1 5'): ")

    # Get range to test
    min = int(input[0 : input.find(" ")])
    max = int(input[input.find(" "):])

triesDict = {}

# Run recursive conjecture
for index in range(min, max + 1):
    tries = operation(index, 0)
    print("The number, {}, worked after {} tries".format
          (int(index), tries))
    if tries in triesDict:
        triesDict[tries] += 1
    else:
        triesDict[tries] = 1
# End for

print()
lastnum = 0
sorted(triesDict)

for num in triesDict:
    if(lastnum != num - 1):
        print("-------------------------------------------------")
    print("The amount of times it took {} tries is {}".format
          (num, triesDict[num]))
    lastnum = num
