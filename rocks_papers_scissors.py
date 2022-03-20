import random

def play():
    print("Enter your Choice")
    user = input(" 'r' for rock, 'p' for paper ,'s' for scissor: ")
    computer = random.choice(['r', 'p', 's'])

    if computer == user:
        return "You Tied"
    elif is_win(user, computer):
        return f" Computer's {computer} You Won !"

    return f" Computer's {computer} You Lost :("

def is_win(user, computer):
    # r > s, s > p, p > r
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    else:
        return False


answer = play()
print(answer)
