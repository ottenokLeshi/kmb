f = open(path_to_file, 'r')
w = open(path_to_file, 'w')

for line in f:
    str = line.lower().replace('snake', 'python')
    if "python" in str and "anaconda" in str:
        print(str)
        w.write(str)
