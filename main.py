import sys
file_with_data = sys.argv[1]
# ./ поточна папка
country = sys.argv[3]
year = sys

print("country = ", country)

with open(file_with_data, 'r') as file:
    line = file.readline()
    #current_country = line[6]
    while line != "":
        line = file.readline()
        line_splitted = line.split("\t")
        print(line_splitted)
