input = open('input.txt', 'r')
output = open('output.txt', 'a')

for line in input:
    line = line.rstrip()
    output.write("('" + line + "')\n")