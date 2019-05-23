'''
responses={}
#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat is your name?")
    response = input("Which moutain would you like to climb someday?")

    #将答案储存在字典中
    responses[name] = response

    #看看是否还有人要参与调查
    repeat=input("Would you like to let another person respond?（yes/on）")
    if repeat == 'no':
        polling_active=False

    #调查结束，显示结果
    print("\n----Poll Results---")
    for name, response in responses.items():
        print(name + "Would like to climb "+ response +".")

#------ZuoYe-----#
#def display_message(username):
#    print("I like study Python  "+username.title()+"!")
#display_message('wanggang')

def favorite_book(book='mather_where'):
  #  print("One of my favorite books is  Alice in Worderland .")
    print("One of my favorite books is "+book)
favorite_book('father where').

#-----8.3--ZuoYe--##
#def make_shirt(size ,typesce):
def make_shirt(size='175',typesce='tang'):
  print("shirt size:"+size)
  print("shirt sypesce: "+typesce)
#make_shirt(size='175',typesce='song')
#make_shirt('175','song')
#make_shirt(typesce='tang',size='180')
make_shirt(size='175',typesce='tang')

#8-4___##
def make_shirt(size,sypeece='Python'):
  print("I love "+sypeece+" shirt zui da "+size)
make_shirt(size='175')
'''
#8-5__##
def describe_city(city='XiAn', country='China'):
  print(city + "is in " + country)
describe_city(city='XiAn', country='China')

def describe_city(city='New YOURK', country='US'):
  print(city + " is in " + country)
describe_city(city='New YOURK', country='US')

def describe_city(city,conuntry):
  print(city + "is in "+ conuntry)
describe_city()
