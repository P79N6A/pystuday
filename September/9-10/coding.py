from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors=[]):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def show(self):
        print("We have ",end='')
        for flavor in self.flavors:
            print(flavor,end=',')
        print(str(len(self.flavors)) + ' ice-cream ')

r = IceCreamStand('ken','eva',['sweet'])
r.show()
print(r.number_served)