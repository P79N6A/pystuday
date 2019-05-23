'''
alien_0={'color':'green','points':5}
print(alien_0)

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

alien_0 ={'x_position':}

favoite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name,language in favoite_languages.items():
    print(name.title()+"'s favorite language is "
          + language.title()+".")


for name in favoite_languages.keys():
    print(name.title())
 
friends=['phil','sarah']
for  name in favoite_languages:
    print(name.title())

    if name in friends:
        print("Hi"+name.title()+
            ",I see your favorite language is "+
            favoite_languages[name].title()+"!")

#按照顺序遍历字典中所有的健   sorted()
for name  in  sorted(favoite_languages.keys()):
    print(name.title()+",thank you for taking the poll. ")

#遍历字典中所有的值   values()
print("The following languages have been mentionde:")
for language in favoite_languages.values():
    print(language.title())

#  集合 set  每个元素都是独一无二的
print("The following languages hanv been mentionde:")
for language in  set(favoite_languages.values()):
    print(language.title())
'''
rivers={'nile':'geypt',
        'huanghe':'china',
        'chnazhongguojiang':'china'}
#输出每个河流打印
for river in  rivers:
    print('The Nike runs through Egypt.'+ river)
#输出每条河流的名字
for river in rivers:
    print(river)
#使用循环打印每个国家的名字
for river in  rivers.values():
    print(river.title())
#



