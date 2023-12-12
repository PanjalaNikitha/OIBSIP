import random
import string
def pass_gen(length):
    char=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(char) for i in range(length))
    return password
while(1):
    n=int(input("enter the length:"))
    if n>=6:
     password=pass_gen(n)
     print(password)
     exit(0)
    else:
       print("the length should be atleast 6")


  
