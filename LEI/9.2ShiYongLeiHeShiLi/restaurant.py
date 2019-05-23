class Restraurant():
    """docstring for  Restraurant"""

    def __init__(self, restaurant_name, cuisine_type,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_servde = 0
    def describe_restaurant(self):
        print(self.restaurant_name, ":", self.cuisine_type)

    def open_restaurant(self):
        print("Is opening")
    def serve_nmuber(self):
        print("This resrrurant can serve "+str(self.number_servde)+ " people" )
    def set_number_served(self,n):
        self.number_servde = n

    def incerment_number_served(self,n):
        self.number_servde+=n
        return self.number_servde

restraurant = Restraurant('A', 'B')
print(restraurant.restaurant_name, " ", restraurant.cuisine_type)
restraurant.describe_restaurant()
restraurant.open_restaurant()
restraurant.set_number_served(10)
restraurant.serve_nmuber()
restraurant.incerment_number_served(50)
restraurant.serve_nmuber()
restraurant.incerment_number_served(150)
restraurant.serve_nmuber()