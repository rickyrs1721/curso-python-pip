import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        header = next(reader)
        data = []

        for row in reader:
            # print('***' * 5)
            # print(row)
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

# def read_csv_2(path):
#    with open(path, 'r') as csvfile:
#       data = csv.reader(csvfile)
#       total = sum(int(row[1]) for row in data)
#    return total

# response = read_csv_2('./data.csv')
# print(response)

#print(read_csv('./app/world_population.csv'))

if __name__ == '__main__':
    data = read_csv('./app/world_population.csv')
    # new_list = list(filter(lambda item: item['Country/Territory'] == 'Albania', data))
    # #print(data[0])
    # print(new_list[0])
    print(data[0])