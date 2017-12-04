#coding:utf-8

def is_power(a,b):
    if a%b==0:
        if a/b==1:
            return True
        else:
            return is_power(a/b,b)
    else:
        return False

if __name__ == "__main__":
     if is_power(125,5)==True:
         print "YES"
     else:
         print "No"

