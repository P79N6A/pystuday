'''
1．什么是转义字符？
    答：转义字符表示字符串中的一些字符，这些字符用别的方式很难在代码中打印出来
2．转义字符\n 和\t 代表什么？
    答： \n 换行符  \t是制表符
3．如何在字符串中放入一个倒斜杠字符\？
    答：\\
4．字符串"Howl's Moving Castle"是有效字符串。为什么单词中的单引号没有转义，却没有问题？
    答：因为使用了  双引号来标识字符串的开始和结尾
5．如果你不希望在字符串中加入\n，怎样写一个带有换行的字符串？i
    答：如果你不希望在字符串中加入\n，怎样写一个带有换行的字符串？
6．下面的表达式求值为什么？
• 'Hello world!'[1]      =  e
• 'Hello world!'[0:5]    =  Hello
• 'Hello world!'[:5]     =  Hello
• 'Hello world!'[3:]     =  lo world!

7．下面的表达式求值为什么？
• 'Hello'.upper()           = HELLO
• 'Hello'.upper().isupper() = Ture
• 'Hello'.upper().lower()   = hello
8．下面的表达式求值为什么？
• 'Remember, remember, the fifth of November.'.split()
     #   =['Remember,', 'remember,', 'the', 'fifth', 'of', 'Novermber']
• '-'.join('There can be only one.'.split())
    #   =['T_h_e_r_e_', '_c_a_n_', '_b_e_', '_o_n_l_y_', '_o_n_e_.']

9．什么字符串方法能用于字符串右对齐、左对齐和居中？
答：
rjust()是右对齐
ljust()是左对齐
center()是居中

10．如何去掉字符串开始或末尾的空白字符？
    答：strip()是去掉两端的空白字符
'''