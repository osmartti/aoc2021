f = open('./input.txt', 'r')
data = []
for x in f:
    data.append(x.strip())

# Exercise 1
horizontal = depth = 0
for i in range(len(data)):
    command = data[i].split(' ')[0]
    value = int(data[i].split(' ')[1])
    if (command == 'forward'):
        horizontal += value
    if (command == 'down'):
        depth += value
    if (command == 'up'):
        depth -= value
print(horizontal * depth)

# Exercise 2
horizontal = aim = depth = 0
for i in range(len(data)):
    command = data[i].split(' ')[0]
    value = int(data[i].split(' ')[1])
    if (command == 'forward'):
        horizontal += value
        depth += aim * value
    if (command == 'down'):
        aim += value
    if (command == 'up'):
        aim -= value
print(horizontal * depth)