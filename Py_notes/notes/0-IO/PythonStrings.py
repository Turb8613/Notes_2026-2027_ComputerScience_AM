'''
    Primitive: 
        Integers, floats, bit, boolean, char

    Non primitive 
        string,list 
    string type data 
        - non primitive 
        - made up of other data types 
        - SEQUENCE data type => iterable
            iterable == you can access each element
            technically called a char array or a list of chars
'''
#NO MATTER WHAT - all data input is a string by default

num1 = input("number: ")
num2 = input("number: ")
print(int(num1) +float(num2))
'''
 int => converts somthing to an int 
 float => converts somthing to an float 
 eval => lets python figure it out
'''

# ' " ''' """ they're are all strings!*

print('bob')
print("bob")
print('''bob''')
print("""bob""")
#has to start and stop with the same string started so no ' " or """ '''
print("""
I can write anything in this area while its spaced out
                bob""")
print("It's a trap")
print('''"It's a trap" quoted by Admiral ackbar''')
print("\"It's a trap\" quoted by Admiral ackbar")
'''
    escape characters
        \n == newline
        \" == "
        \t == Tab
        \\s == space (not really anymore)
        \b == backspace
        \\d == delete
        \\ == \ 
'''

########### ITERABLES ##################
first = "Brett" #Hey wait thats me 
last = "Crawdaddy" # that is NOT me

print (first + " " + last)  #concatenates
print (first *2)  #concatenates

fullname=""
fullname+=first #fullname = fullname + first
fullname+=last
print(fullname)

fullname*=200
print(fullname)

print(len(fullname))        #len() will tell me the length

print(first[0])
print(first[3])
#print(first[5])

username= f"{first}.{last}"
email = username+"@stu.evsck12.com"
print(email) 
print(len(email))

#ett.c
print(email[2:7])
# aw dad
print (email[8:13])
#.com
print(email[27:31])
print(email[len(email)-4:])
print(email[-4:])


#print backwards
print(email[::-1])
print(email[::-2])  #print ever other
print(email[2::4]) #print from 2 by the end of 4

import string
print(string.ascii_letters)
print(string.ascii_lowercase[::-1])
