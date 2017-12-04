#coding:utf-8

fin = open('C:\Users\LzyRapx\PycharmProjects\untitled\words.txt')

def has_no_e(string):
    string = string.lower()
    for character in string:
        if character == 'e':
            return False
    return True

count = 0
no_e = 0
while True:
    line = fin.readline()
    if line:
        count+=1
        if has_no_e(line):
            no_e+=1
    if not line:
        break

print no_e
print 100.0/count * no_e
