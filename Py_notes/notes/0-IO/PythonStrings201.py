'''
    Ask the user for their email
    Print out their username in the formaat of 
        Welcome {username}!

'''

email = input("Email:")
username = email[0:email.find("@")] #if not found return -1
#retuns -1 because us as the programers say its an error
print(email)
print(f"Welcome {username}")
first = username[0:username.index(".")] #if not found break program
last = username[username.index(".")+1:]
print(first.title(),last.title())

name = "zoe"
#name[0] = "Z" this is a no no
name = name.replace("z","Z")    #It returns the replaced version
print(name)

'''
    Other common methods
        strip, lstrip, rstrip == removes the extra blank spaces
        startswith and endwith == searching tools
        split == splits bases on a character but returns a list
'''
