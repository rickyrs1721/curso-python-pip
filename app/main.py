import utils

data = [
    {
        'country': 'Peru',
        'population': 2300
    },
    {
        'country': 'Argentina',
        'population': 400
    }
]

def run():
    key, value = utils.get_population()
    print(key, value)



    country = input('Ingrese el pais: ')

    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__':
    run()