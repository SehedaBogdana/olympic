import sys
# ./ поточна папка

data_file = sys.argv[1]
command = sys.argv[2]

if command == "-medals":
    country = sys.argv[3]
    year = sys.argv[4]
    output_t = sys.argv[6]
    all_countries = []
    quantity = 0
    all_years = []
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
            current_year = line_split[9]
            all_years.append(current_year)
            all_countries.append(current_country)
            line = file.readline()
            if country == current_country or country == NOC:
                if year in line_split and current_year == year:
                    if medal != "NA\n":
                        if quantity < 10:
                            print(f"{quantity + 1}.{name} - {sport} - {medal}")
                            quantity += 1

                        else:
                            break
        else:
            if year not in all_years:
                print("This year didn't have game")
                exit()
            elif country not in all_countries:
                print("This country doesn't exist")
                exit()

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
            current_year = line_split[9]
            sum_of_medals = (int(gold) + int(bronze) + int(silver))
            line = file.readline()
            if country == current_country or country == NOC:
                if year in line_split and current_year == year:
                    if medal == "Gold\n":
                        gold += 1
                    elif medal == "Silver\n":
                        silver += 1
                    elif medal == "Bronze\n":
                        bronze += 1

        else:
            if sum_of_medals < 10:
                print("This country doesn't have more than 10 medals")
            else:
                print(f"Gold medals - {gold}, Silver medals - {silver}, Bronze medals - {bronze}")

elif command == "-interactive":
    medals = {}
    place = {}
    our_list = []
    all_countries = []
    each_olymp = {
        "Gold": 0,
        "Bronze": 0,
        "Silver": 0
    }
    country = input("Enter the country: ")
    with open(data_file, 'r') as file:
        file.readline()
        line = file.readline()
        while line != "":
            line_split = line.split("\t")
            current_country = line_split[6]
            NOC = line_split[7]
            current_medal = line_split[14]
            current_place = line_split[11]
            current_years = line_split[9]
            all_countries.append(current_country)
            line = file.readline()
            if NOC == country or current_country == country:
                if current_medal != "NA\n":
                    if current_years in medals:
                        medals[current_years] = medals[current_years] + 1
                    else:
                        medals[current_years] = 1
                        our_list.append(current_years)
                        place[current_place] = current_years
        else:
            print(f"{min(place, key=place.get)} where was their first game")
            print(f"{min(our_list)} - is the first year when the country participated")
            print(f"{max(medals, key=medals.get)} - the best year")
            print(f"{min(medals, key=medals.get)} - the worst year")



