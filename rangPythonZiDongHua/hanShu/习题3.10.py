'''
#1．为什么在程序中加入函数会有好处？
    答：函数减少了重复的代码，这让程序刚短， 更容易阅读，更容易修改

#2．函数中的代码何时执行：在函数被定义时，还是在函数被调用时？
    答：函数中的代码在函数被调用的时候执行，而不是在函数被定义时

#3．什么语句创建一个函数？
    答： def 语句定义了 一个函数

#4．一个函数和一次函数调用有什么区别？
    答：函数包含def语句和def中的代码  函数调用让程序执行，转到函数内，函数条用求值为该函数的返回值

#5．Python 程序中有多少全局作用域？有多少局部作用域？
    答：在调用一个函数时，创建了一个全局函数，和一个局部函数作用域。

#6．当函数调用返回时，局部作用域中的变量发生了什么？
    答：当函数返回时，局部作用域被销毁，其余所有变量都被遗忘了

#7．什么是返回值？返回值可以作为表达式的一部分吗？
    答：返回值是函数调用求值的结果，像所有值一样，返回值可以作为表达式的一部分

#8．如果函数没有返回语句，对它调用的返回值是什么？
    答：如果函数没有返会 reutrn 语句 他的返回只就是Nnoe

#9．如何强制函数中的一个变量指的是全局变量？
    答：global 语句强制函数中的一个变量引用该全局变量

#10．None 的数据类型是什么？
    答：None的数据类型是None  Type

#11．import areallyourpetsnamederic 语句做了什么？
    答：import 语句导入 areallyourpetsnamederic 模块

#12．如果在名为 spam 的模块中，有一个名为 bacon()的函数，在引入 spam 后，如何调用它？
    答： spam.bacon()

#13．如何防止程序在遇到错误时崩溃？
    答：将可能导致错误的代码放在一个try子句中

#14．try 子句中发生了什么？except 子句中发生了什么？
    答：可能导致错误的代码放在try字句中，发生错误时，要执行的代码放在except中




#实践项目

def collatz(number):
    #print("请输入:"+ input(number))
 #   number = input('请输入：')
    if number == 1:
        return 1
    elif number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3*number + 1
if __name__ == '__main__':
    print('请输入:')
    number = input()
    print(collatz(int(number)))
#print(collatz(18))
#print(collatz(17))



'''

def collatz(number):
    if number == 1:
        return 1
    elif number % 2 == 0:
        numbers = number // 2
        print(numbers)
        collatz(numbers)
    elif number % 2 == 1:
        numbers = 3*number + 1
        print(numbers)
        collatz(numbers)
try:
    number = int(input("请输入一个整数->:"))
    collatz(number)
except ValueError:
    print("please input a integer number")













