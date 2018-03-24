cities = {
    'HongKong': {
        'country': 'China',
        'population': 120000,
        'fact': 'The Oriental Pearl'
    },
    'NewYork': {
        'country': 'America',
        'population': 250000,
        'fact': 'The largest city in the United States'
    },
    'London': {
        'country': 'America',
        'population': 180000,
        'fact': 'One of the largest financial centers in the world'
    }
}

for city in cities:
    print(city + ':')
    for item, info in cities[city].items():
        print(item + ': ' + str(info))
    print()