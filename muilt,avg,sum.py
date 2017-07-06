# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
#
# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

for i in range(1,1000):
    if(i%2!=0):
        print i


for c in range(5,1000000):
    if(c%5 == 0):
        print c


# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
#
#
a = [1, 2, 5, 10, 255, 3]
total = 0
for sumList in range(len(a)):
        total += a[sumList]
        print (total)

#Average List
#Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

avgList = [1, 2, 5, 10, 255, 3]
subtotal = 0
for i in range(len(avgList)):
        subtotal += avgList[i]
        mean = subtotal / len(avgList)
        print (mean)
