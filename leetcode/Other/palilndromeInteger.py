#palindrome integer
def isPalindrome(n):
        y = n
        if n <= 0 :
            return False
        elif n > 0 :
            rev = 0
            while n != 0 :
                x = rev + n % 10
                n = n//10
                if n > 0:
                    rev = x *10
            if y == x:
                 return True
            else : 
            	return False
       	else :
            return False

a=isPalindrome(50)
b=isPalindrome(121)
c=isPalindrome(-12)
print(a,b,c)