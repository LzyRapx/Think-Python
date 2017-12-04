#coding:utf-8

"""
最近我看忘了妈妈，然后我们发我的年龄反过来正好是她的年龄。例如，假如他是73岁，
我就是37岁了。我们好奇这种情况发生多少次，但中间叉开了话题，没有想出来这个问题的
答案。
我回家之后，我发现到目前位置我们的年龄互为逆序已经是六次了，我还发现如果我们幸运
的话过几年又会有一次，如果我们特别幸运，就还会再有一次这样情况。换句话说，就是总
共能有八次。那么问题来了：我现在多大了？
写一个 Python 程序，搜索一下这个谜语的解。提示一下：你可能发现字符串的 zfill 方法很有
用哦
"""
def birthday(string):
    string = int(string)
    string = string + 1
    string = str(string)
    return  string

def rev_age(string):
    return string[::-1]

def solve():
    age = '0'
    for i in  range(100):
        if int(rev_age(age)) < int(age):
            if abs(int(rev_age(age)) - int(age)) > 13 \
                and abs(int(rev_age(age)) - int(age)) < 45:
                print 'Monther age:',age,'Son age:',rev_age(age),'difference:',abs(int(rev_age(age)) - int(age))
        age = birthday(age)

if __name__ =='__main__':
    solve()
"""
Monther age: 20 Son age: 02 difference: 18 y
Monther age: 30 Son age: 03 difference: 27
Monther age: 31 Son age: 13 difference: 18 y
Monther age: 40 Son age: 04 difference: 36
Monther age: 41 Son age: 14 difference: 27
Monther age: 42 Son age: 24 difference: 18 y
Monther age: 51 Son age: 15 difference: 36
Monther age: 52 Son age: 25 difference: 27
Monther age: 53 Son age: 35 difference: 18 y
Monther age: 62 Son age: 26 difference: 36
Monther age: 63 Son age: 36 difference: 27
Monther age: 64 Son age: 46 difference: 18 y
Monther age: 73 Son age: 37 difference: 36
Monther age: 74 Son age: 47 difference: 27
Monther age: 75 Son age: 57 difference: 18 y
Monther age: 84 Son age: 48 difference: 36
Monther age: 85 Son age: 58 difference: 27
Monther age: 86 Son age: 68 difference: 18 y
Monther age: 95 Son age: 59 difference: 36
Monther age: 96 Son age: 69 difference: 27
Monther age: 97 Son age: 79 difference: 18 y
"""
