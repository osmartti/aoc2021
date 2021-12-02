f = open('./input.txt', 'r')
data = []
for x in f:
    data.append(int(x))

# Exercise 1
increases = 0
for i in range(len(data)):
    if (data[i] > data[i - 1]):
        increases += 1
print(increases)

# Exercise 2
increases = 0
prevResult = float('inf')
for i in range(len(data)-2):
    result = data[i] + data[i+1] + data[i+2]
    if (result > prevResult):
        increases += 1
    prevResult = result
print(increases)