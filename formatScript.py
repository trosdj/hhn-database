file_input = open('input.txt', 'r')
file_output = open('output.txt', 'a')

for line in file_input:
    line = line.rstrip()
    file_output.write("('" + line + "')\n")