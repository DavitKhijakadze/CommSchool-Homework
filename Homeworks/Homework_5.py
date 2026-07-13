import itertools, time, random, calendar
from datetime import datetime, timedelta, date

#task1
text = "ABCD"

result = len(list(itertools.product(text, repeat=2)))
print(result)

#task2
find_date = datetime.today()
day_name = find_date.strftime("%A")

if day_name == "Tuesday":
    find_date = find_date+timedelta(days=1)

while True:
    find_date = find_date+timedelta(days=1)
    day_name = find_date.strftime("%A")
    
    if day_name == "Tuesday":
        print(find_date)
        break
        
        
#task3
user_input = int(input("Enter the eyar: "))
month = 2
_, last_day = calendar.monthrange(user_input, month)

if last_day == 29:
    print("ეს წელი ნაკიანია")
else:
    print("ეს წელი ნაკიანი არ არის")
    
    
#task4

today = datetime.today()
last_day_of_year = today.replace(month=12, day=31)

week_left = round((last_day_of_year - today).days / 7, 1)
print(week_left)


#task5

digits = [1,2,3,4,5]

possible_options = list(itertools.combinations(digits, 3))
print(possible_options)


#task6

import itertools

input_string = "XYZ"
all_combinations = []

for length in range(1, 4):
    for combo in itertools.combinations(input_string, length):
        joined_word = "".join(combo)
        all_combinations.append(joined_word)

output_result = ", ".join(all_combinations)
print(output_result)


#task7

start_time = time.time()
random_number = random.randint(1,20)

while True:
    user_input = input("guess the number: ")
    end_time = time.time()
    duration = round(end_time - start_time,1)
    
    if duration > 5:
        print("you lose")
        print(f"time duration: {duration}")
        break
        
    if user_input == random_number and duration <= 5:
        print(f"it's correct. comp number{random_number} - your number{user_input}")
        print(f"time duration: {duration}")
        break
    else:
        print("try again")
        continue
        
        
#task8
start = datetime.now()
player1 = start + timedelta(seconds=random.randint(5,20))
player2 = start + timedelta(seconds=random.randint(5,20))
player1_time = player1 - start
player2_time = player2 - start

if player1_time > player2_time:
    print(f"player2 won! player1 time {player1_time} - player2 time {player2_time}")
elif player1_time < player2_time:
    print(f"player1 won! player1 time {player1_time} - player2 time {player2_time}")
else:
    print("its draw")



#task9

today = date.today()
birthday = date(2000, 12, 10)
next_birthday = date(today.year, birthday.month, birthday.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_left = (next_birthday - today).days

print(days_left)


#task10

secret_password = tuple(random.choices(range(1, 7), k=4))
all_combinations = itertools.product(range(1, 7), repeat=4)
counter = 0

for guess in all_combinations:
    counter +=1
    print(f"try {counter}: {guess}")
     
    if guess == secret_password:
        print(f"password match: {guess}")
        break

"""

git checkout main & git pull origin main

git checkout -b exercises-1-6

git push origin exercises-1-6

git checkout main

git checkout -b exercises-7-10

git push origin exercises-7-10

git checkout main

git merge exercises-1-6

git merge exercises-7-10

git push origin main

"""