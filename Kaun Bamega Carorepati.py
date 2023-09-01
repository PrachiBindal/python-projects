#exercise 3
# kaun Banega Carorepati
questions_ans=[]
print(type(questions_ans))
questions_ans.append("what is the capital of india")
questions_ans.append("Delhi")
questions_ans.append("Banglore")
questions_ans.append("Mumbai")
questions_ans.append("New Delhi")
questions_ans.append("New Delhi")
questions_ans.append("who is the prime minister of india")
questions_ans.append("Narendra Modi")
questions_ans.append("jay shankar prasad")
questions_ans.append("kejriwal")
questions_ans.append("yogi")
questions_ans.append("Narendra Modi")
questions_ans.append("how many states are there in India")
questions_ans.append("29")
questions_ans.append("30")
questions_ans.append("28")
questions_ans.append("27")
questions_ans.append("28")
print(questions_ans[0])
print("1.",questions_ans[1],"\t2.",questions_ans[2])
print("3.",questions_ans[3],"\t4.",questions_ans[4])
answer=input("what is the answer: ")
money=1000
i=0
while(answer==questions_ans[6*i+5] ):
    print("you won",money)
    money=money*(10.1)
    i=i+1
    if i>=3:
        print("you won")
        break
    print("next question is ")
    print(questions_ans[6*i])
    print("1.",questions_ans[6*i+1],"\t2.",questions_ans[6*i+2])
    print("3.",questions_ans[6*i+3],"\t4.",questions_ans[6*i+4])
    answer=input("what is the answer ")
else:
    if i==0:
        print("you lost ,the money you won is 0")
    else:    
        message=f"you lost,the money you won is {(money/10.1):.1f}"
        print(message)    