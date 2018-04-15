from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, rst_name, cui_type, ic_list):
        super().__init__(rst_name, cui_type)
        self.flavors = ic_list

    def print_flavors(self):
        for i in self.flavors:
            print(i)

if __name__ == '__main__':
    ice = IceCreamStand('Mc', 'Ice Cream', ['IceA', 'IceB', 'IceC'])
    ice.open_restaurant()
    ice.describe_restaurant()
    ice.print_flavors()
