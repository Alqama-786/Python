# So in this program u have to answer all the asked question if u win u will get the money accordingly.

questions = ["What is React.js?", "Why use React?", "What are the features of React?", "What is Node.js?"]
answers = ["React is a JavaScript library used to create single page application.", "React help us to create high performance web applications.", "React provides Component-Based Architecture for reusable UI pieces, the efficient Virtual DOM for fast updates.", 
           "A JavaScript backned framework for bulding apis and handling complex backend apis and logic."]
questions = ["1","2","3","4"]
answers = ["1","2","3","4"]
amount = 0

for i in range(len(questions)):
    print(f"Question for ${ (i+1)*1000 } : { questions[i] }")
    user_answer = input("Your Answer: ")
    if user_answer.strip().lower() == answers[i].strip().lower():
        amount += (i+1)*1000
        if i == len(questions) - 1:
            print(f"Your all the answers are correct! Amount You Won: ${amount}.")
            break
        print(f"Correct! You have won ${ (i+1)*1000 }. Total amount: ${ amount }")
    elif user_answer.strip().lower() != answers[i].strip().lower():
        if i <= len(answers):
            print(f"Wrong Answer! The correct answer is: { answers[i] }")
            user_answer = input("Do you want to move to another question? y or n: ")
            if user_answer == "Y":
                continue
            elif user_answer == "N":
                break
            else:
                print("Invalid entry!")
    else:
        print(f"Wrong Answer! The correct answer is: { answers[i] }")
        print(f"You leave with ${ amount }")
        break