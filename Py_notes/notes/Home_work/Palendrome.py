#https://stackoverflow.com/questions/64297253/checking-whether-a-number-is-a-palindrome-getting-nameerror

numb = input("what is your 3 diget number")

if str(numb)== str(numb)[::-1]:print("Number is a palendrome")
else:print("number is not a palendrome")