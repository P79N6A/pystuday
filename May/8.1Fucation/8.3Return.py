'''
    # 定义形参 性 和 名
def get_formatted_name(first_name,last_naem):
   #和而为一 并将结果储存在变量为full_name
    full_name=first_name+' '+last_naem
   #将fuill_name的值装换为以首字母大写格式
    return full_name.title()

musician =get_formatted_name('jimi','hendrix')
print(musician)


def get_formatted_name(first_name,middle_name,last_name):
    full_name = first_name +' '+middle_name+' '+last_name
    return full_name.title()
musician=get_formatted_name('john','lee','hooker')
print(musician)

    #让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name= first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('joho','hooker','lee')
print(musician)


    #返回函数
def build_person(first_anme,last_name):
    person ={'first':first_anme,'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)


def build_person(first_name,last_name,age=''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age']=age
        return person
musician = build_person('jimi','hendrix',age = 27)
print(musician)

    #-------8.3.4结合函数和while循环------------#
def get_formatted_name(first_name,last_name):
    full_name=first_name + " " + last_name
    return full_name.title()
    #这是一个无限循环！
while True:
    print("\nPlease tell me you name:")
    f_name = input("First name:")
    l_name = input("last name:")

    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello." + formatted_name + "!")

    # 提示q退出
def get_formatted_name(first_name,last_name):
    full_name=first_name + " " + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter'q'ara may time to quit)")

    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello," + formatted_name +"!")

#---------ZuoYe  8-6---#
def city_country(city_name,country_name):
    full_name = city_name+','+country_name
    return full_name.title()

bull =city_country('santiago','chile')
red  = city_country('xian','china')
green = city_country('dongjing','janpan')
print(bull)
print(red)
print(green)


def makde_album(song_name,writer_naem,):
    album = {'song':song_name,'writer':writer_naem}
    return album
one = makde_album('献给爱丽丝','beiduofen')
print(one)
two = makde_album('夜曲','肖邦')
print(two)
three = makde_album('克罗地亚狂想曲','马克西姆')
print(three)


    #-----number---#
def makde_album(song_name,writer_naem,number=''):
    album = {'song': song_name, 'writer': writer_naem}
    if number:
        album = {song_name , writer_naem ,  number }
    else:
        album = {song_name,writer_naem}
    return album

one = makde_album('献给爱丽丝','beiduofen',number=20)
print(one)

'''
def make_album(song_name,writer_naem):
    album = {'song': song_name, 'writer': writer_naem}
while True:
    print('\nPlass tell me song:')
    print("(enter 'q' at nay time to quit)")

    s_name = input("song:")
    if s_name == 'q':
        break
    w_name = input("writer:")
    if w_name == 'q':
        break
    oen_name = make_album(s_name,w_naem)
    print("\n Hello,"+ oen_name +"!")
