import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('world_population.csv')
    
    continent = input('Type continent: ')
    country = input('Type country: ')

    data = list(filter(lambda item: item['Continent'] == continent, data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    porcentage = list(map(lambda x: x['World Population Percentage'], data))

    charts.generate_pie_chart(countries, porcentage)

    # new_list = list(filter(lambda item: item['Country/Territory'] == country, data))

    result = utils.population_by_country_reto(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population_for_country(country)
        charts.generate_bar_chart(country["Country/Territory"], labels, values)
    else:
        raise Exception('No se encontró el pais solicitado')

if __name__ == '__main__':
    run()


