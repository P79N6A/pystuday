'''
1．什么是[]？
    答：空的列表值，他是一个列表  不包换任何选项

2．如何将'hello'赋给列表的第三个值，而列表保存在名为 spam 的变量中？（假定变量包含[2, 4, 6, 8, 10]）。
对接下来的 3 个问题，假定 spam 包含列表['a', 'b', 'c', 'd']。
    答：
    spam = ['a','b','c','d']
    spam[2] = 'hello'
    print(spam)

3．spam[int('3' * 2) / 11]求值为多少？
    答：'3'*2 为字符串33
    int 33/11  = 3
    d 的下标是 3  答案为d

4．spam[-1]求值为多少？
    答：d

5．spam[:2]求值为多少？
    答：['a','b']
对接下来的 3 个问题。假定 bacon 包含列表[3.14, 'cat', 11, 'cat', True]。
6．bacon.index('cat')求值为多少？
     答：1

7．bacon.append(99)让 bacon 中的列表值变成什么样？
    答：[3.14, 'cat', 11, 'cat', True，99]

8．bacon.remove('cat')让 bacon 中的列表时变成什么样？
    答：[3.14, 11, 'cat', True，99]

9．列表连接和复制的操作符是什么？
    答：列表链接的操作不是 +    复制的操作符是+

10．append()和 insert()列表方法之间的区别是什么？
    答：append（）是插入到列表末尾
        insert（）是插入任意位置

11．从列表中删除值有哪两种方法？
    答：remove（）   #  list.remove[数值]
        del（）       #    del(list(下标))
12．请说出列表值和字符串的几点相似之处。
    答：列表和字符串都可以传入len（），都有下标和切片   用于for循环  连接或者复制，并与int和not in 操作符一起使用

13．列表和元组之间的区别是什么？
    答：列表可以修改 添加 删除 ，  列表使用的是[]
        元组是不可修改的            元组使用的是（）

14．如果元组中只有一个整数值 42，如何输入该元组？
    答：{42,}
15．如何从列表值得到元组形式？如何从元组值得到列表形式？
    答：list（）    tuple（）函数
16．“包含”列表的变量，实际上并未真地直接包含列表。它们包含的是什么？
    答：包含的是对列表值的引用
17．copy.copy()和 copy.deepcopy()之间的区别是什么？
    答：copy.copy（）函数将浅拷贝列表，而copy.deepcomy()函数将深拷贝列表值，会复制列表内的所有列表
'''
a= ['3.14', 'cat', '11', 'cat', '99']
del(a[0])
print(a)