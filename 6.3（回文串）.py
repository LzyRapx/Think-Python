#coding:utf-8

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print middle("prthk")
print middle("jdf")

def is_palindrome(word):
    if first(word) == last(word) and len(middle(word)) == 0:
        return True
    elif first(word) == last(word) and len(middle(word)) > 0:
        return is_palindrome(middle(word))
    else:
        return False

if __name__ == "__main__":
    
    if is_palindrome("redivider")==True:
        print "Yes,it is a palindrome!"
    else:
        print "NO,it is not a palindrome!"

