places = ['Beijing', 'Shanghai', 'Guangzhou', 'Tokyo', 'America']

print('Origin:', places)
print('Sorted:', sorted(places))
print('Origin:', places)
print('Sorted reverse:', sorted(places, reverse=True))
print('Origin:', places)

places.reverse()
print('Reverse:', places)
places.reverse()
print('Origin:', places)

places.sort()
print('Sort:', places)
places.sort(reverse=True)
print('Sort reverse:', places)