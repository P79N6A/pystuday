class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name + " uses " + self.type)

    def open_restaurant(self):
        print(self.name + ' is opening!')

    def set_number_served(self,pnum):
        self.number_served = pnum

    def increment_number_served(self,pnum):
        self.number_served += pnum