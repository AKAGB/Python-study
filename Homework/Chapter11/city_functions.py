def city_country(city, country, population=0):
    if population:
        return '%s, %s - population %d' % (city, country, population)
    else:
        return '%s, %s' % (city, country)