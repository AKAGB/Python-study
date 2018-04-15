class Restaurant:
    def __init__(self, rst_name, cui_type):
        self.restaurant_name = rst_name
        self.cuisine_type = cui_type

    def describe_restaurant(self):
        print('Restaurant name is ' + self.restaurant_name + '.')
        print('Cuisine type is ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print('Restaurant is openning...')
    
if __name__ == '__main__':
    rest = Restaurant('KFC', 'Fast Food')
    print(rest.restaurant_name)
    print(rest.cuisine_type)
    rest.describe_restaurant()
    rest.open_restaurant()
