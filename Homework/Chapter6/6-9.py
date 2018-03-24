favorite_places = {
    'Tom': ['Beijing', 'London', 'Paris'],
    'Jack': ['GuangZhou', 'Shanghai', 'Tokyo'],
    'Sarah': ['NewYork', 'Paris', 'Moscow']
}
for name in favorite_places:
    print(name + ':')
    for place in favorite_places[name]:
        print(place, end=' ')
    print('\n')