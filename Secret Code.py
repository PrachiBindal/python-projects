#convert english into secret code
convert=input("do you want to code or Decode ")
message=input("what is the message ")
print(type(message))
print(type(message[0]))
message=message.split(" ")
def reverse(x):
    return x[::-1]
def coder(x):
    # y=x[0]
    # x=x.replace(x[0],"")
    # x='pop'+ x[:]+ y + 'how'
    # return x
    y='pop'+ x[1:] + x[0] +'how' 
    return y
def Decoder(x):
    # for i in range(0,2):
    #     x=x.replace(x[i],"")
    #     x=x.replace(x[-(i+1)],"")
    # y=x[-1]
    # x=x.replace(x[-1],"")
    # x=y+x[:]
    # return x
    y=x[-4]+x[3:-4]
    return y
def code(message): 
    new_message=[]
    for word in message:
        if len(word)<3:
            new_message.append(reverse(word))
        else:
            new_message.append(coder(word).strip())
            
    return (" ".join(new_message))  
def Decode(message):
    new_message=[]
    for word in message:
        if len(word)<3:
            new_message.append(reverse(word))
        else:
            new_message.append(Decoder(word).strip())
            #print(type(new_message))
    return (" ".join(new_message))  
# x='how are you'
# print(reverse('how'))
# code(x)                         
if convert.lower()=='code':
    print(code(message))
elif convert.lower()=='decode':
    print(Decode(message))