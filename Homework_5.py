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