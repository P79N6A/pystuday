'''
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mjusheroms','gerren peppers','extra cheese')

def make_pizza(*toppings):
    print("\nMaking a Pizz with the following tipping :")
    for topping in toppings:
        print("-" + topping)
make_pizza('pepperoni')
make_pizza('mjusheroms','gerren peppers','extra cheese')

def build_profile(filrst,last **user_info):
    profile = {}
    profile['first_name' = first]
    profile['last_name'] = last
    for key , value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_prfile('albert','einstein',
                            location='princetion',
                            field ='physics')
print(user_profile)

#---ZuoYe---8.12#
def san_pizza(*topoons):
    print(topoons)
san_pizza('666')
san_pizza('ss','as')
san_pizza('dd','gg','hh')

def build_profile(first,last ,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key , value in user_info.items():
        profile[key] = value
    return profile
user_message = build_profile('Wang','Gang',
                            location='princetion',
                            field ='physics')
print(user_message)
'''
def build_profile(first,last ,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key , value in user_info.items():
        profile[key] = value
    return profile
user_message = build_profile('Wang','Gang',
                            location='princetion',
                            field ='physics')
print(user_message)