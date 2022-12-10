import sys
# ./ поточна папка

def the_best_ten_champions():
    pass

def total_amount_of_medals():
    pass

def extreme_cases():
    pass


def output():
    pass


data_file = sys.argv[1]
country = sys.argv[3]
year = sys.argv[4]
quality = 0

with open(data_file, 'r') as file:
    file.readline()
    line = file.readline()
    while line != "":
        line_split = line.split("\t")
        current_country = line_split[6]
        NAC = line_split[7]
        medal = line_split[14]
        name = line_split[1]
        sport = line_split[12]
        line = file.readline()
        if country == current_country or country == NAC:
            line = file.readline()
            if year in line_split and country in line_split:
                line = file.readline()
                print(f"{name} - {sport}")

