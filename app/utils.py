def get_population():
    keys = ['per', 'aus']
    values = [500, 800]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item: item['country'] == country, data))
    return result

def population_by_country_reto(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

def get_population_for_country(country_dict):
    population_dic = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }

    labels = population_dic.keys()
    values = population_dic.values()

    return labels, values