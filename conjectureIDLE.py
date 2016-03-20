#!/usr/bin/env python3

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


minimum = 0;
maximum = 0;

while minimum <= 0:
    # Prompt user for input
    rangeInput = input("Enter a positive range to test the conjecture. (Ex. '1 5'): ")

    # Get range to test
    minimum = int(rangeInput[0 : rangeInput.find(" ")])
    maximum = int(rangeInput[rangeInput.find(" "):])

    # Reverse minimum and maximum if necessary
    if(minimum > maximum):
        temp = minimum
        minimum = maximum
        maximum = temp

triesDict = {}

# Run recursive conjecture
for index in range(minimum, maximum + 1):
    tries = operation(index, 0)
    print("The number, {}, worked after {} tries".format
          (int(index), tries))
    if tries in triesDict:
        triesDict[tries] += 1
    else:
        triesDict[tries] = 1

print()
lastnum = 0

# Print the sorted dictionary
for num in sorted(triesDict):
    if(lastnum != num - 1):
        print("-------------------------------------------------")
    print("The amount of times it took {} tries is {}".format
          (num, triesDict[num]))
    lastnum = num

# End program after user is done with output
print()
end = input("Press Enter to quit.")
print()