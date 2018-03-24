rivers = {
    'nile': 'egypt',
    'yangtse': 'china',
    'mississippi': 'america',
}

for k, v in rivers.items():
    print('The %s runs through %s' % (k.title(),
            v.title()))
print('\nRivers:')
for key in rivers.keys():
    print(key.title())
print('\nCountries:')
for country in rivers.values():
    print(country.title())