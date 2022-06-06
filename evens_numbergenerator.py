# Function to generate arrays of possible numbers for the evens puzzle solver.
# This code is unfinished - I decided to creat the arrays manually for now for the sake of getting a working
# solution.
# To be continued!

evens = [2, 4, 6, 8]
odds = [1, 3, 5, 7, 9]

numbers = []
results = []

#j = 1
#for j in range(3):
#    numbers =[]
#    if ((j+2) < (len(odds))):
#        for i in range(j,(j+3)):
#            numbers.append(odds[i])
#            numbers.append(x)
#        results.append(numbers)

#print(results)

def addNumbers(nums):
    total = 0
    for i in range(len(nums)):
        total =  total + nums[i]
    return total


for i in range(4):
    if (i+2)< len(odds):
        m = [odds[i], odds[i+1], odds[i+2]]
        m.append(addNumbers(m))
        results.append(m)
    if (i+3) < len(odds):
        n = [odds[i], odds[i+1], odds[i+3]]
        results.append(n)
        o = [odds[i], odds[i+2], odds[i+3]]
        results.append(o)
    if (i+4) < len(odds):
        p = [odds[i], odds[i+1], odds[i+4]]
        results.append(p)
        q = [odds[i], odds[i+2], odds[i+4]]
        results.append(q)
        r = [odds[i], odds[i+3], odds[i+4]]
        results.append(r)

print(results)



