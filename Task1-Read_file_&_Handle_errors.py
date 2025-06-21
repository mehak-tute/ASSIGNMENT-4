try:
    file = open('sample.txt', 'r')
    print("Reading file content:")
    READ = file.readline()
    print("Line 1: ", READ)
    READ = file.readline()
    print("Line 2: ", READ)
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
