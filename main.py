import sys
# ./ поточна папка

# -medals China 2004
data_file = sys.argv[1]
command = sys.argv[2]
# 1 -medals =====================================================================================================

if command == "-medals":
    country = sys.argv[3]
    year = sys.argv[4]
    output_t = sys.argv[6]
    all_countries = []
    quantity = 0
    all_years = []
    with open(data_file, 'r') as file:
        file.readline() #пропуск першу лінію
        line = file.readline() #читаємо наступну лінію
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
            all_years.append(current_year)
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

# 4 interactive ========================================================================================

if command == "-interactive":
    medals = {}
    place = {}
    our_list = []
    filtered_data = []
    data = []
    all_countries = []
    distDatas = {}
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
            data.append(line_split)
            current_country = line_split[6]
            NOC = line_split[7]
            current_medal = line_split[14]
            current_place = line_split[11]
            current_years = line_split[9]
            all_countries.append(current_country)
            set_of_gold = set()
            set_of_silver = set()
            set_of_bronze = set()
            # value_1 = sum{values[0], values[1], values[2]}
            line = file.readline()
            if NOC == country or current_country == country:
                if current_medal != "NA\n":
                    filtered_data.append(line)
                    if current_years in medals:
                        medals[current_years] = medals[current_years] + 1
                        if current_years in distDatas.keys():
                            if current_medal == "Bronze\n": #якщо медаль бронзова
                                distDatas[current_years][0] += 1 #тоді додаємо до словника
                            elif current_medal == "Silver\n":
                                distDatas[current_years][1] += 1
                            elif current_medal == "Gold\n":
                                distDatas[current_years][2] += 1

                    else:
                        medals[current_years] = 1
                        our_list.append(current_years)
                        place[current_place] = current_years
                        for line in filtered_data:
                            if current_years not in distDatas.keys(): #якщо міста немає в словнику
                                distDatas[current_years] = [0, 0, 0]

        else:
            print(f"{min(place, key=place.get)} where was their first game")
            print(f"{min(our_list)} - is the first year when the country participated")
            print(f"{max(medals, key=medals.get)} - the best year")
            print(f"{min(medals, key=medals.get)} - the worst year")
            for key, value in distDatas.items(): #проходимося по словнику
                first = value[0]
                second = value[1]
                third = value[2]
                quantity_of_years = len(distDatas)
                set_of_gold.add(third)
                set_of_bronze.add(first)
                set_of_silver.add(second)
            print(f"On average, the country got: {int(sum(set_of_bronze)/quantity_of_years)} - bronze, {int(sum(set_of_silver)/quantity_of_years)} - silver, {int(sum(set_of_gold)/quantity_of_years)} - gold")



#################################################################################################################
# -total 1972

elif command == "-total":
    year_2 = sys.argv[3] #дістаємо рік
    with open(data_file, 'r') as file:
        file.readline() #пропуск першу лінію
        line = file.readline()# читаємо наступну лінію
        data = [] #створ список

        while line != "": #поки лінія не пуста
            line_split = line.split("\t") #розділ лінію на табуляції
            data.append(line_split) #додаємо в список
            line = file.readline() #читаємо наступну лінію

        filtered_data = [] #створ пустий список

        for line in data: #проход по списку
            current_year = line[9]
            medal = line[14]
            if current_year == year_2 and medal != "NA\n": #якщо рік співпадає і медаль не NA
                filtered_data.append(line) #тоді додаємо в список

    for line in filtered_data: #проход по списку
        if '-' in line[6]: #якщо в місті є дефіс
            line[6] = line[6].split('-')[0] #то виділяємо його і два символи після нього
        for line in filtered_data: #проход по списку
            if '-' in line[6]: #якщо в місті є дефіс
                line[6] = line[6].split('-')[0] #то виділяємо його і два символи після нього


        distData = {} #створ словник
        for line in filtered_data: #проход по списку
            current_city = line[6]
            medal = line[14]

            if current_city not in distData.keys(): #якщо міста немає в словнику
                distData[current_city] = [0, 0, 0] #тоді додаємо його
            else: #якщо місто є в словнику
                if medal == "Bronze\n": #якщо медаль бронзова
                    distData[current_city][0] += 1 #тоді додаємо до словника
                elif medal == "Silver\n":
                    distData[current_city][1] += 1
                elif medal == "Gold\n":
                    distData[current_city][2] += 1

        for key, value in distData.items(): #проходимося по словнику, оверт ключ і значення
            print(f"{key} won {value[0]} Bronze, {value[1]} Silver, {value[2]} Gold")



################################################################################################################
# -overall China Ukraine Poland

elif command == "-overall":
    data_file = sys.argv[1]
    year = sys.argv[3] #дістаємо рік

    info = {}

    with open(data_file, 'r') as file:
        file.readline()
        row = file.readline()
        while row:
            row = row[:-1] #весь рядок крім останнього символа
            columns = row.split('\t') #ділимо по табуляції

            year = columns[9]
            team = columns[6]
            medal = columns[14]
            countries = sys.argv[3:]

            if medal != 'NA' and team in countries:
                if team not in info:
                    info[team] = {} #словник
                if year not in info[team]:
                    info[team][year] = {'count': 0} #словник

                info[team][year]['count'] += 1

            row = file.readline()

        for team, teamInfo in info.items(): #проходимось по словнику
            print(f'{team}:')
            maxCount = 0
            maxYear = 0

            for year, totalCount in teamInfo.items():
                count = totalCount['count']
                #print(f'\t\t{year} : {count}')

                if count > maxCount:
                    maxCount = count
                    maxYear = year

            print(f'\t\tнайуспішніший рік {maxYear} - {maxCount} медалей')
            continue

