import logging
import random
import time

#task1

word = "CODE"

def text_generator(text):
    for char in text:
        yield char

gen_object = text_generator(word)

print(next(gen_object))
print(next(gen_object))
print(next(gen_object))


#task2

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

user_input = input("Enter an index (number): ")

try:
    index = int(user_input)
    
    element = arr[index]
    print(f"The element at index {index} is: {element}")
except ValueError:
    print("Invalid input. Please enter numbers only")
except IndexError:
    print(f"Please enter a number between 0 and {len(arr) - 1}")


#task3

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"გამოძახება: {wrapper.count}")
        
        return func(*args, **kwargs)
    
    wrapper.count = 0
    return wrapper

@counter
def say():
    print("Hi")

say()
say()


#task4

logging.basicConfig(
    filename="game.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

questions = {
    "What is 5 + 7? ": 12,
    "What is 9 * 6? ": 54,
    "What is 100 / 4? ": 25,
    "What is 15 - 8? ": 7,
    "What is 3 ^ 3 (3 cubed)? ": 27
}

total_score = 0
current_question = 1

for question, correct_answer in questions.items():
    try:
        user_answer = int(input(f"Question {current_question}: {question}"))
        
        if user_answer == correct_answer:
            score = 10
            print("Correct! (+10 points)\n")
        else:
            score = 0
            print(f"Incorrect! The correct answer was: {correct_answer} (+0 points)\n")
            
    except ValueError:
        score = 0
        print("Invalid input! You scored 0 points for this question.\n")
    
    logging.info(f"Question {current_question}: Scored = {score} points")
    total_score += score
    current_question += 1

print(f"Game Over! Your total score is: {total_score} / 50")
logging.info(f"Game finished. Total Score: {total_score} / 50\n" + "="*40)


#task5

logging.basicConfig(
    filename="quiz.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

quiz_dict = {
    "What is 5 + 7? ": 12,
    "What is 9 * 6? ": 54,
    "What is 100 / 4? ": 25,
    "What is 15 - 8? ": 7,
    "What is 3 ^ 3 (3 cubed)? ": 27
}

def question_generator(data_dict):
    for question, answer in data_dict.items():
        yield question, answer

total_score = 0
question_number = 1

questions = question_generator(quiz_dict)

for question_text, correct_answer in questions:
    try:
        user_answer = int(input(f"question {question_number}: {question_text}"))
        
        if user_answer == correct_answer:
            score = 10
            print("Correct! (+10 point)\n")
        else:
            score = 0
            print(f"incorrect! correct answer is: {correct_answer}\n")
            
    except ValueError:
        score = 0
        user_answer = "Invalid"
        print("invalid input. 0 point\n")
    
    logging.info(f"question {question_number}: user answer = {user_answer}, point = {score}")
    
    total_score += score
    question_number += 1

print(f"test finished! total points: {total_score} / 50")

logging.info(f"total points: {total_score} / 50\n" + "="*45)


#task6

logging.basicConfig(
    filename="rock_paper_scissors.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

computer_score = 0
gamer_score = 0

moves = {
    1: "rock", 
    2: "paper", 
    3: "scissor"
}

logging.info("New Game Started")

while computer_score < 3 and gamer_score < 3:
    try:
        gamer_input = int(input("Enter one of them (1 - rock, 2 - paper, 3 - scissor): "))
        
        if gamer_input not in moves:
            print("Invalid choice! Please choose 1, 2, or 3\n")
            continue
            
        computer_choice = random.choice(list(moves.keys()))
        
        gamer_move = moves[gamer_input]
        computer_move = moves[computer_choice]
        
        print(f"Your move: {gamer_move} | Computer's move: {computer_move}")

        if gamer_move == computer_move:
            print("It's a draw, continue game!\n")
            log_msg = f"Draw! Both chose {gamer_move}."
            
        elif (gamer_move == "rock" and computer_move == "scissor") or \
             (gamer_move == "scissor" and computer_move == "paper") or \
             (gamer_move == "paper" and computer_move == "rock"):
            
            gamer_score += 1
            print(f"You won this round! Score -> You: {gamer_score} | Computer: {computer_score}\n")
            log_msg = f"Gamer won round with {gamer_move} against {computer_move}"
            
        else:
            computer_score += 1
            print(f"Computer won this round! Score -> You: {gamer_score} | Computer: {computer_score}\n")
            log_msg = f"Computer won round with {computer_move} against {gamer_move}"
            
        logging.info(f"{log_msg} Current Score - Gamer: {gamer_score}, Computer: {computer_score}")

    except ValueError:
        print("Please enter a valid number (1, 2, or 3)!\n")

if gamer_score == 3:
    winner_message = f"Congratulations! Gamer won the game with score {gamer_score}:{computer_score}!"
else:
    winner_message = f"Game Over! Computer won the game with score {computer_score}:{gamer_score}"

print(winner_message)

logging.info(f"Game Finished. {winner_message}\n" + "-"*50)


#task7

def roll_dice():
    return random.randint(1, 6)

def play_round():
    while True:
        input("\nGamer 1, press Enter to roll the dice")
        p1_roll = roll_dice()
        print(f"Gamer 1 rolled: {p1_roll}")
        
        input("Gamer 2, press Enter to roll the dice")
        p2_roll = roll_dice()
        print(f"Gamer 2 rolled: {p2_roll}")
        
        if p1_roll > p2_roll:
            print("Gamer 1 wins this round!")
            return "Gamer 1", "Gamer 2"
        elif p2_roll > p1_roll:
            print("Gamer 2 wins this round!")
            return "Gamer 2", "Gamer 1"
        else:
            print("It's a tie! Rolling again")
            time.sleep(1)

game_active = True

while game_active:
    winner, loser = play_round()
    
    print(f"\n{winner}, you won!")

    user_choice = input(f"Do you want to give {loser} another chance? (y/): ").strip().lower()
    
    if user_choice == "y":
        print(f"\n{winner} accepted the challenge! Starting a new round")
        time.sleep(1)
    else:
        print(f"\n{winner} declined. Game over!")
        game_active = False


#task8

words = ["apple", "house", "happy", "river", "cloud", "smile", "window", "friend", "coffee", "guitar"]

choice1 = random.choice(words)
words.remove(choice1)
choice2 = random.choice(words)

def hide_letters(word):
    word_list = list(word)
    indices_to_hide = random.sample(range(len(word)), 2)
    
    for index in indices_to_hide:
        word_list[index] = "_"
        
    return "".join(word_list)

hidden1 = hide_letters(choice1)
hidden2 = hide_letters(choice2)

print("Fill in the missing letters and type the full word\n")

print(f"First word: {hidden1}")
user_guess1 = input("Your answer: ").strip().lower()

print(f"\nSecond word: {hidden2}")
user_guess2 = input("Your answer: ").strip().lower()

correct_count = 0

if user_guess1 == choice1:
    correct_count += 1
if user_guess2 == choice2:
    correct_count += 1

if correct_count == 2:
    print("Victory!")
elif correct_count == 1:
    print("50%")
else:
    print(f"you lose! The correct words were: {choice1} and {choice2}")
