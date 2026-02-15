print("WELCOME TO THE KAUN BANEGA CROREPATI")

questions=[["who is father of nation",
      "1. Mahatma Gandhi",
      "2. Jawaharlal Nehru",
      "3. Bose",
      "4. Bhagat Singh",
      1],
      ["What is the Capital of India?",
     "1. Mumbai",
     "2. Delhi",
     "3. Kolkata",
     "4. Chennai",
     2],

    ["Which language is used for Data Science?",
     "1. C++",
     "2. Java",
     "3. Python",
     "4. HTML",
     3],

    ["Who invented the Light Bulb?",
     "1. Newton",
     "2. Einstein",
     "3. Edison",
     "4. Tesla",
     3]
    ]
prizes=[1000,5000,10000,50000]
money=0
for i in range(len(questions)):
    print("\n-----------------------------------")
    print(f"Question for Rs.{prizes[i]}")
    print(questions[i][0])
    print(questions[i][1])
    print(questions[i][2])
    print(questions[i][3])
    print(questions[i][4])

    answer=int(input("enter your answer (1-4): "))
    
    if(answer==questions[i][5]):
        print("right answer")
        money=prizes[i]
    else:
        print("wrong answer")
        break    

print("\n-----------------------------------")
print(f"🎊 You are taking home Rs. {money}")
print("Thanks for playing KBC!")