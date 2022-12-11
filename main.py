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
        NOC = line_split[7]
        medal = line_split[14]
        name = line_split[1]
        sport = line_split[12]
        year = line_split[9]
        line = file.readline()
        if country == current_country or country == NOC:
            if year in line_split:
                if medal != "NA\n":
                    if quality < 10:
                        print(f"{quality + 1}.{name} - {sport} - {medal}")
                        quality += 1

                    else:
                        break

gold = 0
silver = 0
bronze = 0
with open(data_file, "r") as file:
    file.readline()
    line = file.readline()
    while line != "":
        line_split = line.split("\t")
        current_country = line_split[6]
        NOC = line_split[7]
        medal = line_split[14]
        year = line_split[9]
        line = file.readline()
        if country == current_country or country == NOC:
            if year in line_split:
                if medal == "Gold\n":
                    gold += 1
                    continue
                elif medal == "Silver\n":
                    silver += 1
                    continue
                elif medal == "Bronze\n":
                    bronze += 1
                    continue
    else:
        print(f"Gold medals - {gold}, Silver medals - {silver}, Bronze medals - {bronze}")



