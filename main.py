import sys
file_with_data = sys.argv[1]
# ./ поточна папка
country = sys.argv[3]
year = sys
year_set = set()
with open(file_with_data, 'r') as file:

    #current_country = line[6]
    line = file.readline()
    line = file.readline()
    while line != "":
        line_splitted = line.split("\t")
        year = int(line_splitted[9])
        year_set.add(year)
        line = file.readline()

year_list = sorted(year_set)

for i, y in enumerate(year_list[:10], 1):
    print(i, "\t", y)

