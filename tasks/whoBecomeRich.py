import inquirer

questions = {
    "What is React.js?": [
        "A JavaScript library used to create single page application.",
        "A backend framework for building APIs.",
        "A database management system.",
        "A CSS framework for styling web pages.",
        0
    ],
    "Why use React?": [
        "To manage server-side logic.",
        "To handle database operations.",
        "To style web pages.",
        "To create high performance web applications.",
        3
    ],
    "What are the features of React?": [
        "MVC Architecture, SQL Integration, RESTful APIs.",
        "NoSQL Database, Server-Side Rendering, Middleware.",
        "Component-Based Architecture, Virtual DOM, JSX.",
        "Responsive Design, Grid System, Preprocessors.",
        2
    ],
    "What is Node.js?": [
        "A frontend library for building user interfaces.",
        "A JavaScript backend framework for building APIs and handling complex backend logic.",
        "A database management system.",
        "A CSS framework for styling web pages.",
        1
    ]
}
wrongAnsTimes = []
amount = 0

for index, question in enumerate(questions):
    ans = inquirer.prompt([inquirer.List('answer', message=f"Question for ${ (index+1)*1000 } : {question}", choices=questions[question][:-1])])
    user_answer = ans["answer"]
    correctAnsIdx = questions[question][-1] # Last index contains the correct answer index in the questions dict.
    if user_answer == questions[question][correctAnsIdx]:
        amount += (index+1)*1000
        if index == len(questions) - 1:
            print(f"Your all the answers are correct! Amount You Won: ${amount}.")
            break
        print(f"Correct! You have won ${ (index+1)*1000 }. Total amount: ${ amount }")
    elif user_answer != questions[question][correctAnsIdx]:
        if index <= len(questions) - 1:
            wrongAnsTimes.append(True)
            if int(wrongAnsTimes.count(True)) >= 2:
                amount = 0
                print(f"Wrong Answer! The correct answer is: {questions[question][correctAnsIdx]}")
                print(f"You leave with $0, Better luck next time.")
                break

            print(f"Wrong Answer! The correct answer is: { questions[question][correctAnsIdx] }")
            user_answer = input("If you give 2 wrong answers your money will be lost. Do you want to continue? (y/n): ")
            if user_answer.lower() == "y":
                continue
            elif user_answer.lower() == "n":
                break
            else:
                print("Invalid entry!")
    else:
        print(f"Wrong Answer! The correct answer is: {questions[question][correctAnsIdx]}")
        print(f"You leave swith ${ amount }")
        break