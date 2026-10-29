'''
    For and while loop
    while loop is... while somthing is happing (boolean expression is true) 
        do this algorithom

    real life example
        - while sky is dark sleep
        - while light is red, stop
        - while under water, dont breath
    Progaming Ex:
    -while not lights.active():
        sleep
    do somthing forever
    repeat actions 
    ask a question until correct input

'''

#print 0-9

i=10 # i is typicaly for an ittorator
while(i>=-1):
    print(i,end=",")
    i-=1


i=0 # i is typicaly for an ittorator
while(i<=10):
    print(i,end=",")
    i+=1
   



i=-11 # i is typicaly for an ittorator
while(i<=10):
    print(i,end=",")
    i+=1


i=96
while(i<=122):
    let=chr(i)
    print(let)
    i+=1

i=65
while(i<=90):
    print(chr(i),end=",")
    i+=1
i=1
while(i!=2):
    print(i)
    i*=10
