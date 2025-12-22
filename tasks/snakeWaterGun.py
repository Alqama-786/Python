import inquirer
import random

options = ["Snake", "Water", "Gun"]

usrInp = inquirer.prompt([inquirer.List('choice', message="Choose one of these? To play the game.", choices=options)])

def gameResult(c, u):
    if c == u: return 0
    if c == 0 and u == 2: return -1
    if c == 1 and u == 1: return -1
    if c == 2 and u == 0: return -1

    return 1

c = random.randint(0, 2)
u = options.index(usrInp["choice"])

result = gameResult(c, u)

if result == 0:
    print(f"Its a Draw! Computer chooses: {options[c]}.")
elif result == -1:
    print(f"Computer Wins! He chooses: {options[c]}.")
else:
    print(f"You Wins! Computer chooses: {options[c]}.")