class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
            self.restaurant_name=restaurant_name
            self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print('This restaurant is open.')
class IceCramstand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['cool','hot','nice']

    def show_flvors(self):
        for n in self.flavors:
            print('my favorate tatea in ' +n)

liangliang = IceCramstand('yili',' mengniu')
liangliang.show_flvors()