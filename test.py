my_file = open('readings.csv', 'r')
line = my_file.readline()
while line:
    print(line)
    line = my_file.readline()